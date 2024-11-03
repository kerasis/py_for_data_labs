import json

def main(): 
    with open('ex_2.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    phone_dict = {member["name"]: member["phoneNumber"] for member in data["members"]}
    print(phone_dict) 
    
if __name__ == "__main__":
    main()
