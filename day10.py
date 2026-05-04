tasks = ["Design", "Testing", "Planning", "Review", "Deployment"] 
#            0          1          2          3           4
#Indexing
print(tasks[0])
print(tasks [1])
print(tasks [4])
print(tasks [-1])
#Slicing
print(tasks[0:3])
print(tasks[1:4])
print(tasks[:2])
print(tasks[3:])
#Append
tasks = ["Design", "Testing", "Planning"]
tasks.append("Review")
print(tasks)
# Remove
tasks = ["Design", "Testing", "Planning", "Review",]
tasks.remove ("Testing")
print(tasks)
#Sort
tasks = ["Design", "Testing", "Planning", "Review", "Deployment"] 
tasks.sort()
print(tasks)

tasks = ["Design", "Testing", "Planning", "Review", "Deployment"] 
print("  Indexing   ")
print("First tasks:", tasks [0])
print("Second task:", tasks [1])
print("Last task:", tasks [-1] )
print("Second task", tasks [-2])

print("  Slicing   ")
print("First 3 tasks:", tasks[0:3])
print("Last 2 tasks:", tasks [3:])
print("Middle tasks:", tasks [1:4])

print("  Sorted Alphabetically   ")
tasks.sort()
print("Full Sorted List:", tasks)
print("First task after sort:", tasks [0])
print ("Last task after sort:", tasks [-1])

print("  Adding a task    ")
tasks.append ("Sign off")
print("After adding Sign Off:", tasks)
print ("Total tasks:", len (tasks))

print("  Removing a task   ")
tasks.remove ("Testing")
print("After removing Testing:", tasks)
print("Total Tasks:", len(tasks))
