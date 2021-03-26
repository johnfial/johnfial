# API - Application Programming Interface (website for robots)

# requests module is used to make HTTP requests to websites
import requests

# url to access a single todo item
# url = "https://jsonplaceholder.typicode.com/todos/5"

# url to access the list of todo items
url = "https://jsonplaceholder.typicode.com/todos"

# make an HTTP GET request to url and save the HTTP response in a variable
response = requests.get(url)



# JSON - JavaScript Object Notation (JS's version of a dictionary)
# convert the response data from JSON to Python dict using .json() method of the response object
todo_list = response.json()


# loop 0-9
for index in range(0, len(todo_list), 33):
    # get the todo item at the index
    todo = todo_list[index]


    # output the todo item
    todo_display = f"""
    #{todo['id']}. {todo['title']}
    Created by: {todo['userId']}
    Completed: {todo['completed']}
    """

    print(todo_display)
