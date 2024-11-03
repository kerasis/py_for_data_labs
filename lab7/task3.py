import json

def main(): 
    with open('ex_3.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    new_data = {"id": 5,
                "total": 400.00,
                "items": [
                {
                     "name": "item 54",
                     "quantity": 2,
                     "price": 200.00
                }]}
    
    data["invoices"].append(new_data)
    
    with open("ex_3_updated.json", "w") as write_file:
        json.dump(data, write_file)
        
if __name__ == "__main__":
    main()

