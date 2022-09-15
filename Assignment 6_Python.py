#!/usr/bin/env python
# coding: utf-8

# 1. In Python strings, the backslash "\" is a special character, also called the "escape" character. It is used in representing certain whitespace characters: "\t" is a tab, "\n" is a newline, and "\r" is a carriage return. Conversely, prefixing a special character with "\" turns it into an ordinary character.
# 
# 2. It is used in representing certain whitespace characters: "\t" is a tab, "\n" is a newline, and "\r" is a carriage return.
# 
# 3. To insert characters that are illegal in a string, use an escape character. An escape character is a backslash \ followed by the character you want to insert.
# 
# 4. The single quote in Howl's is fine because we’ve used double quotes to mark the beginning and end of the string.
# 
# 5. Multiline strings allow you to use newlines in strings without the \n escape character.
# 
# 

# In[4]:


'Hello world!'[1]


# In[5]:


'Hello world!'[0:5]


# In[6]:


'Hello world!'[:5]


# In[7]:


'Hello world!'[3:]


# In[8]:


'Hello'.upper()


# In[9]:


'Hello' .upper().isupper()


# In[10]:


'Hello'.upper().lower()


# In[11]:


'Remember, remember, the fifth of November.'.split()


# In[12]:


'-'.join('There can be only one.'.split())


# In[ ]:


The rjust(), ljust(), and center() string methods, respectively


# In[ ]:


The lstrip() and rstrip() methods remove whitespace from the left and right ends of a string, respectively.

