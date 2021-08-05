from math import *
#Number
x = 3   # y will be 3
print(x)

y = 3.0  # z will be 3.0
print(y)

#convert number to string 
z = "3"    # x will be '3'
print(z)

#القيمه المطلقه 
print(abs(-4))  # it will be 4

#داله الاس بتاخد رقمين (الاساس و الاس)
print(pow(2, 3))     # it will be 8.0

#بتطبع اكبر رقم 
print(max(3,7,9,2,5))    # it will be 9

#بتطبع اصغر رقم 
print(min(3,7,9,2,5))    # it will be 2

#round => بتقرب الرقم 
print(round(3.6))  # it will be 4

#floor => بتقرب الرقم للاقل 
print(floor(3.9))  # it will be 3

#ciel   => بتقرب الرقم للاعلي 
print(ceil(3.1))  # it will be 4

#sqrt => بتاخد الجزر
print(sqrt(16))  # it will be 4.0

###########################

# Strings 
name = "Yasmin Muhammad"

#upper => بتحول كل الحروف تخليها كابيتل
print(name.upper())    # it will be 'YASMIN MUHAMMAD'

#lower => بتحول كل الحروف تخليها كابيتل
print(name.lower())       # it will be 'yasmin muhammad'

#isupper => لو كله كابيتل بتطلع ترو 
print(name.isupper()) # it will be false 

#islower => لو كله سمول بتطلع ترو 
print(name.islower()) # it will be false 

#len => بترجعلي طول الكلمه اللي عندي 
#print(name.len) 

#عشان اطبع اي حرف جوه السترينج عندي بستخدم رقمه 
print(name[0])      #it will be Y

#index => عشان اعرف الاندكس لحرف معين ولو حطيتله كلمه بيطلعلي اندكس اول 
print(name.index('a'))

#reblace => ببدل حاجه بحاجه تانيه ف التكيست
#print(name.reblace('Muhammad', 'Ali'))

