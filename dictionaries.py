names_dec={
    "A": "Ahmad"
    ,"M": "Muhammad" 
    ,"B":"Basem"
    }
print(names_dec["A"])
#OR
print(names_dec.get("A"))
#الداله دي لو اديتها كي مش موجود هتطبع none
#بس ممكن احددلها تطبع اي لو انا دخلت كي مش موجود
print(names_dec.get("S","Not found"))
# لو انا حطيت 2 كي زي بعض هبقا كأني بعمل اوفررايد
#كدا هياخد القيمه التانيه مش الاولي اللي اتحطت للكي 