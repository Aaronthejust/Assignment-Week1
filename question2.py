#Question No 2
#Calculate Area of a Rectangle

#taking lenght and width as input for calculating area of rectangle
lenght = int(input("Enter lenght of the rectangle in cm: ")) #using int with input because it take string by default 
width = int(input("Enter width of the rectangle in cm: "))
area = lenght * width #rectangle area formula
print("The area of rectangle is: ", int(area), "cm\u00b2") #using unicode to print cm square