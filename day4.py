print("___ Numbers 1 to 10___")
for number in range (1,11):
    print(number)
print("---Even Numbers---")
for number in range (1,11):
    if number % 2 == 0:
        print(number)
# list of project names
projects = [ 
    "Website Redesign"
    "Mobile App Launch"
    "Data Migration"
    "Brand Refresh"
    "CRM Integration"
]
# loop through and print each one
print("---Active Projects---")
for project in projects:
    print("Projects:", projects)

projects = [
    ["Website Redesign", "over budget"],
    ["Mobile App Launch", "on target"],
    ["Data Migration", "under budget"],
    ["Brand Refresh", "on target"],
    ["CRM Integration", "over budget"]
]
print("   Print Status Report   ")
for project in projects:
    name = project [0]
    status = project [1]

    if status == "over budget":
        print(name, "-> ALERT: Over Budget!")
    elif status == "on target":
        print(name, "-> On Track")
    else: 
        print(name, "-> Under Budget - Check Resourcing ")

    print("   Numbers 1 to 20  ")
    for number in range (2,16):
        print(number)
    print("   Odd Numbers   ")
    for number in range(2,16):
        if number % 2 != 0:
            print (number)