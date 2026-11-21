print("Smart school day planner. \n")
print("Answer 3 questions and I will plan your day.\n")

day = input("Enter the day (Monday - Sunday) : ").strip().lower()
weather =  input("enter the weather condition. (sunny/rainy/cloudy) :  ").strip().lower()
homework = input("Have you done your homeowork? (yes/no) : ").strip().lower()

print("\nPlan for the day : ", day)

if day in ("saturday, sunday"):
    print("This is a weekend, Enjoy your free time !")
elif day == "monday":
    print("This is the first day of school, plan your weekly planner")
elif day == "friday":
    print("This is the last day of school, return the library books today!")
elif day in ("tuesday, wednesday, thursday"):
    print("This is a regular school day")
else:
    print("day not recognised, please check the spelling")

if weather == "sunny" and homework == "yes":
    print("good job!, your homework is done, you can go out to play.")

if weather == "cloudy" or weather == "rainy":
    print("pack your umbrella, it may rain outside.")

if not homework == "yes":
    print("Finish your homework before going outside.")

print("\nbest plan:\n")

if weather == "rainy" and homework != "yes":
    print("stay inside, finish your homeowrk and watch your favorite show.")
elif homework == "yes" and weather == "sunny" and not day in("saturday, sunday"):
    print("you are all set for a great school day")
elif day in ("saturday, sunday") and weather == "sunny":
    print("perfect weekend weather, Go out and have fun!")
else:
    print("take it one step at a time, you have got this")
print("\n Plan comelete, have a wonderful day!")