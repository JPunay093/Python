a = 1
try:
    b = float(input("Please enter a number to divide a "))
    a = a/b
    print(f"Success a= {a}")
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
    /workspaces/Python/Virtual web