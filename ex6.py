txt = input(" Enter the text: ")

mid = int(len(txt) / 2)

if txt[:mid] == txt[mid+1:][::-1]:
  print(" Palindrome.")
else:
  print(" Not Palindrome.")