#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
count = 0                            # счетчик попыток
number = np.random.randint(1,101)    # загадали число
print ("Загадано число от 1 до 100")
    
def game_core_v1(number):
    count = 0
    predict = 0
    left = 0
    right = 100
    while True:
        count += 1
        predict = (left+right)//2
        if number < predict:
            right = predict + 1
        elif number > predict:
            left = predict - 1
        else:
            break
    if number == predict:
        print(predict)
    return(count)
game_core_v1(number)


# In[ ]:




