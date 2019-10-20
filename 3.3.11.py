try:
    score = float(input('Input your score,\n'))
except:
    print('Bad Score')
if score >= .9 and score <= 1.0:
    print('your grade is A')
elif score >=.8 and score <.9:
    print('your grade is B')
elif score >= .7 and score <.8:
    print('your grade is C')
elif score >= .6 and score <.7:
    print('your grade is D')
elif score < 0.6:
    print('your are fail')
    
    
    