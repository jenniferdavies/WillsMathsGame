choice= input("Type m to practice timestables or press d to practice division or press a to practice addition or press s to practice subtraction  ")

if choice == 'm':

    #~THIS IS MULTIPLICATION

    timestabletext = input("What times table do want to practice? ")
    timestable=int(timestabletext) #this line of code turns the text answer into the number 

    for i in range(13): #this loops the code 12 times

        xtext = input(f"What is {timestable} * {i}?  ")
        x=int(xtext) #this line of code turns the text answer into the number 

        while x != timestable*i: #this means while x does NOT equal the correct answer

            print('wrong. Try again')
            xtext = input(f"What is {timestable} * {i}?  ")
            x=int(xtext) #this line of code turns the text answer into the number 

        print('correct')

elif choice == 'd':

    #~THIS IS DIVISON

    timestabletext = input("What division do want to practice? ")
    timestable=int(timestabletext) #this line of code turns the text answer into the number 

    for i in range(13): #this loops the code 13 times

        xtext = input(f"What is {timestable*i} / {timestable}?  ")
        x=int(xtext) #this line of code turns the text answer into the number 

        while x != i: #this means while x does NOT equal the correct answer

            print('wrong. Try again')
            xtext = input(f"What is {timestable*i} / {timestable}?  ")
            x=int(xtext) #this line of code turns the text answer into the number 

    print('correct')


elif choice =='a':
    
     #~THIS IS ADDITION

    choice2= input("Type 1 if you want to add up 1-digit numbers, 2 if you want to add up 2-digit numbers, or 3 if you want to add up 3-digit numbers ")

    import random

    if choice2 == '1':

        for i in range(1,12): #this loops the code 12 times from 1 to 12

            x = random.randint(1,9)
            y = random.randint(1,9)

            ztext = input(f"What is {x} + {y}?  ")
            z=int(ztext) #this line of code turns the text answer into the number

            while z != x+y: #this means while x does NOT equal the correct answer

                print('wrong. Try again')
                ztext = input(f"What is {x} + {y}?  ")
                z=int(ztext) #this line of code turns the text answer into the number

            print('correct')

    elif choice2 == '2':

        for i in range(1,12): #this loops the code 12 times from 1 to 12

            x = random.randint(10,99)
            y = random.randint(10,99)

            ztext = input(f"What is {x} + {y}?  ")
            z=int(ztext) #this line of code turns the text answer into the number

            while z != x+y: #this means while x does NOT equal the correct answer

                print('wrong. Try again')
                ztext = input(f"What is {x} + {y}?  ")
                z=int(ztext) #this line of code turns the text answer into the number

            print('correct')

    elif choice2 == '3':

        for i in range(1,12): #this loops the code 12 times from 1 to 12

            x = random.randint(100,999)
            y = random.randint(100,999)

            ztext = input(f"What is {x} + {y}?  ")
            z=int(ztext) #this line of code turns the text answer into the number

            while z != x+y: #this means while x does NOT equal the correct answer

                print('wrong. Try again')
                ztext = input(f"What is {x} + {y}?  ")
                z=int(ztext) #this line of code turns the text answer into the number

            print('correct')


elif choice =='s':
    
     #~THIS IS SUBTRACTION

    choice2= input("Type 1 if you want to take away 1-digit numbers, 2 if you want to take away 2-digit numbers, or 3 if you want to take away 3-digit numbers ")

    import random

    if choice2 == '1':

        for i in range(1,12): #this loops the code 12 times from 1 to 12

            x = random.randint(1,9)
            y = random.randint(1,9)
            while y>x:
                y = random.randint(1,9)

            ztext = input(f"What is {x} - {y}?  ")
            z=int(ztext) #this line of code turns the text answer into the number

            while z != x-y: #this means while x does NOT equal the correct answer

                print('wrong. Try again')
                ztext = input(f"What is {x} - {y}?  ")
                z=int(ztext) #this line of code turns the text answer into the number

            print('correct')

    elif choice2 == '2':

        for i in range(1,12): #this loops the code 12 times from 1 to 12

            x = random.randint(10,99)
            y = random.randint(10,99)
            while y>x:
                y = random.randint(10,99)

            ztext = input(f"What is {x} - {y}?  ")
            z=int(ztext) #this line of code turns the text answer into the number

            while z != x-y: #this means while x does NOT equal the correct answer

                print('wrong. Try again')
                ztext = input(f"What is {x} - {y}?  ")
                z=int(ztext) #this line of code turns the text answer into the number

            print('correct')

    elif choice2 == '3':

        for i in range(1,12): #this loops the code 12 times from 1 to 12

            x = random.randint(100,999)
            y = random.randint(100,999)
            while y>x:
                y = random.randint(100,999)

            ztext = input(f"What is {x} - {y}?  ")
            z=int(ztext) #this line of code turns the text answer into the number

            while z != x-y: #this means while x does NOT equal the correct answer

                print('wrong. Try again')
                ztext = input(f"What is {x} - {y}?  ")
                z=int(ztext) #this line of code turns the text answer into the number

            print('correct')

print('game over')


