import csv
import json
import os
import pyperclip

# This converts the raw .csv file from takeout.google.com into a json format and write it to subscriptions.json
def convertToJson():    
    csvFile = "subscriptions.csv"
    jsonFile = "subscriptions.json"

    if os.path.exists(jsonFile): return
    
    else:
        data = []

        with open(csvFile) as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)

        jsonData = json.dumps(data)

        with open(jsonFile, 'w') as f:
            f.write(jsonData)
        
convertToJson()

# Here we verify we are getting an integer as an input when setting our start and end indices
def getValidIntInput(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Input must be an integer")

# This function parses the json input subscriptions.json and outputs youtube channel URLs in a given range
def parseSubs():
    with open("subscriptions.json", "r") as f:
        json_str = f.read()

    subNestedDictList = json.loads(json_str)

    startIndex = getValidIntInput(
        "Please Enter the start index of the URLs you would like: ")
    endIndex = getValidIntInput(
        "Please Enter the end index of the URLs you would like: ")
    urlList = []
    for i in range(startIndex, endIndex+1):
        if i == endIndex:
            break
        try:
            for key, value in subNestedDictList[i].items():
                if key == "Channel Url":
                    urlList.append(value)                    
        except IndexError:
            print(
                f"Unable to parse {endIndex - startIndex} URLs, was only able to parse {i - startIndex} URLs")
            break
    clipboardString = '\n'.join(urlList)
    # print(clipboardString)
    pyperclip.copy(clipboardString)
    pyperclip.paste()
    print(f"Successfully copied {i-startIndex} URLs to clipboard!")

parseSubs()
