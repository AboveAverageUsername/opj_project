# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
import csv
import zipfile

import sqlite3worker
from tqdm import tqdm
from zipfile import ZipFile

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
    #print("Stored blob data into: ", filename, "\n")


def get_and_unzip(db, id):
    ret = db.get_data(
        "subz",
        "num",
        id)

    if len(ret) == 0:
        return

    sub = ret[0]

    #print(sub)

    filename = sub[1][22:len(sub[1])-1]
    foldername = ".\\subs\\" + filename[:len(filename)-4]

    if os.path.exists(foldername):
        return

    print(filename)

    subPath = ".\\subs\\" + filename
    writeTofile(sub[2], subPath)
    try:
        zObject = ZipFile(subPath, "r")
        zObject.extractall(foldername)
        zObject.close()
        os.remove(subPath)
    except zipfile.BadZipFile:
        print("Bad zip file")
    except:
        print("other error")
    finally:
        zObject.close()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    db = sqlite3worker.SQLite3Worker('C:\\Users\\u\\Downloads\\opensubtitles.org.Actually.Open.Edition.2022.07.25\\opensubs.db')  # "FILEPATH" | ":memory:"

    with open("moviesOnlyNoDupes.csv", 'r', encoding="utf8") as csvfile:
        datareader = csv.reader(csvfile)

        for row in datareader:
            get_and_unzip(db, row[0])




# See PyCharm help at https://www.jetbrains.com/help/pycharm/