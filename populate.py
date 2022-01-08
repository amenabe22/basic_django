import csv
import json
import requests
from pprint import pprint
from typing import ValuesView


def save_town(twn):
    url = "http://127.0.0.1:8000/add/"
    res = requests.post(url, twn)
    print(res.status_code)
    # print(res.content)


def add_towns():
    with open("uk-towns/towns.json") as file:
        j_file = json.load(file)
        for town in j_file:
            print("[+] Adding",town["county"])
            save_town(town)
        # print(len(j_file),"bruh")


def main():
    add_towns()
    # url = "http://127.0.0.1:8000/add/"
    # res = requests.post(url, data={"message": "Here"})
    # print(res.status_code)
    # print(res.content)


if __name__ == "__main__":
    main()
