#1
print(10 > 9)
print(10 == 9)
print(10 < 9)
#2
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
#3"
print(bool("Hello"))
print(bool(15)) #true
#4
x = Hello"
y = 15
print(bool(x))
print(bool(y)) #true
#5
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"])) #true
#6
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({})) #false
#7
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj)) #false
#8
def myFunction() :
  return True

print(myFunction()) #true
#9
def myFunction() :
  return True
#10
if myFunction():
  print("YES!")
else:
  print("NO!") #yes
#11
x = 200
print(isinstance(x, int)) #true


