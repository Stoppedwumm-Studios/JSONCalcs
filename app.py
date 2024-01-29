import json
import os

filename = "calcs.jsoncalcs"

import sys

if len(sys.argv) == 1:
    maybefilename = input("Filename (leave empty for standard): ")

    if maybefilename == "":
        print("Using normal filename")
    else:
        filename = str(maybefilename) + ".jsoncalcs"
else:
    if sys.argv[1] == "":
        print("Opened without file via batch")
    else:
        filename = sys.argv[1]
        print(sys.argv[1])
        print("[INFO] Opened file opened with argument/batch file")
    
    
def LoadFile():
    if os.path.exists(filename):
        with open(filename, 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)
    else:
        json_object = {}
    
    return json_object

dictionary = LoadFile()

def AskMethod():
    print("Methods:")
    print("a) Save JSON (Save this document)")
    print("b) Write new (Write new calc)")
    print("c) Use saved calc")
    print("d) List calcs")
    method = input("What do you want to do (type letter, press Ctrl/Strg + C to cancel)? ")
    
    return method

def SaveFile():
 
    # Serializing json
    json_object = json.dumps(dictionary, indent=4)
 
    # Writing to sample.json
    with open(filename, "w") as outfile:
        json.dump(dictionary, outfile)

def SaveCalc(calc, name, varia):
    info = {
        "calculation": calc,
        "name": name,
        "vars": varia
    }
    dictionary[name] = info
    SaveFile()

def LoadCalc(name, variables):
    calculationStr = dictionary[name]["calculation"]
    exec(variables + "\nprint(" + str(calculationStr) + ")")


while True:
    method = AskMethod()

    if method == "a":
        SaveFile()
        print("DONE")
        print("======================")
    elif method == "b":
        name = input("Name of new calc: ")
        Calc = input("The new calc: ")
        variables = []
        while True:
            lastInput = input("Enter Variable or 'done' to close this prompt: ")
            if lastInput == "done":
                break
            else:
                variables.insert(1, lastInput)
        SaveCalc(Calc, name, variables)
    elif method == "d":
        for listinfo in dictionary:
            print("Name: " + dictionary[listinfo]["name"])
            print("Calc: " + dictionary[listinfo]["calculation"])
            print("=====================")
    else:
        name = input("Name of the calc: ")
        command = ""
        variables = dictionary[name]["vars"]
        for x in variables:
            lastInput = input("Variable " + x + "? ")
            command = command + x + " = " + lastInput + "\n"
        
        
        print("Result is ")
        LoadCalc(str(name), command)
