print("select the operations:\n"
	  "1.Addition:\n"
	  "2.Subtraction:\n"
	  "3.Multiplication\n"
	  "4.Division\n")
select=int(input("Enter the operation:"))
x=int(input("enter number1:"))
y=int(input("enter number2:"))
if select==1:
   (lambda x,y : print(x+y))(x,y)
elif select==2:
     (lambda x,y : print(x-y))(x,y)
elif select==3:
     (lambda x,y : print(x*y))(x,y)
elif select==4:     
     (lambda x,y : print(x/y))(x,y)
else:
     print("please enter valid operator.")
