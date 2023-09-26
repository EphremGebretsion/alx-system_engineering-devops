#!/usr/bin/python3
"""" this script will display the to dolist info usinf id"""
from json import loads
from math import ceil
from sys import argv
from urllib import request


def tasksDone(id_no, tasks):
    """ count complited taskes"""

    last = int(id_no) * 20
    begin = last - 19
    task_done = 0
    i = begin - 1
    while (i < last):
        if tasks[i].get("completed") is True:
            task_done += 1
        i += 1

    return task_done


def printComplited(id_no, tasks):
    """ print complited tasks """

    last = int(id_no) * 20
    i = last - 20
    while (i < last):
        if (tasks[i].get("completed") is True):
            print("\t " + tasks[i].get("title"))
        i += 1


if __name__ == "__main__":

    user_req = request.urlopen("https://jsonplaceholder.typicode.com/users")
    users = loads(user_req.read().decode("UTF-8"))
    name = users[int(argv[1]) - 1].get("name")
    task_req = request.urlopen("https://jsonplaceholder.typicode.com/todos")
    tasks = loads(task_req.read().decode("UTF-8"))
    no_done = tasksDone(argv[1], tasks)
    print("Employee {} is done with tasks({}/20):".format(name, no_done))
    printComplited(argv[1], tasks)
