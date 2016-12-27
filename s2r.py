#coding=utf8

import json
import step
import urllib2
import os
import sys
import re
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


if __name__ == '__main__':

    if len(sys.argv) > 1:
        TITLE_PREFIX = sys.args[1].replace('_', ' ')

    if len(sys.argv) > 2:
        ROOT_URL = sys.args[2]

    if len(sys.argv) > 3:
        OUTPUT_DIR = sys.args[3]

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    patches = get_all_patches(PATCH_FILES)

    base_uri = re.findall(r'^(.+?//.+?)/', ROOT_URL)[0]

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

        template = open('template.raml').read()
        page = step.Template(template).expand(locals())        
        page = page.encode('utf8')

        output_path = os.path.join(OUTPUT_DIR, '%s.raml' % name)
        open(output_path, 'w').write(page)


print('==================================================')
for patch in patches:
    print(patch, patch.match)

print('Finish!')


