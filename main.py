while True:
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print("This is an even number")
    else:
        print("This is an odd number")
    cont = input("Do you want to continue? ")
    while cont .lower() not in ("yes", "no"):
        cont = input("Do you want to continue? ")
    if cont == "no":
        print("Break")
        break
