def Chapter_1():
    choices = ["1", "2", "3", "4"]

    print("2 days have passed since the unknown contagious virus infected the first human and widespread chaos amongst neighboring cities. The virus turned the living into the undead. Time to find more supplies")

    user_input = ""
    
    print("You wake up in your home where you are barricaded from the outdoor threats. There are no survivors on your street. You remember the neighbor gave you keys to his house before he left, but no promising there will be supplies")
    
    while user_input not in choices:
        print("""
        Options:
        1. Check current supplies
        2. Check the news media
        3. Leave your home to search neighbor’s home
        4. Leave home to search for resources
        """)

        if user_input == "1":
            print("You have little food and water, a pocket knife, and a small backpack")
        elif user_input == "2":
            print("You are informed that the west coast is overtaken by the virus and all survivors are order to take shelter where they can. The military is sending teams to round up survivors")
        elif user_input == "3":
            print("You find a crowbar")
            global crowbar #User finds crowbar, final program will announce crowbar = False
            Chapter_2()
        elif user_input == "4":
            Chapter_2()
        else:
            print("Enter a valid option")
