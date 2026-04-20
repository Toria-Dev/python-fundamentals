#Project Budget Checker
project_name = "Website Redesign" 
total_budget = 5000 
amount_spent = 4800
#calculate how much is remaining 
remaining = total_budget - amount_spent
# check the budget status
if amount_spent> total_budget:
    print("BUDGET ALERT")
    print("Project:", project_name)
    print("Status: OVER BUDGET")
    print("You have overspent by $", amount_spent - total_budget)
elif amount_spent == total_budget:
    print("BUDGET STATUS")
    print("Project:", project_name)
    print("Status: EXACTLY ON TARGET")
    print("You have $0 remaining - no room for error")
else:
    print("BUDGET STATUS")
    print("Project:", project_name)
    print("Status: UNDER BUDGET")
    print("Balance:$", remaining, "remaining")
print("__________")
print("Total Budget:$",total_budget)
print("Amount Spent:$",amount_spent)

