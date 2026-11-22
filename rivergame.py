# Dictionaries for starting state of each side of river
north = {"farmer": True, "fox": True, "chicken": True, "seeds": True}
south = {}
accessible_items = {"farmer": True, "fox": True,
                    "chicken": True, "seeds": True, "boat": "north"}


def user_interface(north, south, accessible_items):
    '''
    Shows current game state to the user
    Checks current game state to check for win.
    Calls move function when there is no win. 
    ARGUMENTS: Dictionaries containing items accessible and on each side.
    '''
    # Show current game state
    print(" ")
    print("NORTH: " + f" ". join(north.keys()))
    print("~~~~~~~~~~~~~~RIVER~~~~~~~~~~~~~~")
    print("SOUTH: " + f" ".join(south.keys()))
    print(" ")
    print(f"The boat is on the {accessible_items["boat"]} side. ")
    # Check for win
    if len(south) < 4:
        item = input("What would you like to move?")
        move(item)
    else:
        print("Congratulations you have won!!!!")


def move(item):
    '''
    Function assesses whether a move is possible
    Moves the object and/or the farmer 
    ARGUMENTS: 1 item to be moved
    '''
    # Check item is moveable
    if item not in accessible_items or item == "boat":
        print("You cannot take that item")
        user_interface(north, south, accessible_items)

    if accessible_items["boat"] == "north":  # Check if boat is north
        if item in north:  # Check if item is north
            south[item] = north.pop(item)  # Move item south
            accessible_items["boat"] = "south"  # Move boat south
            if item != "farmer":
                # Moves farmer with the item for non solo trips
                south["farmer"] = north.pop("farmer")
        else:
            # User error message
            print("Please select an item to move on the north side")
            # Request valid input
            user_interface(north, south, accessible_items)
    else:  # Check if boat is south
        if item in south:  # Check if item is south
            north[item] = south.pop(item)  # Move item north
            accessible_items["boat"] = "north"  # Move boat north
            if item != "farmer":
                # Moves farmer with the item for non solo trips
                north["farmer"] = south.pop("farmer")
        else:
            # User error message
            print("Please select an item to move on the south side")
            # Request valid input
            user_interface(north, south, accessible_items)
    loss_checker(north, south)  # Checks for loss after each item is moved


def loss_checker(north, south):
    '''
    Function checks for loss state and outputs loss statement. 
    Quits code after and tells user to re-run. 
    ARGUMENTS: 2 dictionaries; 1 for each side of the river. 
    '''
    for side in [north, south]:  # Checks each side
        if "farmer" not in side:  # Checks farmer location
            # Check if Fox ate Chicken
            if "fox" in side and "chicken" in side:
                print("NOOOOO! The Fox ate the Seeds!")
                print("Please re-run the code to try again")
                quit()
            # Check if Chicken ate Seeds
            if "chicken" in side and "seeds" in side:
                print("NOOOOO! The Chicken ate the Seeds!")
                print("Please re-run the code to try again")
                quit()
    user_interface(north, south, accessible_items)


user_interface(north, south, accessible_items)
