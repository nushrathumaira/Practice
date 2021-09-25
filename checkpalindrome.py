def checkPalindrome(inputStr: str):
  return inputStr == inputStr[::-1]

print(checkPalindrome("aba"))