# print("Hello world " * 10)

# name = "John Smith"
# age = 20
# is_new_patient = True

# name = input("what is your name? ")
# print("Hi,"+name)

# birth_year = input("Birth Year: ")
# age = 2020 - int(birth_year)
# print(age)


# multi_line = '''
# hi,Lau
#     hello world!
# Thank you!
# '''
# print(multi_line)
# print(multi_line[-2])
# print(multi_line[1:-3])

# first = "Jam"
# last = "Lau"
# str_format = f'{first} [{last}] is a coder'
# print(str_format)
#
# print(len(str_format))
# print(str_format.upper())
# print(str_format)
# print(str_format.find(last))
# print("coder" in str_format)


# import math
# print(math.floor(2.9))
# print(math.ceil(2.9))
# print(math.degrees(2.9))


# is_hot = False
# is_cold = True
# if is_hot:
#     print("it's a hot day")
# elif is_cold:
#     print("it's a cold day")
# else:
#     print("it's a lovely day")

# guess_count = 0
# guess_limit = 3
# guess_number = 8
# while guess_count < guess_limit:
#     guess_count += 1
#     guess = int(input("Guess: "))
#     if guess == guess_number:
#         print("You won!")
#         break
# else:
#     print("Sorry,you failed!")


# your_input = ""
# while 1:
#     your_input = input(">").lower()
#     if your_input == "help":
#         print("start - start the car")
#         print("stop  - stop the car")
#         print("quit  - quit the game")
#     elif your_input == "start":
#         print("The car started")
#     elif your_input == "stop":
#         print("The car stopped")
#     elif your_input == "quit":
#         break
#     else:
#         print("i do not understand")

# total = 0
# for item in range(5, 19, 3):
#     print(item)
#     total += item
# print(f"total: {total}")
#
# for item in [1, "test", True]:
#     print(item)

# for x in [5, 2, 5, 2, 2]:
#     s = ""
#     for y in range(x):
#         s += "x"
#     print(s)
# print(str(5))

# test = (1, 2, 3)
# x, y, z = test
# print(x)
# print(y)
# print(z)


# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         print(f"{self.name} is talking ...")
#
#
# someone = Person("Lau")
# someone.talk()

# import utils
#
# # from utils import find_max
# numbers = [1, 2, 10, 99, 8]
# max_number = utils.find_max(numbers)
# print(f"max number is {max_number}")

# import ecommerce.shipping
# ecommerce.shipping.calc_shipping()

# from ecommerce import shipping
# shipping.calc_shipping()


# import random
# class Dice:
#     def roll(self):
#         t = (random.randint(1, 6), random.randint(1, 6))
#         return t
# a = Dice()
# print(a.roll())


# from pathlib import Path
#
# path = Path('')
# # print(path.mkdir())
# # print(path.rmdir())
# for file in path.glob("*.py"):
#     print(file)


# import requests
#
#
# def get_html_text(url):
#     try:
#         r = requests.get(url, timeout=30)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#         return "Error"
#
#
# print(get_html_text("https://hixin.cc"))


