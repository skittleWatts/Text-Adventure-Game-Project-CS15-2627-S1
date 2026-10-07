talked_to_goblin = False
relationship_mended = False
stairwell_opened = False
code = "9149"

areas = ["hallway1", "living_room", "bathroom", "room1", "room2", "room3", "stairwell", "hallway2", "room4", "room5", "painting"]
area = areas[0]
options = ["1", "2", "3", "4"]

def hallway1() -> int:
    """
    Runs the code required for the area of the first hallway.
    :return: Value of the new area.
    """
    print("""
    You are in the downstairs hallway.
    
    
    """)
    while True:
        user_input = input()
        if user_input in options[0:2]:
            if user_input == "1":
                area = areas[1]
                break
        else:
            print("Please enter a valid input! ")
    return area

def living_room() -> int:
    """
    Runs the code required for the area of the living room.
    :return: Value of the new area.
    """
    print("""
    Description of room
    """)
    while True:
        user_input = input()
        if user_input in options[0:2]:
            if user_input == "1":
                area = areas[1]
                break
        else:
            print("Please enter a valid input! ")
    return area

def bathroom() -> int:
    """
    Runs the code required for the area of the bathroom.
    :return: Value of the new area.
    """
    print("""
    Description of room
    """)
    while True:
        user_input = input()
        if user_input in options[0:2]:
            if user_input == "1":
                area = areas[1]
                break
        else:
            print("Please enter a valid input! ")
    return area

def room1() -> int:
    """
    Runs the code required for the area of the first room.
    :return: Value of the new area.
    """
    print("""
    Description of room
    """)
    while True:
        user_input = input()
        if user_input in options[0:2]:
            if user_input == "1":
                area = areas[1]
                break
        else:
            print("Please enter a valid input! ")
    return area

def room2() -> int:
    """
    Runs the code required for the area of the second room.
    :return: Value of the new area.
    """
    print("""
    Description of room
    """)
    while True:
        user_input = input()
        if user_input in options[0:2]:
            if user_input == "1":
                area = areas[1]
                break
        else:
            print("Please enter a valid input! ")
    return area

def room3() -> int:
    """
    Runs the code required for the area of the third room.
    :return: Value of the new area.
    """
    print("""
    Description of room
    """)
    while True:
        user_input = input()
        if user_input in options[0:2]:
            if user_input == "1":
                area = areas[1]
                break
        else:
            print("Please enter a valid input! ")
    return area

def stairwell() -> int:
    """
    Runs the code required for the area of the stairwell.
    :return: Value of the new area.
    """
    print("""
    Description of room
    """)
    while True:
        user_input = input()
        if user_input in options[0:2]:
            if user_input == "1":
                area = areas[1]
                break
        else:
            print("Please enter a valid input! ")
    return area

def hallway2() -> int:
    """
    Runs the code required for the area of the second hallway.
    :return: Value of the new area.
    """
    print("""
    Description of room
    """)
    while True:
        user_input = input()
        if user_input in options[0:2]:
            if user_input == "1":
                area = areas[1]
                break
        else:
            print("Please enter a valid input! ")
    return area

def room4() -> int:
    """
    Runs the code required for the area of the fourth room.
    :return: Value of the new area.
    """
    print("""
    Description of room
    """)
    while True:
        user_input = input()
        if user_input in options[0:2]:
            if user_input == "1":
                area = areas[1]
                break
        else:
            print("Please enter a valid input! ")
    return area

def room5() -> int:
    """
    Runs the code required for the area of the fifth room.
    :return: Value of the new area.
    """
    print("""
    Description of room
    """)
    while True:
        user_input = input()
        if user_input in options[0:2]:
            if user_input == "1":
                area = areas[1]
                break
        else:
            print("Please enter a valid input! ")
    return area

def painting() -> int:
    """
    Runs the code required for when you choose to inspect the painting.
    :return: Value of the new area.
    """
    print("""
    Description of room
    """)
    while True:
        user_input = input()
        if user_input in options[0:2]:
            if user_input == "1":
                area = areas[1]
                break
        else:
            print("Please enter a valid input! ")
    return area

#You might notice my programs have a theme.
print("""
Welcome to the Greatest Library Ever!

There are two floors, with 8 rooms, 2 hallways, and one stairwell. 
Your task is to solve the mystery. The man in the living room can tell you what the mystery is and give you hints.

""")

while True:
    if area == areas[0]:
        area = hallway1()

    elif area == areas[1]:
        area = living_room()

    elif area == areas[2]:
        area = bathroom()

    elif area == areas[3]:
        area = room1()

    elif area == areas[4]:
        area = room2()

    elif area == areas[5]:
        area = room3()

    elif area == areas[6]:
        area = stairwell()

    elif area == areas[7]:
        area = hallway2()

    elif area == areas[8]:
        area = room4()

    elif area == areas[9]:
        area = room5()

    elif area == areas[10]:
        area = painting()

    else:
        print("What the heck this isn't possible double check the code.")

