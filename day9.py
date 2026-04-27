# Day 9 - Functions Practice
#   Function 1: is_over_budget    
def is_over_budget (spent, budget):
    if spent >= budget:
        return True
    else:
        return False
    
#   test it   
print("   Budget Checker   ")
print("Project A:", is_over_budget(6200, 5000))
print("Project B:", is_over_budget(3800, 5000))
print("Project C:", is_over_budget(5000, 5000))

# Function 2: Budget Status
def budget_status (spent, budget, project_name):
    if is_over_budget(spent, budget):
        print(project_name, "-> OVER BUDGET by GHS", spent - budget)
    else:
        print(project_name, "-> OnTrack. GHS", budget - spent, "remaining")
print("")
print("   Project Status   ")
budget_status (6200, 5000, "Website Redesign")
budget_status (3800, 5000, "Mobile App Launch")
budget_status (5000, 5000, "Data Migration")

#   Function 3
def greet_team (names):
    print("")
    print("   Family Greeting   ")
    for name in names:
        print ("Good night", name, "- let's all have a good sleep! 😴")
team = ["Toria", "Joy", "Aiden", "Marlize", "Mom"]
greet_team(team)
def greet_team (names):
    print("")
    print("   Family Greeting   ")
    print("Family size this year", len(names), "people")
    print("")
    for name in names:
        print ("Good night", name, "- let's all have a good sleep! 😴")
team = ["Toria", "Joy", "Aiden", "Marlize", "Mom"]
greet_team(team)