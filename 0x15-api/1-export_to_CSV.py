#!/usr/bin/python3
"""Fetch and export TODO list data for a given employee ID in CSV format."""

import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    #Fetch user data
    user = requests.get(url + "users/{}".format(user_id)).json()
    employee_name = user.get("username")

    #Fetch TODO list data
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    #Define CSV file name
    file_name = f"{user_id}.csv"

    #Write data to CSV
    with open(file_name, mode='w' newline='', encoding='utf-8) as file:
        writer = csv.writer(file,quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                user_id,
                employee_name,
                task.get("completed"),
                task.get("title)
            ])
