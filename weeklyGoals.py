## Weekly Goals
import json

def makeJson(filename) -> dict:
    filepath = 'goals' + filename + ".json"
    try:
        file = open(filepath, 'r+')
    
    except FileNotFoundError:
        file = open(filepath, "w")
    
    finally:
        readable = json.load(file)
        file.close()

    return readable

def getJson():
    pass

def seeGoals():
    pass

def setGoals():
    pass

def clearGoal():
    pass


def main():
    pass

main()
makeJson('term1')
