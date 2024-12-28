class AllFunctions():
    def Subfields():
        lists = [1,2,3,4,5,6]
        print("Sub-Fields in AI are:")
        for field in lists:        
            if (field == 1):
                print ("Machine Learning")
                message = "Machine Learning"
            elif (field == 2 ):
                print ("Neural Network")
                message = "Neural Network"
            elif (field == 3):
                print ("Vision")
                message = "Vision"
            elif (field == 4):
                print ("Robotics")
                message = "Robotics"
            elif (field == 5):
                print ("Speech Processing")
                message = "Speech Processing"
            else:
                print ("Natural Language Processing")
                message = "Natural Language Processing"

    def OddEven():
        number = int(input("Enter a number:"))
        if (number%2==0):
            print(number,"is Even Number")
        else:
            print(number,"is Odd Number")
            
    def Eligible():
        gender = input("Enter the Gender:")
        age = int(input("Enter the Age:"))
        if (gender == "Male" and age >= 21):
            print("Eligible")
        elif(gender == "Female" and age >= 18):
            print("Eligible")
        else:
            print("NOT ELIGIBLE")


    def percentage():
        subject1 = int(input("Subject1="))
        subject2 = int(input("Subject2="))
        subject3 = int(input("Subject3="))
        subject4 = int(input("Subject4="))
        subject5 = int(input("Subject5="))
        Total = subject1 + subject2 + subject3 + subject4 + subject5
        Percentage = Total/5
        print("Total :",Total)
        print("Percentage :",Percentage)


    def triangle():
        Height = int(input("Height="))
        Breadth = int(input("Breadth="))
        area_of_traingle = (Height*Breadth)/2
        print("Area formula: (Height*Breadth)/2")
        print("Area of Traingle:",area_of_traingle)
        Height1 = int(input("Height1="))
        Height2 = int(input("Height2="))
        Breadth1 = int(input("Breadth1="))
        print("Perimeter formula: Height1+Height2+Breadth1")
        perimeter_of_traingle = Height1+Height2+Breadth1
        print("perimeter of Traingle:", perimeter_of_traingle)


    

    