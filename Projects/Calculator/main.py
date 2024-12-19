#SImpleCalc Without Match Case Number
e=input("ENTER THE FIRST NUMBER: ")
d=input("ENTER THE SECOND NUMBER: ")
print("ADDITITON: ",int(e)+int(d))
print("SUBTRACTION: ",int(e)-int(d))
print("MULTIPLICATION: ",int(e)*int(d))
print("DIVISION: ",int(e)/int(d))

#SimpleCalc With Match Case Number

a=int(input("ENTER FIRST NUMBER: "))
b=int(input("ENTER SECOND NUMBER: "))

print(" + ")    
print(" - ")
print(" * ")
print(" / ")
inpu_t=input("SELECT THE SIGN: ")

match inpu_t:
    case "+":
        print("ADDITION: ", a+b)
    case "-":
        print("SUBTRACTION: ",a-b)
    case "*":
        print("MULTIPLICATION: ",a*b)
    case "/":
        print("DIVISION: ",a/b)

