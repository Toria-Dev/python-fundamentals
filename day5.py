#countdown timer
print("   Countdown   ")
count = 10
while count >= 0:
    print(count)
    count = count - 1 
print("Blast Off! 🚀")

#password checker
correct_username = "Toria"
correct_password = "Python 2026"
attempts = 0
max_attempts = 3
print ("   Secure Login   ")
while attempts < max_attempts:
    username = input ("username: ")
    password = input ("Enter password: ")
    attempts += 1

    if username == correct_username and password == correct_password:
        print("Access granted! Welcome", correct_username )
        break 
    else: 
        remaining = max_attempts - attempts 
        if remaining > 0:
            print ("Wrong Credentials.", remaining, "attempts remaining.")
        else:
            print("Too many failed attempts. Account Locked).")
