import json
# import os

# # def check_for_dublicate():
# #     number = int(input())
# #     number_list = []
# #     with open("contacts.json", "r") as file :
# #      temp = json.load(file)
# #      for value in temp.values():
# #        number_list = value["number"].append(number_list)
# #        if number in number_list():
# #         print("Number already exists! Do you want to continue y/n: ")

# # check_for_dublicate()


# # a = input("enter")
# # with open("contacts.json", "r") as file :
# #     contacts = json.load(file)
# #     for key, values in contacts.items():
# #         if a== key:
# #             print(key,values)


# def save_to_json():
#     contacts = {}
#     number = int(input())
#     if os.path.exists("contacts.json"):
#         with open("contacts.json", "r") as file:
#             try:
#                 contacts = json.load(file)
#             except json.JSONDecodeError:
#                 contacts = {}
#                 contacts = json.load(file)
              
#     number_list = []
#     for value in contacts.values():
#         number_list.append(value["number"])
#     if not number in number_list:
#         with open("contacts.json", "w") as file:
#             json.dump(number, file, indent=3)
#     else:
#         print("already exists")


# save_to_json()


number_list= []
n = int(input("Enter number: "))

with open("contacts.json", "r") as file : 
    contacts = json.load(file)
    for value in contacts.values():
        number_list.append(value["number"])
    
    if n not in number_list : 
         print(n)
    else : 
           print("already exists")