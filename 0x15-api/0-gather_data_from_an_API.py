#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    # Fetch user data
    user = requests.get(url + "users/{}".format(user_id)).json()
    employee_name = user.get("name")

    # Fetch TODO list data
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Get list of completed tasks
    completed_tasks = [task.get("title") for task in todos if task.get("completed")]

    # Output format
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), len(todos)))
    for task_title in completed_tasks:
        print("\t {}".format(task_title))

