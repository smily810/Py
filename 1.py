#1a
test1 = float(input("Enter Test1 marks: "))
test2 = float(input("Enter Test2 marks: "))
test3 = float(input("Enter Test3 marks: "))
if test1 <= test2 and test1 <= test3:
 min_score = test1
elif test2 <= test1 and test2 <= test3:
 min_score = test2
else:
 min_score = test3
average = (test1 + test2 + test3 - min_score) / 2
print("The Average of Best Two Tests is : ", average)

#1b
val = int(input("Enter a value : "))
str_val = str(val)
if str_val == str_val[::-1]:
 print("Palindrome")
else:
 print("Not Palindrome")
for i in range(10):
 if str_val.count(str(i)) > 0:
  print(str(i), "appears", str_val.count(str(i)), "times");
