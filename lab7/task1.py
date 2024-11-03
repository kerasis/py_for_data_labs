from jsonschema import validate, ValidationError, SchemaError
import json
def validate_json(data, schema):
    try:
        validate(instance=data, schema=schema)
        print("соответствует схеме.")
    except ValidationError as ve:
        print("ошибка валидации :", ve.message)
     
    except SchemaError as se:
        print("ошибка", se.message)

def main():
    correct_json = 'ex_1.json'
    wrong_json = 'ex_1_err.json'
    
    with open(correct_json, 'r', encoding='utf-8') as f:
        data_c = json.load(f)
    
    with open(wrong_json, 'r', encoding='utf-8') as f:
        data_w = json.load(f)

    with open( 'ex_1schema.json', 'r', encoding='utf-8') as f:
        schema = json.load(f)

    validate_json(data_c, schema)
    validate_json(data_w, schema)
    
if __name__ == "__main__":
    main()

