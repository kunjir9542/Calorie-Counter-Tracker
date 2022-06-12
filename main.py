global caloriesAte
global goal
global foodList
caloriesAte = 0
foodList = []


print("--------------------------------------------------------------------")



def mainMenu():
    print("--------------------------------------------------------------------")
    global caloriesAte
    print("The foods you ate so far are")
    for x in foodList:
        print(x)
    choice = input("Would you like to add food you ate,edit your goal, or clear your progress? (A/E/C)")
    if choice == "A":
        addFood()
    if choice == "E":
        editGoal()
    if choice == "C":
        caloriesAte = 0
        foodList.clear()
        print("Cleared Progress")
        mainMenu()

def addFood():
    global foodList
    global caloriesAte
    print("--------------------------------------------------------------------")
    foodNameAdded = input("Enter the type of food you ate")
    if (foodNameAdded.isnumeric()):
        print("Please enter a word/string")
        addFood()
    else:
        caloriesAdded = input("Enter the number of calories the food add")
    if (caloriesAdded.isnumeric()):
        print("Successfully added food")
        foodList.append(foodNameAdded + ": " + caloriesAdded)
        caloriesAte += int(caloriesAdded)
        checkGoal()
        mainMenu()
    else:
        print("Please enter a number")
        addFood()


def editGoal():
    print("--------------------------------------------------------------------")
    global goal
    goal = input("Please set a goal for calories to eat for the day")
    print("Goal Set. You can always edit this later")
    mainMenu()

def checkGoal():
    global caloriesAte
    if caloriesAte >= int(goal):
        print("Goal Reached!!")
        mainMenu()
    else:
        print("You are " + str(caloriesAte) + " / " + goal + " toward your goal")

editGoal()
mainMenu()
