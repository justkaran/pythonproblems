str = "OTTO"
# what if we wanted to use recursion?
'''def palindrome_1(str):
  if len(str) <= 1:
    return True
  if str[0] != str[-1]:
    return False
  return palindrome_1(str[1:-1])

print(palindrome_1(str))

print(str[1:-1])'''


def palindrome_2(str):
  str = str.lower()
  for i in range(len(str)//2):
    if str[i] != str[-i -1]:
      return False
  return True


print(palindrome_2(str))