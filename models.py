

class Field(object):

    def __init__(self, name, data, for_write=False):
        self.name = name
        self.data = data
        self.required = data.get('required', False)
        self.read_only = data.get('readOnly', False)
        self.write_only = data.get('writeOnly', False)
        self.type = data.get('type', '')
        self.format = data.get('format', '')
        self.items = data.get('items', {})

        if self.type == 'array':
            itme_type = list(data['items'].values())[0]
            self.type = itme_type + '[]'
            if 'serializer' in self.type.lower() and for_write:
                self.type = 'Write' + self.type

        self.required_json = 'true' if self.required else 'false'

    def __repr__(self):
        return self.name


class Serializer(object):

    def __init__(self, data):
        self.data = data
        self.id = data['id']

        if self.id.startswith('Write'):
            self.name = self.id[5:]
            self.category = 'write'
        else:
            self.name = self.id
            self.category = 'read'

        self.fields = []
        for field_name, field_data in data['properties'].items():
            for_write = (self.category == 'write')
            field = Field(field_name, field_data, for_write)
            self.fields.append(field)

    def __repr__(self):
        return self.id


class Parameter(object):
    
    def __init__(self, data):
        self.data = data
        self.param_type = data['paramType']
        self.name = data['name']
        self.type = data.get('type')
        self.required = data.get('required', False)
        self.description = data.get('description')
        self.enum = data.get('enum', [])

        self.required_json = 'true' if self.required else 'false'

    def __repr__(self):
        return self.name


class Operation(object):
    
    def __init__(self, data):
        self.patch = None
        self.data = data

        self.nickname = data['nickname']
        self.notes = data['notes']
        self.summary = data['summary']
        self.method = data['method'].lower()
        self.type = data['type']
        self.items = data.get('items', {})

        self.action_name = self.nickname.strip().split('_')[-1]

        self.path_parameters = []
        self.query_parameters = []
        self.form_parameters = []

        for parameter_data in data['parameters']:
            parameter = Parameter(parameter_data)

            if parameter.param_type == 'path':
                self.path_parameters.append(parameter)

            if parameter.param_type == 'query' and self.action_name == 'list':
                self.query_parameters.append(parameter)

            if parameter.param_type == 'form':
                self.form_parameters.append(parameter)

        self.serializer_name = self.type
        if self.serializer_name == 'array':
            self.serializer_name = self.items.get('$ref', '') + '[]'

        self.serializer_name_write = self.serializer_name
        if 'serializer' in self.serializer_name_write.lower():
            self.serializer_name_write = 'Write' + self.serializer_name_write

    def __repr__(self):
        return self.nickname


class Api(object):

    def __init__(self, data):
        self.data = data
        self.path = data['path']
        self.description = data['description']
        self.operations = []
        for operation_data in data['operations']:
            operation = Operation(operation_data)
            self.operations.append(operation)

    def __repr__(self):
        return '<API:%s>' % self.path

    def match_patches(self, patches):
        for operation in self.operations:
            for patch in patches:
                if patch.path == self.path and patch.method == operation.method:
                    assert patch.matched == False
                    patch.matched = True
                    operation.patch = patch


class Patch(object):

    def __init__(self, path, method):
        self.path = path
        self.method = method.lower()
        self.content = '\n'
        self.matched = False

    def __repr__(self):
        return '<Patch:%s %s>' % (self.path, self.method)

    def append_content(self, line):
        self.content += line.rstrip() + '\n'
        






