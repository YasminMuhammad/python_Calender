#three number to find the max number 
def max_num(number1 , number2 ,number3) :
    if number1>=number2 and number1>=number3 :
        return number1
    elif number2>=number3 and number2>=number1 :
        return number2
    else :
        return number3
#هي فانكشن جاهزه اصلا بس هي مرقعه و خلاص
print(max_num(20,15,9)) 
 #بنقارن استرينج بقا 
def macth_string(string1,string2) :
     if string1==string2 :
         print("Matched")
     else:
             print("Not matched")
             
macth_string("ali", "ali")            
