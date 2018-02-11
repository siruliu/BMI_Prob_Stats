import random
li=[]
for i in range(100000):
	li.append(random.randint(1,6)+random.randint(1,6)+random.randint(1,6))

print(len([x for x in li if x>12 ])/len([x for x in li if x>=10 ]))
print(len([x for x in li if x>12 ])/len([x for x in li if x>10 ]))
print(len([x for x in li if x<=12 and x>=10 ])/len(li))