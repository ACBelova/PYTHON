#Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30
x= int(input('введите число '))
if not x%5:
   print ('число кратно 5 ')
elif not x%10:
    print ('число кратно 10 ')
elif not x%15:
    print ('число кратно 15 ')


else: print ('число не кратно 5,10, или 15 ')
