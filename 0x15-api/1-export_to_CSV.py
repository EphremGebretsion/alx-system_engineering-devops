#!/usr/bin/python3
""" export the data to a CSV file """
import csv
from json import loads
from urllib import request
from sys import argv


def addToList(user_id, users, tasks):
    """ creates a list for the later use """
    name = users[user_id - 1].get("username")
    my_list = []
    last = user_id * 20
    i = last - 20

    while (i < last):
        qq = '"'
        data = [user_id, name, tasks[i].get("completed"),
                tasks[i].get("title")]
        formated_data = [str(a) for a in data]
        my_list.append(formated_data)
        i += 1

    return my_list


if __name__ == "__main__":
    user_id = int(argv[1])
    my_file = open(argv[1] + ".csv", "w")
    user_req = request.urlopen("https://jsonplaceholder.typicode.com/users")
    task_req = request.urlopen("https://jsonplaceholder.typicode.com/todos")
    users = loads(user_req.read().decode("UTF-8"))
    tasks = loads(task_req.read().decode("UTF-8"))

    my_writer = csv.writer(my_file, quoting=csv.QUOTE_ALL)
    my_writer.writerows(addToList(user_id, users, tasks))
    my_file.close()
