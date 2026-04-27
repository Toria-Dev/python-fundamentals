#   define the functions   #
def calculate_tax (price,rate):
    tax_amount = price * (rate/100)
    return tax_amount 
print("Tax on $200 at 10%: $", calculate_tax (200,10))
print("Tax on $500 at 15%: $", calculate_tax (500,15))
print("Tax on $1000 at 7%: $", calculate_tax (1000,7))
print("Tax on GHS8000 at 15%: GHS", calculate_tax (8000,15))
# Total price with tax 
def total_price (price,rate):
    tax=calculate_tax (price,rate)
    total = price + tax
    return total
print("")
print("   Total Price   ")
print("Total for GHS200 at 10%: GHS", total_price (200,10))
print("Total for GHS500 at 15%: GHS", total_price(500,15))
# Project Health Checker
def project_health(budget, spent, deadline_met):
    percent_spent = (spent/budget) * 100
    if deadline_met == False:
        return "RED - Deadline missed"
    elif percent_spent > 100:
        return "RED - Over Budget" 
    elif percent_spent >=80: 
        return "AMBER - Budget Warning"
    else:
        return "GREEN - On Track"
print("")
print("   Project Health Report   ")
print("Project A:", project_health (5000, 6200, True))
print("Project B:", project_health (5000, 4200, True))
print("Procject c:", project_health(5000, 2000, False))
print("Project D:", project_health (5000, 3800, True))

#My test 
def days_remaining (deadline, today):
    remaining = deadline-today
    return remaining
print("")
print ("   Days Remaining   ")
print("Project A:", days_remaining (90, 45), "days left" )
print("Project B:", days_remaining (30, 28), "days_left")
print("Project C:", days_remaining (60, 61), "days left - OVERDUE")


