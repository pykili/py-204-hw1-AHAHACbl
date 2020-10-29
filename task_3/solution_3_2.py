alphabet = ""
user_input = ""
for i in range (1,11):
  line = input()
  user_input = (user_input + line)
for i in user_input:
  if i not in alphabet:
    alphabet = (alphabet + i)
print(alphabet)
