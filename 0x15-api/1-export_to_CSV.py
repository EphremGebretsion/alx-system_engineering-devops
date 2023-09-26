#!/usr/bin/python3
""" export the data to a CSV file """
from csv import writer
from json import loads
from urllib import request
from sys import argv


def addToList(user_id, users, tasks):
    """ creates a list for the later use """
    name = users[user_id - 1].get("name")
    my_list = []
    last = user_id * 20
    i = last - 20

    while (i < last):
        data = [str(user_id), str(name), str(tasks[i].get("completed")),
                str(tasks[i].get("title"))]
        my_list.append(data)
        i += 1

    return my_list


if __name__ == "__main__":
    user_id = int(argv[1])
    my_file = open(argv[1] + ".csv", "w")
    user_req = request.urlopen("https://jsonplaceholder.typicode.com/users")
    task_req = request.urlopen("https://jsonplaceholder.typicode.com/todos")
    users = loads(user_req.read().decode("UTF-8"))
    tasks = loads(task_req.read().decode("UTF-8"))

    my_writer = writer(my_file)
    my_writer.writerows(addToList(user_id, users, tasks))
    my_file.close()
