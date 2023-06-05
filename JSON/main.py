import json
import requests

# data = {
#     "data_name": "Data Name",
#     "data_info": "Data Info",
#     "data_date": 2023,
#     "is_active": True,
#     "data_types": ["data_1", ("data_2","data_3")]
# }

# json_data = """
# {
#     "data_name": "Data Name",
#     "data_info": "Data Info",
#     "data_date": 2023,
#     "is_active": true,
#     "data_types": [
#         "data_1",
#         [
#             "data_2",
#             "data_3"
#         ]
#     ]
# }
# """

# print(type(data))
# data_json_format = json.dumps(data, indent=4)

# print(type(json_data))
# data_dict_format = json.loads(json_data)
# print(data_dict_format)

# with open("data.json", "w") as f:
#     f.write(data_json_format)

# with open("data.json", "r") as f:
#     data_dict_format = json.load(f)
#     print(data_dict_format)

#-----------------------------------------------------------

# r = requests.get("https://jsonplaceholder.typicode.com/users")

# data = r.json()
# # print(data[0]["name"])

# for name in data[0:11]:
#     if name['company']:
        
#         print(name["name"])

#     with open('users_names.txt','a') as f:
#         f.write(f"{name['name']}\n")

#-----------------------------------------------------------

r = requests.get("https://jsonplaceholder.typicode.com/users")

data = r.json()
# print(data[0]["name"])

web_site = int(input("Veb saytni kiriting: "))

for name in data[0:11]:
    if name['company']:
        
        print(name["name"])

    with open('users_names.txt','a') as f:
        f.write(f"{name['name']}\n")