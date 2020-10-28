# coding:utf-8
a = ["a", "b", "a", "c", "a", "c", "b", "d", "e", "c", "a", "c"]
b= (2,3,5,1,2,5)
c={'a':5,'b':2,'c':1}

a.sort(key=lambda x:x,reverse=True)
#sort只能用于list,reverse为True时是降序，默认为升序
print(a)
print(sorted(a))
print(sorted(b,reverse=True))
print(sorted(c.items(),key=lambda x:x[1]))
print(sorted(c.items(),key=lambda x:x[0]))
print(c.items())
#sorted不会改变原来的数据，而是生成一个新的，并且不局限与list
d=[x for x in a if not x==b]
print(d)
print([str(x)+str(y) for x,y in zip(a,d)])