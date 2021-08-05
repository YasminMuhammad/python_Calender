#define no return
def say_hi(name) :
    print("Hi "+name)
    
#calling
say_hi("Ali") 
#طبعا ممكن تستقبل كذا براميتر و تعمل كذا تاسك و كدا يعني 

#define and calling returned functions
def cube(num) :
    return num*num*num
result=cube(5)
print(result)  #== print(cube(5))
