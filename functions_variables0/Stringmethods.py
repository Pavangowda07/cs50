# name = input("what is your name ?")
# name = name.strip().title()   #removing the white spaces and captilizing the words first letter

# or
name = input("What is your name ").strip().title()

#split the first name and greet them only using there first name 
first, last = name.split(" ")

print(f"The name is {first}")

