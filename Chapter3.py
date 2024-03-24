def Chapter_3():
    choices = ["1", "2", "3"]

    print("You run for your life out of the market as the undead chase you")
    print("")
    print("You quickly analyze your options of escape")

    print("""
    Options:
    1. Fight off the undead
    2. Attempt escape through market side entrance
    3. Exit through the broken window
    """)

    user_input = input("")

    while choices:
        if user_input == "1":
            print("You fend off the undead and find a bite mark on your shoulder and forearm. You are taken over by the virus")
            Chapter_4()
        elif user_input == "2":
            print("The door is jammed; you get swarmed by the undead and become lunch")
            Chapter_4()
        elif user_input == "3":
            print("You escape with slight cuts bruises, but you manage to escape")
            Chapter_5()
        else:
            print("Enter a valid option")
            user_input = input("")

