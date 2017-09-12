ctr = 1
while ctr != -1:
    try:
        print(ctr)  
        ctr=int(input("Enter the number:"))
    except NameError:
        print("Kindly Enter a number:")
    except ValueError:
        print("You need to use a number Idiot!!")
    else:
        print("Try me once more")
    finally:
        print("Its ok we are done for the day")
