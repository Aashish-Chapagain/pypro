# import json
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


# number_list= []
# n = int(input("Enter number: "))

# with open("contacts.json", "r") as file : 
#     contacts = json.load(file)
#     for value in contacts.values():
#         number_list.append(value["number"])
    
#     if n not in number_list : 
#          print(n)
#     else : 
#            print("already exists")





# import string 


# a = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase

# password = input("")

# contains_up = any()


# import matplotlib.pyplot as plt

# # Sample Data
# x = [1, 2, 3, 4, 5]
# y = [10, 20, 25, 30, 40]

# # Plot Graph
# plt.plot(x, y, marker='o', linestyle='--', color='b', label='Line 1')

# # Labels and Title
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Simple Matplotlib Plot")
# plt.legend()

# # Show Plot
# plt.show()



import numpy as np 

a = np.array([1,2,3])
print(a)
print(type(a))
print(a.shape)
