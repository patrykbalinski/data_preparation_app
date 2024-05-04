import json


def save_json(objects_list, file_path, fields='all'):
    with open(file_path, 'w', encoding='utf8') as file:
        output_list = []

        for object in objects_list:
            if fields == 'all':
                fields = object.__dict__.keys()

            output_dict = {}
            for field in fields:
                output_dict[field] = object.__dict__[field]

            output_list.append(output_dict)

        file.write(json.dumps(output_list, indent=2))
