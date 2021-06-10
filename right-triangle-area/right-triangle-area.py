a = float(input("First leg lenght: "))
if a < 0:
    print("Error! Negative leg length!")
else:
    b = float(input("Second leg lenght: "))
    if b < 0:
        print("Error! Negative leg length!")
    else:
        print("Area of the triange is ", a * b / 2)