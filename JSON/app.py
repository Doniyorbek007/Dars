import json

search = input("Search in here: ")

with open("data.json", "r") as f:
    data = json.load(f)


def search_result(search):
    for user in data:
        if search == user["ishchi_nomi"]:
         print(f'Delete {user["ishchi_nomi"]}?')  

         is_delete = str(input("Yes/no: ") or "yes").lower()
         
         if is_delete == "yes":
            data.remove(user)
            with open("data.json", "w") as f:
               json.dump(data, f, indent=4)
               print(f"{user['ishchi_nomi']} deleted!")
        else:
          print(f'{search} not found!')
          break 

search_result(search)