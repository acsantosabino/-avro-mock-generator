from Gerador import *
import json
schema = {
    'type': 'record',
    'fields': [
        {'name': 'field1', 'type': 'null'},
        {'name': 'field2', 'type': 'boolean'},
        {'name': 'field3', 'type': ['null', 'int']},
        {'name': 'field4', 'type': 'long'},
        {'name': 'field5', 'type': 'float'},
        {'name': 'field6', 'type': 'double'},
      ##  {'name': 'field7', 'type': 'bytes'},
        {'name': 'field8', 'type': 'string'},
        {
            "type": "enum",
            "name": "field9",
            "symbols": ["SPADES", "HEARTS", "DIAMONDS", "CLUBS"]
        },
        {
            "type": "array",
            "name": "field10",
            "items": 'int'
        },
        {
            "type": "array",
            "name": "field11",
            "items": {
                'type': 'record',
                'fields': [{'name': 'item_array', 'type': ['null', 'int']}, ]}
        },
        {
            "type": "record",
            "name": "field12",
            'fields': [
                {'name': 'item_record1', 'type': 'int'},
                {'name': 'item_record2', 'type': 'string'},
                {
                    "type": "array",
                    "name": "item_record3",
                    "items": {
                        'type': 'record',
                        'fields': [{'name': 'item_array', 'type': 'int'}, ]}
                },
            ]
        },
        {
            "type": "map",
            "name": "field14",
            "items": 'int'
        },
        {
            "type": "map",
            "name": "field13",
            "items": {
                        'type': 'record',
                        'fields': [{'name': 'item_array', 'type': 'int'}, ]
                      }
        }
    ],
}

with open("teste.json", "+w") as file:
  file.write(json.dumps(generateData(schema), indent=4))
print()
