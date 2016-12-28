#coding=utf8

import json
import step
import urllib2
import os
import sys
import re
import getopt
from models import Api, Serializer, Patch


# ======== support swagger version: 1.2 ========

TITLE_PREFIX = u'嘿店开放平台 API '
ROOT_URL = 'http://heidianapi.com/api/docs/api-docs/'
OUTPUT_DIR = './result'
PATCH_FILES = ['./patch/notifications_patch.raml']


def get_all_patches(patch_files):
    patches = []
    for filename in patch_files:
        api_path  = ''
        method = ''
        patch = None
        for line in open(filename).readlines():
            line = line.rstrip()

            rs = re.findall(r'^(/.+):$', line)
            if rs:
                api_path = rs[0]
                continue

            rs = re.findall(r'^  (\w+):$', line)
            if rs:
                method = rs[0]
                assert api_path != ''
                patch = Patch(api_path, method)
                patches.append(patch)
                continue

            if not patch:
                continue

            patch.append_content(line)

    return patches


def usage():
    text = """
Usage:   
  python s2r.py [options]

General Options:
  -h, --help                    Show help.
  -i(--input=) <api_root_url>   Such as: 'http://xxx.com/api/docs/api-docs/'
  -o(--output=) <result_dir>    Such as: './result/'
  -t(--title=) <title_prefix>   Such as: 'My_First_Api'
  -p(--patches=) <patch_files>  Such as: 'aaa.raml,patches/bbb.raml,ccc.raml'
"""
    print(text)
    sys.exit()


if __name__ == '__main__':

    try:
        options, args = getopt.getopt(sys.argv[1:], 'hi:o:t:p:', ['help', 'input=', 'output=', 'title=', 'patches='])

        for name, value in options:
            if name in ['-h', '--help']:
                usage()
            elif name in ['-i', '--input']:
                ROOT_URL = value
            elif name in ['-o', '--output']:
                OUTPUT_DIR = value
            elif name in ['-t', '--title']:
                TITLE_PREFIX = value.replace('_', ' ')
            elif name in ['-p', '--patches']:
                PATCH_FILES = value.strip().split(',')

    except getopt.GetoptError:
        usage()

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    base_uri = re.findall(r'^(.+?//.+?)/', ROOT_URL)[0]
    patches = get_all_patches(PATCH_FILES)
    page = urllib2.urlopen(ROOT_URL).read()
    data = json.loads(page)

    for sub_api_data in data['apis']:

        sub_url = ROOT_URL.strip('/') + sub_api_data['path']
        name = sub_url.strip('/').split('/')[-1]
        print('================ %s ==================' % name)
        print(sub_url)

        title = TITLE_PREFIX + name.upper()

        page = urllib2.urlopen(sub_url).read()
        data = json.loads(page)

        apis = []
        for api_data in data['apis']:
            api = Api(api_data)
            api.match_patches(patches)
            apis.append(api)

        print(apis)

        serializers = []
        for serializer_name, serializer_data in data['models'].items():
            serializer = Serializer(serializer_data)
            serializers.append(serializer)

        print(serializers)

        expands = {}
        template = open('template.raml').read()
        page = step.Template(template).expand(locals())        
        page = page.encode('utf8')

        output_path = os.path.join(OUTPUT_DIR, '%s.raml' % name)
        open(output_path, 'w').write(page)


print('================ Expand Patches ==================')
name = 'expand'
title = TITLE_PREFIX + name.upper()
apis = []
serializers = []
expands = {}
for patch in patches:
    print(patch, patch.matched)
    if not patch.matched:
        expands[patch.path] = expands.get(patch.path, [])
        expands[patch.path].append(patch)

template = open('template.raml').read()
page = step.Template(template).expand(locals())        
page = page.encode('utf8')

output_path = os.path.join(OUTPUT_DIR, '%s.raml' % name)
open(output_path, 'w').write(page)

print('=====================================')
print('Finish!')


