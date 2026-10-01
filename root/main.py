talked_to_goblin = False
relationship_mended = False
code = "9149"

areas = ["hallway1", "living_room", "bathroom", "room1", "room2", "room3", "stairwell", "hallway2", "room4", "room5", "painting"]
area = areas[0]
user_input = None

def check_user_input(num_of_options: int, input_from_user: str) -> bool:
    """
    :param num_of_options: The number of options
    :param input_from_user: What the user inputted.
    :return: Whether or not the input passed or not.
    """
    

#You might notice my programs have a theme.
print("""
Welcome to the Greatest Library Ever!

There are two floors, with 8 rooms, 2 hallways, and one stairwell. 
Your task is to solve the mystery. The man in the living room can tell you what the mystery is and give you hints.

""")
while True:
    if area == areas[0]:
        print("""
        Description of room
        """)
        user_input = input()
        if check_user_input(5, user_input)
            #Go into that state
    



