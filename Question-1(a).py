def myfunction(x):
    if len(x) > 2:
        delete_string = x[:-2]
        string_reverse = delete_string[::-1]
        print(string_reverse)
    else:
        print("String lenth is not greater than 2 ")

x=str(input("Enter a word : "))
myfunction(x)