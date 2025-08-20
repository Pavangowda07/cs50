def main():
    x = get_int("What is the value of x?: ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
            # return x
        except:
            # print("Please give me an integer! ")
            pass
        
            

main()

