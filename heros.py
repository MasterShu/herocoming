'''
Heros beta-0.0.1
mastershu
2017-10-26
'''
hp = 100
helpTitle = "'a' for left, 'd' for right!"
print('welcome Heros world')
print("the world is like this ##### , 'a' for left, 'd' for right!")
# 获取用户输入的英雄名
name = input("input your name: ")
if not name:
    name = 'player01'

userMsg = [name, hp]
# print(userMsg)
print("your hero's is: ", userMsg[0], ', Hp is : ', userMsg[1])
print('and now you are here: *####', helpTitle)
userInput = input()
if userInput == 'd':
    print('you are here #*###')
if userInput == 'a':
    print('you are here *####')
