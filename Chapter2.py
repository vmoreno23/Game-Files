def Chapter_2():
    choices = ["1", "2", "3"]

    print("After sneaking through your block, you find the local market where resources may be in abundance. The undead monsters you tried to avoid on your street fill the neighborhood")

    user_input = ""

    print("The front door of the market is boarded up, but there is a side entrance. There are screams heard throughout the neighborhood, but one scream sounds eerily close by. A woman is trapped inside her vehicle as an undead mob try to pry doors open. She's a lost cause")

    while user_input not in choices:
        print("""
        Options:
        1. Attempt to save the woman
        2. Enter the market through side entrance
        3. Break window to enter market
        """)

        if user_input == "1":
            print("You use your knife to fend off the undead, but you are overrun and become the dead’s next meal")
            Chapter_4()
        elif user_input == "2":
            print("Door is locked")
            if crowbar: #crow was found from chapter 1
                print("You break in through side door and resources are gathered, hearing a loud bang you witness the woman from the car scream and run into the window of the market shattering it as she gets devoured. The noise attracts unwanted attention to you")
            else:
                Chapter_3()
        elif user_input == "3":
            print("Resources are gathered, but the noise attracted unwanted attention")
            Chapter_3()
        else:
            print("Enter a valid option")
