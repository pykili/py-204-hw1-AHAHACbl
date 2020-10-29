l=0
m=0
user_input = input()
a = len(user_input)
for i in range(0,a):
  for j in range(0,a):
    if user_input[i]==user_input[j]:
      l=l+1
      if l>m:
        m=l
        most_frequent_character = user_input[i]
  l=0
  j=0
print(most_frequent_character)
