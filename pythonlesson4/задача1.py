a= int(input("Введите число месяцев="))
b= int(input("Введите сумму="))
proc= int(input("Введите процент"))
if a >=12:
    n=b+b*(proc/100)
    print("Твоя сумма", n)
else:
    print("Деньги возвращены", b)
    
