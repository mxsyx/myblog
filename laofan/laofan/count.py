#!/opt/Anaconda/bin/python3.6
import os
import json

def calculate_item_numbers():
    print("各个文件内的URL数量如下：\n")
    file_names = os.listdir("tmp/")
    for file_name in file_names:
        if os.path.isfile("tmp/%s" % file_name):
            with open("tmp/%s" % file_name) as file:
                print("%s : %s\n" % (file_name, str( len(json.load(file)))))


if __name__ == "__main__":
    calculate_item_numbers()
