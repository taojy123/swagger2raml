#coding=utf8

import os
import sys
import re
import json
import getopt
import step

from models import Api, Serializer, Patch

PY3 = sys.version_info[0] == 3


# ======== support swagger version: 1.2 ========

TITLE_PREFIX = u''  #u'嘿店开放平台 API '
ROOT_URL = 'http://heidianapi.com/api/docs/api-docs/'
OUTPUT_DIR = './result/'
PATCH_DIR = './patch/'
GENERATE_HTML = False


def get_data(url):
    if PY3:
        import urllib.request
        data = urllib.request.urlopen(url).read()
        data = data.decode()
    else:
        import urllib2
        data = urllib2.urlopen(url).read()
    return json.loads(data)


def get_all_patches(patch_dir):
    patches = []
    for name in os.listdir(patch_dir):
        patch_path = os.path.join(patch_dir, name)
        api_path  = ''
        method = ''
        patch = None
        for line in open(patch_path).readlines():
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
  -i, --input  <api_root_url>   Such as: 'http://xxx.com/api/docs/api-docs/'
  -o, --output  <result_dir>    Such as: './result/'
  -t, --title  <title_prefix>   Such as: 'My_First_Api'
  -p, --patch  <patch_dir>      Such as: './patch/'
  --html                        Generate html files
"""
    print(text)
    sys.exit()


if __name__ == '__main__':

    try:
        options, args = getopt.getopt(sys.argv[1:], 'hi:o:t:p:', ['help', 'input=', 'output=', 'title=', 'patch='])

        for name, value in options:
            if name in ['-h', '--help']:
                usage()
            elif name in ['-i', '--input']:
                ROOT_URL = value
            elif name in ['-o', '--output']:
                OUTPUT_DIR = value
            elif name in ['-t', '--title']:
                TITLE_PREFIX = value.replace('_', ' ')
            elif name in ['-p', '--patch']:
                PATCH_DIR = value
            elif name in ['--html']:
                GENERATE_HTML = True

    except getopt.GetoptError:
        usage()

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    base_uri = re.findall(r'^(.+?//.+?)/', ROOT_URL)[0]
    patches = get_all_patches(PATCH_DIR)
    data = get_data(ROOT_URL)

    for sub_api_data in data['apis']:

        sub_url = ROOT_URL.strip('/') + sub_api_data['path']
        name = sub_url.strip('/').split('/')[-1]
        print('================ %s ==================' % name)
        print(sub_url)

        title = TITLE_PREFIX + name

        data = get_data(sub_url)

        apis = []
        for api_data in data['apis']:
            api = Api(api_data)
            if api in apis:
                continue
            api.match_patches(patches)
            apis.append(api)

        print(apis)

        serializers = []
        for serializer_name, serializer_data in data['models'].items():
            serializer = Serializer(serializer_data)
            serializers.append(serializer)

        print(serializers)

        others = {}
        template = open('template.raml').read()
        page = step.Template(template).expand(locals())     
        if not PY3:   
            page = page.encode('utf8')

        output_path = os.path.join(OUTPUT_DIR, '%s.raml' % name)
        open(output_path, 'w').write(page)


print('================ Other Patches ==================')
name = 'other'
title = TITLE_PREFIX + name
apis = []
serializers = []
others = {}
for patch in patches:
    print(patch, patch.matched)
    if patch.matched:
        continue
    others[patch.path] = others.get(patch.path, [])
    others[patch.path].append(patch)

template = open('template.raml').read()
page = step.Template(template).expand(locals())
if not PY3:      
    page = page.encode('utf8')

output_path = os.path.join(OUTPUT_DIR, '%s.raml' % name)
open(output_path, 'w').write(page)

print('=====================================')


if GENERATE_HTML or 1:
    print('============== raml2html ==================')

    """
    npm install -g raml2html
    raml2html -i example.raml -o example.html
    """

    HTML_DIR = os.path.join(OUTPUT_DIR, 'html')
    if not os.path.exists(HTML_DIR):
        os.mkdir(HTML_DIR)

    index_path = os.path.join(HTML_DIR, 'index.html')
    open(index_path, 'w')

    for name in os.listdir(OUTPUT_DIR):
        if name[-5:] != '.raml':
            continue
        raml_path = os.path.join(OUTPUT_DIR, name)
        html_name = name[:-5]+'.html'
        html_path = os.path.join(HTML_DIR, html_name)
        cmd = 'raml2html -i %s -o %s' % (raml_path, html_path)
        print(cmd)
        os.system(cmd)
        open(index_path, 'a').write('<p><a href="%s">%s</a></p>\n' % (html_name, html_name))

    print('=====================================')


print('Finish!')


