from lxml import etree

def validate(schema, xml):   #готовая схема и путь к целевому xml
    xml_doc = etree.parse(xml)
    is_valid = schema.validate(xml_doc)
    
    if is_valid:
        print(f"XML {xml} is valid.")
    else:
        print(f"XML {xml} is not valid.")
        for error in schema.error_log:
            print(f"Error: {error.message}")

            
def main():
    schema_file = 'schema_1.xsd'
    
    correct_xml = 'ex_1.xml'
    wrong_xml = 'ex_1_error.xml'
    
    with open(schema_file, 'rb') as xsd_f:
        schema_root = etree.XML(xsd_f.read())
        schema = etree.XMLSchema(schema_root)
        
    validate(schema, correct_xml)
    validate(schema, wrong_xml)

if __name__ == "__main__":
    main()
