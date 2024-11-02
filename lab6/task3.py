import xml.etree.ElementTree as ET

def main():
    my_xml = 'ex_3.xml'
    tree = ET.parse(my_xml)
    root = tree.getroot()
    
    for item in root.findall(".//СведТов"):
        name = item.get("НаимТов")
        quantity = item.get("КолТов")
        price = item.get("ЦенаТов")
   
        print(f"Название товара: {name}, Количество: {quantity}, Цена: {price}")

if __name__ == "__main__":
    main()

