#2a
def Fibonacci(n):
 if n<= 0:
  print("Incorrect input")
 elif n == 1:
  return 0
 elif n == 2:
  return 1
 else:
  return Fibonacci(n-1)+Fibonacci(n-2)
n = int(input("Enter a number:"))
print("Fibonacci number is:")
print(Fibonacci(n))

#2b
def BinToDec(b):
 return int(b, 2)
print("Enter the Binary Number: ")
bnum = input()
dnum = BinToDec(bnum)
print("\nEquivalent Decimal Value = ", dnum)
def OctToHex(o):
 return hex(int(o, 8))
print("Enter Octal Number: ")
onum = input()
hnum = OctToHex(onum)
print("\nEquivalent Hexadecimal Value =", hnum[2:].upper())
