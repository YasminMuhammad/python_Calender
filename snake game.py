import random
import curses
s=curses.initscr() # بيظهرلي سكرين بعرض الشاشه
curses.curs_set(0)# عشان الكيرزر يبقا مخفي 
sh, sw = s.getparyx() #بيعمل احداثيات بحجم الشاشه

# بتعمل ويندو بتبدأ من الاحداثيات اللي بحددها 
#يعني هنا بقوله يبدأ من اول كورنر لاخر كورنر
w = curses.newwin(sh ,sw , 0,0)
w.keypad(1) #بعرفه انه اليوزر هيستحدم الكيبورد
w.timeout(100) # الشاشه بتريفريش كل 100 ملي ثانيه
# هيحددوا السنيك هيبقا فين أول ما ابدأ اللعبه
snk_x=sw//4 #هتظهر في ربع الشاشه
snk_y=sw//2 #هتظهر في نص الشاشه
#هتحدد شكل السنيك بحيث يتكون من 3 قطع و مش فوق بعض
snake=[
       [snk_y,snk_x],
       [snk_y,snk_x-1],
       [snk_y,snk_x-2]
       ]
#بقسم طول الشاشه و عرض الشاشه علي 2 عشان اقول ان انا عايز الاكل يظهر ف النص
food=[sh//2,sw//2] 
#بتاخد المكان اللي هيبدأ منه و بتاخد الشكل اللي المفروض يظهر علي الشاشه 
w.addch(food[0],food[1],curses.ACS_PI)

# بيحدد السنيك هيمشي ازاي و هنا هديله قيمه يمين ك انيشيال
key=curses.KEY_RIGHT
#لوب شغاله طول اللعبه
while True:
    #هاخد من اليوزر الانبوت اللي هو عمله
    next_key=w.getch()
    #لو اليوزر مداسش هيسيب الكي زي ماهو لو ضغط هياخد الكي الجديد
    key=key if next_key == -1 else next_key
    #هشوف لو خبط ف حاجه هطلع من البرنامج 
    if snake[0][0] in [0,sh] or snake[0][1] in [0,sw] or snake[0] in snake[1:] :
        curses.endwin()
        quit()
    new_head=[snake[0][0],snake[0][1]]
    # بحدد بيها موقع الراس فس الحركه 
    #لو اليوزر اتحرك لتحت هزود ال y ب 1
    if key==curses.KEY_DOWN :
        new_head[0]+=1
    #لو اليوزر داس فوق سيبقا الy هتقل بواحد 
    if key==curses.KEY_UP :
        new_head[0]-=1
    # لو مشي يمسن الاكس هتزيد 1
    if key==curses.KEY_RIGHT :
        new_head[1]+=1
    #لو داس شمال الاكس هيقل 1
    if key==curses.KEY_LEFT :
        new_head[1]-=1
    # هضيف النيو هيد لاول السناك
    snake.insert(0, new_head)
    #بشوفه كل ولا لا عشان اكبره بقا 
    if snake[0]==food:
        food=None
        while food is None:
            nf=[
                random.randint(1,sh-1),
                random.randint(1,sw-1)
                ]
            food=nf if nf not in snake else None
            
        w.addch(food[0],food[1],curses.ACS_PI)
    else:
        tail=snake.pop()
        w.addch(tail[0],tail[1,''])
    
    #هعرض بقا التعبان خلاص
    w.addch(snake[0][0],snake[0][1],curses.ACS_CKBOARD)
            
            
    
    



