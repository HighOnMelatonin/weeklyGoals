## Weekly Goals
import json

def makeJson(filename: str) -> None:
    filepath = 'goals/' + filename + ".json"

    try:
        file = open(filepath, 'r+')
    
    except FileNotFoundError:
        file = open(filepath, "r+")
        json.dumps('{}',)
    
    finally:
        file.close()

    return None

def getJson(filename: str) -> dict:
    filepath = 'goals/' + filename + '.json'
    file = open(filepath, 'r+')
    data = json.load(file)
    file.close()
    return data

def seeGoals(filename: str, week: str) -> None:
    data = getJson(filename)
    i = 1
    try:
        for item in data[week]:
            print(f"{i}. {item}")
            i += 1

    except KeyError:
        print("Week not added yet, use setGoal to add")
    
    return None

def setGoal(filename: str, week: str, goal: str) -> None:
    filepath = 'goals/' + filename + '.json'
    file = open(filepath, 'r+')
    data = getJson(filename)

    try:
        data[week] += [goal]

    except KeyError:
        data[week] = [goal]
    
    json.dump(data, file)
    file.close()
    return None

def clearGoal(filename: str, week: str, index: int) -> None:
    filepath = 'goals/' + filename + '.json'
    file = open(filepath, 'r+')
    data = getJson(filename)

    try:
        goal = data[week][index]
        data[week] = data[week].remove(goal)
        print("Removed", goal)

    except KeyError:
        print("Invalid goal")

    json.dump(data, file, indent=4)
    file.close()

    return None


def main():
    menu = """
    Functions: 
    1. See goals
    2. Set goals
    3. Clear goal

    'quit' to exit program
    """
    filename = str(input("Enter a filename (ie. term1): "))
    data = getJson(filename)

    print(menu)
    entry = str(input("Selection: "))
    while entry != "quit":
        week = str(input("Enter week number (week10): "))
        if entry == "1":
            seeGoals(filename, week)

        if entry == "2":
            goal = str(input("Goal: "))
            setGoal(filename, week, goal)
            print("Added", goal)

        if entry == "3":
            seeGoals(filename, week)
            goal = str(input("Goal to remove: "))
            if not goal.isdigit():
                i = 0
                while i < len(data[week]) and data[week][i] != goal:
                    i += 1

                index = i

            else:
                index = int(goal) - 1

            clearGoal(filename, week, index)

        print(menu)
        entry = str(input("Selection: "))


main()
