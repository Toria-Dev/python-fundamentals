# Combining Functions & Dictionaries
# Project Data
project = {
    "Name": "Website Redesign",
    "Owner": "Toria",
    "Budget": 5000,
    "Spent": 3800,
    "Tasks": ["Design", "Development", "Testing", "Review", "Launch"],
    "Complete": ["Design", "Development"],
    "Status": "Active"
}
#   Summarise Project Function
def summarise_project(project_dict):
    Name = project_dict ["Name"]
    Owner = project_dict ["Owner"]
    Budget = project_dict ["Budget"]
    Spent = project_dict ["Spent"]
    Tasks = project_dict ["Tasks"]
    Complete = project_dict ["Complete"]
    Status = project_dict ["Status"]

    remaining = Budget - Spent
    Percent_Spent = (Spent / Budget) * 100
    Tasks_Total = len(Tasks)
    Tasks_Done = len(Complete)
    Tasks_Left = Tasks_Total - Tasks_Done
    Percent_Done = (Tasks_Done / Tasks_Total) * 100

    if Spent > Budget:
        Budget_Status = " ⛔️ OVER BUDGET"
    elif Percent_Spent >= 80:
        Budget_Status = " 🟡 WARNING"
    else: 
        Budget_Status = " 🟢 ON TRACK"

    print("=" * 35)
    print("   PROJECT SUMMARY REPORT"   )
    print("=" * 35)
    print("Name:   ", Name)
    print("Owner:   ", Owner)
    print("Status:   ", Status)
    print("-" * 35)
    print("Budget:   GHS", Budget)
    print("Spent:   GHS", Spent)
    print("Remaining:   ", remaining)
    print("Spent:   ", int(Percent_Spent), "%")
    print("Budget Status:   ", Budget_Status)
    print("-" * 35)
    print("Total Task:   ", Tasks_Total)
    print("Completed:   ", Tasks_Done)
    print("Remaining:   ", Tasks_Left)
    print("Progress:   ", int(Percent_Done), " % done")
    print("-" * 35)
    print("Completed Tasks:")
    for task in Complete:
        print("  ✓", task)
    print("Pending Tasks:")
    for task in Tasks:
        if task not in Complete:
            print("  ->", task)
    print ("=" * 35)
    print("Recommendation:")
    if Spent > Budget and Tasks_Left > 0:
     print ( " OVER BUDGET with Tasks Remaining - Escalate Immediately")
    elif Tasks_Left == 0 and Spent <= Budget:
     print("  All Tasks Done and Within Budget - Ready to Close")
    elif Percent_Spent >= 80 and Tasks_Left > 2: 
     print (" Budget Running Low with Tasks Remaining - Review Resourcing")
    else:
     print(" Project is Healthy - Keep Going")
print("=" * 35)
summarise_project(project)

# Testing with different Projects
Project_B ={
    "Name": "Mobile App Launch",
    "Owner": "Dom",
    "Budget": 8000,
    "Spent": 8500,
    "Tasks": ["Planning", "Design", "Build", "Testing", "Launch"],
    "Complete": ["Planning", "Design", "Build", "Testing" ],
    "Status": "Almost"
}

Project_C = {
    "Name": "Data Migration",
    "Owner": "Edudzi",
    "Budget": 10000,
    "Spent": 9999,
    "Tasks": ["Audit", "Clean", "Migrate", "Verify"],
    "Complete": ["Design", "Development"],
    "Status": "Active"
}
print("")
summarise_project(Project_B)
print("") 
summarise_project(Project_C)

