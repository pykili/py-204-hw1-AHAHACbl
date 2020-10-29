a = input()
b=0
q = len(a)
for i in range (1, q):
  if int(a[i]) > int(b):
    b=a[i]
print(b)
