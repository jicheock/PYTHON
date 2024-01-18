# numlist = [1, 2, 3, 4, 5]
# a = map(lambda x: x ** 2, numlist)
# print(list(a))
# nlist=[1,2,3,4,5]
# b=map(lambda x: x+100,nlist)
# print(list(b))
coffeepricelist=[2000,2500,3000,4000]
d=map(lambda x: str(x+1000)+'원',coffeepricelist)
print(list(d))
fruit=['애플','망고','사과','바나나']
c=map(lambda x: len(x),fruit)
print(list(c))
# filter()
nlist=[1,2,3,4,5]
a=filter(lambda x: x>5,nlist)
print(a)
b=filter(lambda x: x%2==0,nlist)
print(b)
g=filter(lambda x: 'o'in x, fruit )
print(g)
h=filter(lambda x: len(x)>=3,fruit)
print(h)
i=map(lambda x: '🍻🍻🍻🍻'+x ,h)
print(list(i))