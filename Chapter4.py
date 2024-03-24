def Chapter_4():
    choices = ["1", "2", "3"]

    print("Hours after becoming a meal for the undead, you gain control of your body once more. An unquenchable sense of hunger fogs your thoughts leaving you unable to speak")

    user_input = ""

    print("Your decomposing body is all you have left. Feeding on whatever you find. You make your way into the city")

    while user_input not in choices:
        print("""
        Options:
        1. Attack a group of 5 survivors
        2. Attack a lone teenage girl hiding
        3. Attack a military convoy heading to the city
        """)

        if user_input == "1":
            print("Assisted by a mob of undead you feast on 2 survivors, but the rest of the survivors avenge their fallen. They take out the mob including yourself")
            quit()
        elif user_input == "2":
            print("You underestimate the skills and survivability of the teenage girl, she puts an end to your suffering")
            quit()
        elif user_input == "3":
            print("You stood no chance against the power of the military")
            quit()
        else:
            print("Enter a valid option")
