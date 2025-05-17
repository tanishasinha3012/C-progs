#Using Match case

num1 = int(input("Enter the first no:"))
num2 = int(input("Enter the second no:"))

operation = str(input("Enter the operation:"))

match operation:
    case "add":
        result = num1 + num2
        print("Sum =",result)

    case "subtract":
        result = num1 - num2
        print("Difference =",result)

    case "multiply":
        result = num1 * num2
        print("Product =",result)

    case "divide":
        if num2 != 0:
            print("quotient =",num1/num2)
        else:
            print("Denominator can't be 0")
            

    
