#!/usr/bin/python3

import requests
import sys

def get_employee_data(employee_id):
    """Fetch employee data from the REST API"""
    try:
        #Fetch user data
        user_url = f'https://jsomplaceholder.typicode.com/users/{employee_id}'
        user_response = requests.get(user_url)
        user_data = user_response.json()

        #Fetch TODO list data
        todos_url = f'https://jsonplaceholder.typicode.com/todos?userId=employee_id}'
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        return user_data, todos_data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None

def main(employee_id):
    """main function to display employee TODO list progress"""
    user_data, todos_data = get_employee_data(employee_id)

    if not user_data or not todos_data:
        print("No data found.")
        return

    employee_name = user_data.get('name')
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get('completed')]
    number_of_done_tasks = len(done_tasks)

    #print the result
    print(f"Employeee {employee_name} is done with tasks"
            f"({number_of_done_tasks}/total_tasks}):")

    for task in done_tasks:
        print(f"\t {task.get('title')}")

if __name__ =="__main__":
    if len(sys.argv) !=2:
        print("Usage: todo_list.py <employee_id>")
        sys.exit(1)

        try:
            employee_id = int(sys.argv[1])
            main(employee_id)
        except ValueError:
            print("Please provide a valid employee ID as an Integer.")
            sys.exit(1)
