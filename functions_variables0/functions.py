#defining the function using def keyword

# def hello (to="world"):
#     print("Hello ,",to)

# name = input("What is your name ? ")
# hello(name)

# hello()

def main():
    numb = int(input("what is the number? "))
    print("the squared number is :", square(numb))
def square(n):
    return n * n

main()