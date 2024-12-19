'''Write a program to generate multiplication tables from 2 to 20 and write it to the
different files. Place these files in a folder for a 13 – year old.'''
import os

def createtable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n*i}\n"
    with open(f"tables/table_{n}.txt", "w") as file:
        file.write(table)

def table():
    for n in range(2, 21):
        createtable(n)

table()
