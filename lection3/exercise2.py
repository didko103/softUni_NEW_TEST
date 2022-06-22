day = input()

if day in ["Monday", "Thursday", "Wednesday", "Tuesday", "Friday"]:
    print("Working day")
elif day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Error")