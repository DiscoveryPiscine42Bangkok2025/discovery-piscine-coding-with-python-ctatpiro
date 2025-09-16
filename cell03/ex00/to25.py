x = int(input("Enter a number less than 25\n"))   
if x<25:
    i=x
    while i==25:
        print(f"Inside the loop, my variable is {i}")
        i+=1
else:
    print("Error")
