a=""
string = input()
for i in string:
    a = i + a
if a==string:
    is_palindrom=True
else: is_palindrom=False
print(is_palindrom)
