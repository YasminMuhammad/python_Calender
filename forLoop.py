text = "Yasmin"
# هتطبعلي حروف الكلمه
for letter in text:
    print(letter)

names = ["Ali", "Alaa", "Sara", "Rana"]
# هيطبع عناصل الليست اللي عندي
for name in names:
    print(name)
# OR
for index in range(len(names)):
    print(names[index])

# هيطبع من 0 ل 9
for number in range(10):
    print(number)


# هيطبع من 0 ل عدد الحروف هنا -1
for letter in range(len("Yasmin Muhammad")):
    print(letter)


# بيشوف الاسم دا موجود ولا لا
for name in names:
    if name == "Ali":
        print("Ali in your list ")
        break
else: 
    print("Not found ")
    
#هطبع الارقام و اي الزوجي و الفردي من 0 ل 9
for number in range(10):
    if number%2==0 :
        print(number," is even number ")
    else:
         print(number," is odd number ")
         
