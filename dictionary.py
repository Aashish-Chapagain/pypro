
import json

# def check_for_dublicate():
#     number = int(input())
#     number_list = []
#     with open("contacts.json", "r") as file : 
#      temp = json.load(file)
#      for value in temp.values():
#        number_list = value["number"].append(number_list) 
#        if number in number_list():
#         print("Number already exists! Do you want to continue y/n: ")
    
# check_for_dublicate()


a = input("enter")
with open("contacts.json", "r") as file : 
    contacts = json.load(file)
    for key, values in contacts.items():
        if a== key:
            print(key,values)