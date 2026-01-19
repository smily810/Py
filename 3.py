#3a
s = input("Enter a sentence: ")
w, d, u, l = 0, 0, 0, 0
l_w = s.split()
w = len(l_w)
for c in s:
 if c.isdigit():
  d = d + 1
 elif c.isupper():
  u = u + 1
 elif c.islower():
  l = l + 1
print ("No of Words: ", w)
print ("No of Digits: ", d)
print ("No of Uppercase letters: ", u)
print ("No of Lowercase letters: ", l)

#3b
import difflib
str1 = "Welcome to Computer Science"
str2 = "Welcome to Computer Network"
sequence = difflib.SequenceMatcher(a=str1.lower(), b=str2.lower())
difference = sequence.ratio()*100
difference = round(difference,1)
print("Similarity between two said strings:"+str(difference))
