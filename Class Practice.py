#!/usr/bin/env python
# coding: utf-8

# In[ ]:


color_list = ["Red","Green","White","Black"]


# In[ ]:


color_list[]


# In[ ]:


def number_addition(x,y):
    sumxy=x+y
    print(sumxy)
    
    


# In[ ]:


number_addition(3,7)


# In[ ]:


def number_multiplication(x,y):
    productxy=x*y
    print(productxy)


# In[ ]:


number_multiplication(4,1)


# In[ ]:


def number_subtraction(x,y):
    differencexy=x-y
    print(differencexy)


# In[ ]:


number_subtraction(3,73)


# In[ ]:


class Calculator:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
        
    def number_addition(self,x,y):
        sumxy=x+y
        return sumxy
    
    def number_subtraction(self,v,z):
        difference_vz=v-z
        return difference_vz
    
    def number_multiplication(self,a,b):
        product_ab=a*b
        return product_ab
    


# In[ ]:


Isaiah_obj = Calculator("Isaiah",16)


# In[ ]:


Isaiah_obj.number_multiplication(3,6)


# In[ ]:


Alpha_obj = Calculator("Alpha",28)
Alpha_obj.number_subtraction(3,73)


# In[3]:


class number_multiplication:
    def __init__(self,multiplier,multiplicand):
        self.multiplier = multiplier
        self.multiplicand = multiplicand
        
    def multiplication(self,multiplier,multiplicand):
        product = multiplier*multiplicand
        return product
    
    


# In[4]:


Isaiah_obj = number_multiplication(4,5)
Isaiah_obj.multiplication(4,5)


# In[ ]:


# A class is a group of functions that are all stored in one big function with the help of a constructor.

# Self helps the functions in the class know that they are related

# A constructor builds the foundation for the class and helps you setup what variables the class will need

0


# In[ ]:


Create a class called human
with a function that takes name and age as parameters
with a function called sleep that prints out that the person is sleeping
with a function called walk that prints out that the person is walking


# In[23]:


class Human:
    def __init__(self):
        pass
    
    def eat(self):
        print("This person is eating")
    
    def sleep(self):
        print("This person is sleeping")
        
    def walk(self):
        print("This person is walking")


# In[24]:


Isaiah_obj= Human()


# In[25]:


Isaiah_obj.sleep()


# In[26]:


Isaiah_obj.eat()


# In[27]:


Isaiah_obj.walk()


# In[ ]:




