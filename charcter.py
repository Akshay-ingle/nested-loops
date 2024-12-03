st=input('enter your own word:')
cr=input('enter your chracter:')
i=0
ct=0
while(i < len(st)):
    if(st[i]==cr):
        ct=ct + 1
    i=i + 1
print('the total umber of time',cr,'has ocurred=',ct)   