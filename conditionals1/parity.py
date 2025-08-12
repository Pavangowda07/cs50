def main():
    x = int(input("What is the X value ? "))
    if is_even(x):
        print("Even")
    else :
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return (n % 2 == 0)

        # return True if n % 2 == 0 else False

    #     return True
    # else :
    #     return False

main()
