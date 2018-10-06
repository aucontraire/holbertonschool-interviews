#!/usr/bin/python3
# Script to gather data from an API
import json
import requests
import sys


def get_users(base_url):
    """Gets users list
       Args:
           base_url (str): base url for API
       Returns: list of users (dicts)

    """
    response = requests.get("{}users/".format(base_url))
    return response.json()


def get_todo_list(base_url, user_id):
    """Gets todo list for specific user
       Args:
           base_url (str): base url for API
           user_id (str): user id number
       Returns: list of todo items (dicts)
    """
    response = requests.get(
        "{}users/{}/todos".format(base_url, user_id))
    return response.json()


if __name__ == '__main__':
    base_url = 'https://jsonplaceholder.typicode.com/'
    users_dict = {}
    users_json = get_users(base_url)
    for user in users_json:
        user_id = user.get('id')
        username = user.get('username')
        users_dict[user_id] = []
        todo_list = get_todo_list(base_url, user_id)
        for todo in todo_list:
            todo_dict = {}
            todo_dict['username'] = username
            todo_dict['task'] = todo.get('title')
            todo_dict['completed'] = todo.get('completed')
            users_dict[user_id].append(todo_dict)

    with open('todo_all_employees.json', 'w') as f:
        json.dump(users_dict, f)
