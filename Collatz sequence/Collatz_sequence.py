# generating the collatz_sequence 
# Date: 22-3-2020
def collatz_sequence():
    number = 0
    number = int(input("Enter a postive number,or zero to quit: ")) #taking Number
    average = number      #create for computing average
    total_number = 0      # calculating total of iteration
    counter = 1
    if number == 0:
        print("Have a nice day")
    else:
        print (number,end=" ")
        # Loop is create 
        while(number != 1):
            if counter == 5:
                print()
                counter = 0
            # This part is for odd
            if number%2 != 0:
                number = (number*3)+1  #3n+1 formula
                average = average + number 
                print(number,end=" ")
            #This part is for even 
            else:
                number = int(number/2)
                average = average + number
                print(number,end=" ")
            counter = counter+1
            total_number = total_number + 1
        print()
        # Printing
        print("It took",total_number,"iterations to arrive at 1")
        print("The average value is",average/total_number)
collatz_sequence()