a=""
string = input()
num = len(string)
for i in range(0, num):
  a=(a + string[num-i-1])
if a==string:
  is_palindrom=True
else: is_palindrom=False
print(is_palindrom)
