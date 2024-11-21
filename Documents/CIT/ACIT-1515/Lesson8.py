"""
Exceptions - a technique for handline runtime errors

Syntax errors - invalid code that is caught by the interpreter before the program is run, 
and prevents the program from running

Runtime errors - errors that occur while the program is running, and are the result of invalid operations

    int('ed') --> ValueError (cannot convert non-numeric string to int)

    2 + '2' --> TypeError (cannot concatenate string to int)

    json.load(file) --> FileNotFoundError(if the file doesn't exists)



"""



# age = input('Please enter your age: ')
# if age.isdigit():
#     age = int(age)
# else:
#     print('age must be numeric')
"""
    try:
        age = input('Please enter your age: ')
    age = int(age)
        except:
        print('age must be numeric')

"""

# try:
#     with open('test.json', 'r') as file:
#         # assume we are reading a dict from a file
#         data = json.load(file)
#         """
#         student = {
#         'name': 'Akila',
#         'email': 'akila@bcit.ca'
        
#         }
#         """
#     score = input('Please enter your score: ')

# except:
#     print('catches all error types')

#     'as keyword'

# try:
#     score = int(score)
#     with open('data.json', 'r') as file:
#         data = json.load(file)
#         last_score = data['score']
#         if score > last_score:
#             print('You beat your previous score!')
# except ValueError:
#     print('Score must be a number')
# except FileNotFoundError:
#     print('File not found')
# except KeyError:
#     print('Invalid data read from file')


# try:
#     age = 'Tom'
#     age = int(age)
# except ValueError as e:
#     print('An error occured: ', e) # is a variable you declare, its get assigned the error from the interpreter

"""

'else' blocks with try/except
"""
# if the file is successfully read, pass the data into the start 

# def run(arg):
#     pass

# try:
#     with open('test.json','r') as file:
#      data = json.load(file)
#     # run(data) the program may have already crashed or we can run with ??
     
# except FileNotFoundError as e:
#     # data = []
#     # 
    
#     print(e)
# else: #only runs when no error is generated
#     run(data) #

"""
Two labs - this week choose one:
regular - difficulty, lab 7 but with exceptions, requests
advanced - writing a simple shell using pathlib

   
"""

"""
requests - library that allows yo uto fetch data from a network
"""
#pip install requests

import requests
import json

"""
REST APIS

a GET request fetches data from a server
a POST request  sends data to a server
"""
# requests.get() # fetch data

data = requests.get('https://jsonplaceholder.typicode.com/users') # fetch data from any url that returns JSON
print(data)
"""
HTTP status  codes:

200 ok
400 error
500 application
"""
if data.status_code == 200: # if status_code is 200, request was succesful 
    data = data.json() # extracts the JSON data from the HTTP response
    print(data)

