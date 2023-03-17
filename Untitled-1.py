print("Калькурятор")
colvo = int(input("Введите количество: "))
number = float(input("Введите число: "))
sum = number
i = 1

while i != colvo:
    number2 = float(input("Введите второе число: "))
    oper = (input("Введите символ: "))
    if (oper == "+"):
        sum += number2
        print(sum)
    elif (oper == "-"):
        sum -= number2
        print(sum)
    elif(oper == "*"):
        sum = sum * number2
        print(sum)
    elif(oper == "/"):
        if (number2 ==0 or number ==0 and sum == "/"):
                print ("На ноль делить нельзя")
        else:
            sum = sum/number2
            print(sum)
    elif (oper == "^"):
        sum = sum**number2
        print(sum)
    elif (oper == "%"):
        sum = sum%number2
        print(sum)
    else:
        print("Ошибка! Неправльный знак")
            
i+=1
