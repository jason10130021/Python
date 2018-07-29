
# coding: utf-8

# In[ ]:


import random
name=input("敢問大俠您尊姓大名: ")
conti=1
vic=1
while conti<2:
    player= int(input("看我的，剪 刀 石 頭 布!!(請輸入你想出的拳) 1)剪刀 2)石頭 3)布 :"))
    result=random.randint(1,3)
    if result==1: 
        print("我輸了，"+name+"，你是天下第一...")
        conti= int(input("1) 再給你一次機會挑戰我 2)練過再來吧"))
    elif result==2: 
        print("切! 我還以為你是多厲害的人物，原來不過如此而已，難道沒人能擊敗我嗎??")
        conti= int(input("1) 我還沒使出全力呢 2)不猜了不猜了"))
    elif result==3 :
        print("平手，再戰一回!!")
        conti=1
    else: 
        print("你到底要不要出拳!!")
        conti=1
print("大俠，我們來日再相見了")

