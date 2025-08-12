# for _ in range(3):
#     print("#", end="")


def main(): 
    brick = int(input("What is the square of block?"))
    square(brick)

def square(n):
    for i in range(n):
        for j in range(n):
            print("X", end="")
        print()


main()

    



