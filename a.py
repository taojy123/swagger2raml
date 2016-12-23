import json
import step

from models import Api, Serializer


if __name__ == '__main__':

    # swaggerVersion: 1.2
    filename = 'swagger.json'

    data = open(filename).read()

    data = json.loads(data)

    # print data

    apis = []
    for api_data in data['apis']:
        api = Api(api_data)
        apis.append(api)

    print apis

    serializers = []
    for serializer_name, serializer_data in data['models'].items():
        serializer = Serializer(serializer_data)
        serializers.append(serializer)
    
    print serializers

    template = open('template.raml').read()
    page = step.Template(template).expand(locals())        
    page = page.encode('utf8')
    open('result.raml', 'w').write(page)


