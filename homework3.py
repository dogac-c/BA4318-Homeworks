x = input('What is your age? ')
if int(x) > 19:
    print("adult")
else:
    if int(x) > 10:
        print("adolescent")
    elif int(x) <= 10 and int(x) > 1:
        print("children")
    else:
        print("infant")