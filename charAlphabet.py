#7.Write a Python program to check whether a character is alphabet or not.
chrValue = str(input('Enter character :'))




if len(chrValue) == 1:
  if chrValue.isalpha() :
     print(f"'{chrValue}' is an alphabet.")
  else:
    print(f"'{chrValue}' is not an alphabet.")
else:
  print("Please enter only one character")
