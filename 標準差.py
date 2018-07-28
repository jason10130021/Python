
# coding: utf-8

# In[4]:


data= list(range(1, 101))
mean= sum(data)/100
total=0
for i in range(0, 100): 
    temp= (mean-data[i])**2
    total= total+temp
sd= (total/len(data))**0.5
sd

