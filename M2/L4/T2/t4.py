'''
На Марс був відправлений шатл з вантажем. 
Частина коробок містить крихкі предмети 
і вимагає особливої обережності при перенесенні. 
Відомо, що номери таких коробок кратні трьом, 
а всього коробок n. 
Виведіть номери тих вантажів, 
з якими НЕ потрібно поводитися особливо акуратно.
Користувач вводить число n - число коробок. 
Програма повинна вивести всі числа від 1 до n, що не кратні 3
'''

n=int(input("кількість коробок:"))


print("коробки які не містять кригкого вантажу")
for number in range(1,n+1):
    if(number%3!=0):
        print(number)