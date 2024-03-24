def Chapter_5():
    choices = ["1", "2", "3"]

    print("After escaping the market, you need to find shelter. There are flares shot from the city. You figure the city is where the military would start saving survivors")
    print("")
    print("As daylight starts to fade, you think of ways to get closer to the city. You need to quickly get inside the city before you miss the military rescue. No time to waste")

    print("""
    Options:
    1. Head to a nearby car dealership
    2. Head to your friend's house
    3. Head to a nearby gas station
    """)

    user_input = input("")

    while choices:
        if user_input == "1":
            print("You find keys to a sports car with enough fuel to reach the city on time. The military rescues you and other survivors")
            quit()
        elif user_input == "2":
            print("You find your friend alive at his home. He tells you that you're welcome to stay until help arrives, he does not tell you he's received a bite from the undead, you unexpectedly get bitten by your friend")
            Chapter_4()
        elif user_input == "3":
            print("You find the remains of the gas station clerk and search the employee room. His car keys are still hanging. You take his car to reach the city and find the military pickup zone. They rescue you and other survivors")
            quit()
        else:
            print("Enter a valid option")
            user_input = input("")
