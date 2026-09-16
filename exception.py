try:
    number = int(input("Enter the number "))
    print( 10/number)
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("can not divide by 0")
finally:
    print("Finished")