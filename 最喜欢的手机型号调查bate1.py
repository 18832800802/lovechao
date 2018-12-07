phone = {}
test_phone = True
while test_phone:
    name = input('\n请输入您的名字?')
    phone1 = input('\n请输入您最喜欢的手机品牌？')
    phone[name] = phone1
    test2 = input('\n还有人参加调查吗？(y/n)')
    if test2 =='n':
        test_phone = False
#print(phone)
for name,phone in phone.items():
    print(name + '最喜欢的是' + phone + '!')
