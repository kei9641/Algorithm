while 1:
  # 입력
  number = input()
  isPalindrome = True

  # 입력이 0이면 종료
  if number == '0':
    break
  
  # 팰린드롬 검사
  length = len(number)
  for i in range(length//2):
    if number[i] != number[length-i-1]:
      isPalindrome = False
      break
  
  # 출력
  if isPalindrome:
    print('yes')
  else:
    print('no')