#   Project Dictionary
project = {
    "Name":   "Website Redesign",
    "Budget": 5000,
    "Spent": 3800,
    "Status": "Active",
    "Owner": "Toria"
}
#   Accessing Values
print("   Project Details   ")
print("Name: ", project ["Name"])
print("Budget: ", project ["Budget"])
print ("Spent: ", project ["Spent"])
print("Status: ", project ["Status"])
print("Owner: ", project ["Owner"])
#   using .get(), .key(), .values()
print("Deadline:", project.get ("Deadline", "Not yet set"))
print("Owner: ", project.get ("Owner", "Unassigned"))
print("")
print(project.keys())
print("")
print(project.values())
#   Looping
print("")
print("   Full Project   ")
for key, value in project.items():
    print(key, ":", value)
#   Adding & Updating
print("")
print("   Update Project   ")
project["Deadline"] = "June 2026"
project ["Status"] = "In Review"
print("Deadline Added:", project["Deadline"])
print("Status Update:", project ["Status"])
#   Calculations from Dict Values
print("")
print("   Budget Summary   ")
remaining = project["Budget"] - project["Spent"]
percent_spent = (project["Spent"] / project["Budget"]) * 100
print("Remaining: GHS", remaining)
print("Percent Spent:", int(percent_spent), "%")

#   Challenge
project= {
    "Name":   "Website Redesign",
    "Budget": 5000,
    "Spent": 6200,
    "Owner": "Toria"
},
{
    "Name":   "Mobile App Launch", 
    "Budget": 8000,
    "Spent": 4500,
    "Owner": "Marlize"
 },
{   "Name":   "Data Migration", 
    "Budget": 8000,
    "Spent": 4500,
    "Owner": "Dom"
}
print("   Portfolio Status Report   ")
for project in project:
    Name = project ["Name"]
    Budget = project["Budget"]
    Spent = project["Spent"]
    Owner = project ["Owner"]
    Remaining = Budget - Spent 

    if Spent > Budget:
        Status = "OVER BUDGET"
    elif (Spent / Budget) * 100 >= 80:
        Status = "WARNING"
    else:
        Status = "ON TRACK"
    print("")
    print("Project:", Name)
    print("Owner:", Owner)
    print("Status:", Status)
    print("Remaining", Remaining )


