import xml.etree.ElementTree as ET

def main():
    my_xml = 'ex_2.xml'
    
    tree = ET.parse(my_xml)
    root = tree.getroot()
    
    parent = root.find('Detail')
    
    new_item = ET.Element('Item') #добавим айтем
    ET.SubElement(new_item, "ArtName").text = "Сыр Российский"
    ET.SubElement(new_item, "Barcode").text = "2000000000124"
    ET.SubElement(new_item, "QNT").text = "666.66"
    ET.SubElement(new_item, "QNTPack").text = "666.66"
    ET.SubElement(new_item, "Unit").text = "шт"
    ET.SubElement(new_item, "SN1").text = "00000015"
    ET.SubElement(new_item, "SN2").text = "02.11.2024"
    ET.SubElement(new_item, "QNTRows").text = "10"
    
    parent.append(new_item)
    
    summ = 0.0 #пересчитаем значения
    rows = 0
    for item in parent.findall("Item"):
        quantity = float(item.find("QNT").text.replace(",", "."))
        cur_rows = int(item.find("QNTRows").text)
        summ += quantity
        rows += cur_rows

    sum_el = root.find('Summary')
    sum_el.find("Summ").text = f"{summ:.2f}".replace(".", ",")
    sum_el.find("SummRows").text = str(rows)
    
    tree.write('ex_2_edited.xml', encoding="utf-8", xml_declaration=True)

if __name__ == "__main__":
    main()
