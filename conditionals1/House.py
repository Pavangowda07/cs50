name = input("Enter your name ? ")

# if name == "Pavan":s
#     print("Red House!")
# elif name == "Bunty" or "Hemu" or "Suraj":
#     print("Green House!")

# else:
#     print('who?')

# or using match function 
match name :
    case "Pavan":
        print("Red House !")
    case "Bunty" | "Hemu" | "Suraj":
        print("Green House !")
    case _:
        print("who ?")