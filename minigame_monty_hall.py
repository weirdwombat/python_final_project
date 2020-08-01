user_input = input("Do you want Door 1, 2, or 3: ")

def door_selection():
    if user_input != (1,2,3):
        assert ValueError
    else:
