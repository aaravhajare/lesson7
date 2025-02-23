medical = input("did you had a medical problem ? yes or no")

atten = int(input("what is your attendence"))

if medical == "yes" :
    print("you are allowed")

else :
    if atten >= 75 :
        print("you are allowed")

    else :
        print("you are not allowed")
            