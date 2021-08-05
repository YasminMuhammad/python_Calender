print("\n############## Part 1 ##############\n")

names =["Ali","Ahmmad","Noha","Nancy"]
#print all elements
print(names)
#print the frist element
print(names[0])
#print the frist and the second element
print(names[0:2])
#change frist elemment to "Muhammad"
names[0]="muhammad"
#making sure about the change
print(names)

print("\n############## Part 2 ##############\n")

males =["Ali","Ahmmad"]
famales = ["Noha","Nancy"]
#print two lists spirately 
print (males,famales)
#print two lists in one list
famales.extend(males)
print (famales)
#OR
famales+=males
print(famales)

#adding element to the end of frist list
males.append("Alaa")
print(males)
#adding element to the start of frist list
males.insert(0,"Alaa")
print(males)
#remove Ali
males.remove("Ali")
print(males)
#remove lasr element and print it
print(males.pop())
print(males)
#to know what is the position of element
print(males.index("Alaa"))
# عدد مرات التكرار
print(males.count("Alaa"))
#sorting acending
males.sort()
print(males)
##copping  لو غيرت في القديمه الليست الجديده مش بتحس
new_list=males.copy()
print(new_list ,males)
#لو استخدمت = عشان انقل الداتا الليست الجديده هتتاثر بالتغيير اللي هيحصل في الليست القديمه
new_list=males

#remove all elements
males.clear() 
print(males)
