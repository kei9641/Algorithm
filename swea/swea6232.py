words = input()

if words == words[::-1]:
    print(words)
    print('입력하신 단어는 회문(Palindrome)입니다.')