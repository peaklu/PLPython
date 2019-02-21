Dollor = input()
if Dollor[0:3] in ['rmb','RMB']:
    USD = eval(Dollor[3:])/6.78
    print ("USD{:.2F}".format(USD)) 
elif Dollor[0:3] in ['USD','usd']:
    RMB = (eval(Dollor[3:]))*6.78
    print("RMB{:.2f}".format(RMB))
else:
    print("您的输入格式有误")
