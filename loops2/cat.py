# while loop
# i = 3 
# while i != 0:
#     print("meow")
#     i -= 1

# for loop with list 
# for i in [1, 2, 3]:
#     print("meow")


# for loop with range 
# for i in range(3):
#     print("meow")
#     or
# for _ in range(3):
#     print("meow")

# or 
# print("meow\n" * 3, end="")

# while True:
#     n = int(input("What is n?"))
#     if n > 0 :
#         break

# for _ in range(n):
#     print("meow")


def main():
    number = positive_only()
    meow(number)

def positive_only():
    while True:
        n = int(input("what is n?"))
        if n> 0 :
            break
    return n

def meow(num):
  for _ in range(num):
      print("meow")

main()