#!/usr/bin/env python
# coding: utf-8

# In[6]:


items = [20, 30, 40, 3, 16]
maxValue = max(items)
minvalue =min(items)
print(maxValue,minvalue)
#excercise 59


# In[7]:


#excercise 1
a="lionel messi"
b=len(a)
print(b)


# In[14]:


#excercise2
a="lionel messi"
if len(a)<2:
  print(" ")
else:
  z=a[:2]+a[-2:]
print(z)


# In[16]:


#excercise(3)
item=input()
if item<3:
print(item)
else:
if item[-3:]==ing:
    print(item+"ing")
else:
    print(item+"ly")


# In[17]:





# In[19]:


#excercise(3)
item=input()
if item<3:
   print(item)
else:
 if item[-3:]=="ing":
    print(item+"ing")
 else:
    print(item+"ly")


# In[24]:


#excercise(3)
item=input()
if item<3:
  print(item)
else:
if item[-3:]=="ing":
    print(item+"ly")
else:
    print(item+"ing")


# In[29]:


#excercise 4
names=["kvaratisikhalia","chaliouba","batistuota"]
maxname=0
maxlen=0
for name in names:
    if len(name)>maxlen:
     maxlen=len(name)
     maxname=name
    print(maxlen,maxname)


# In[30]:


#excercise 5
name=input()
print(name[-1]+name[1:-1]+name[0])


# In[31]:


#excercise 6
name=input()
print(name[0::2])


# In[40]:


sentance="messi won the world cup when he was old and make paris fans want to kill him"
strings=set(sentance.split(" "))
maxstring=0
maxnumber=0
for string in sentance:
    if sentance.count(string)>maxnumber:
        maxnumber=sentance.count(string)
        maxstring=string
        print(maxnumber,maxstring)


# In[41]:


#excercise 8
a="lionel messi"
print(a.upper())


# In[44]:


#excercise 9
a="june"
if len(a)%4==0:
    print(a[::-1])


# In[49]:


#excercise 10
a='''qwertyuiiljjjggddssd
assdsdsasasdsgfdgfhgf'''
b=a.splitlines()
print(b)


# In[56]:


#excercise 11
a="lionelmessi"
if a[0]=="l":
 print(True)


# In[61]:


#excercise 12
x="my name is %s"%b
b="ahmed"
print(x)


# In[71]:


#excercise 15
n="mohamed"
if len(n)%4==0:
    print(n[::-1])


# In[86]:


#excercise 17
sentance="mohamed went to univercity very day"
strings=set(sentance.split(" "))
maxstring=0
maxnumber=0
for string in sentance:
    if sentance.count(string)>maxnumber:
        maxnumber=sentance.count(string)
        maxstring=string
        print(maxnumber,maxstring)


# In[87]:


#excercise 16
x="ahmed"
print(x[::-1])


# In[90]:


# excercise1 18
sentance="mohamed ali kley is the best boxing player"
strings=set(sentance.split(" "))
maxstring=0
minnumber=0
for string in sentance:
    if sentance.count(string)==minnumber:
        minnumber=sentance.count(string)
        maxstring=string
        print(minnumber,maxstring)


# In[ ]:




