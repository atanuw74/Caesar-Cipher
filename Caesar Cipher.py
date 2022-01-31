#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install pyperclip')
#6nyynzJnnyrx8zJznzJ0ur5rJv6J!285Juvwno
import pyperclip
message=input("Enter the message to encode/decode ")
key=13
mode=input("To encode type 'encrypt'and to decode type 'decrypt' ")
SYMBOLS="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."
translated = ''
for symbol in message:
    if symbol in SYMBOLS:
        symbolindex=SYMBOLS.find(symbol)
        if mode=="encrypt":
            translatedindex=symbolindex+key
        elif mode=="decrypt":
            translatedindex=symbolindex-key
        if translatedindex>=len(SYMBOLS):
            translatedindex=translatedindex-len(SYMBOLS)
        elif translatedindex<0:
            translatedindex=translatedindex+len(SYMBOLS)
        translated=translated+SYMBOLS[translatedindex]
    else:
        translated= translated+symbol
print(translated)
pyperclip.copy(translated)

            

