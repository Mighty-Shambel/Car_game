try:
    Age=int(input("Age: "))
    div=2000/Age
    print(div)
except ValueError:
    print("The value you enterd is wrong!")
except ZeroDivisionError:
    print("Division By zero isn't possible!")

