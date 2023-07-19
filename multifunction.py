class multifunction():
    def subfields():
        AI=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub fields in Ai are: ")
        for x in AI:
            print (x) #method 1
        print("+++++++++++++++++++++++++++++++")
        print("Sub fields in AI are: ")
        [print(i) for i in AI] #method 2
        
    # function to find even or odd
    def evenodd1():
        x=int(input("enter the number: "))
        if (x%2)==0:
            print(x,"Number is even")
            mesg=0
        else:
            print(x,"Number is odd")
            mesg=1
        #return mesg
        
     # function to find the eligibility for marriage
    def eligible():
        gen=input("Enter the gender :")
        age=int(input("Enter the age :"))
        if (gen.upper()=="M") & (age > 21):
            print("you are eligible")
        elif (gen.upper()=="F") & (age >18):
            print("You are eligible")
        else:
            print("You are not eligible")
            
    #function to find the area and perimeter of a triangle
    def triangle():
        h1=int(input("Enter the Hight1: "))
        h2=int(input("Enter the Hight2: "))
        b1=int(input("Enter the Breadth1: "))
        print("Height=",h1)
        print("Breadth=",b1)
        print("Area formula: (Height*Breadth)/2")
        area=(float(h1)*float(b1))/2
        print("Area of the triangle is: ",area)
        print("Height=",h1)
        print("Height2",h2)
        print("Breadth=",b1)
        print("Perimeter formula :Height1+height2+breadth")
        perimeter=h1+h2+b1
        print("Perimeter of the triangle is:",perimeter)

    def percentage():
        m1,m2,m3,m4,m5=input("Enter the marks :").split()
        print (m1,m2,m3,m4,m5)
        print("Subject1=",m1)
        print("Subject2=",m2)
        print("Subject3=",m3)
        print("Subject4=",m5)
        print("Subject5=",m5)
        sum=float(m1)+float(m2)+float(m3)+float(m4)+float(m5)
        percent=sum*100/500
        print("Total :",sum)
        print("Percentage :",percent)    
