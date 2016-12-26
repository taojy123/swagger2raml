import json
import step
import urllib2
import os
from models import Api, Serializer

# support swagger version: 1.2

ROOT_URL = 'http://heidianapi.com/api/docs/api-docs/'
OUTPUT_DIR = './result'


if __name__ == '__main__':

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    page = urllib2.urlopen(ROOT_URL).read()
    data = json.loads(page)

    for sub_api_data in data['apis']:

        sub_url = ROOT_URL.strip('/') + sub_api_data['path']
        name = sub_url.strip('/').split('/')[-1]
        print('================ %s ==================' % name)
        print(sub_url)

        page = urllib2.urlopen(sub_url).read()
        data = json.loads(page)


        apis = []
        for api_data in data['apis']:
            api = Api(api_data)
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


print('finish!')


