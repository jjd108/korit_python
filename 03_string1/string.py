#문자열의 인덱싱
a ="life is too short, you need python"
# print(a[-1])
#
# b= a[0] + a[1] + a[3]
# print(b)

#실습
#단어를 입력 받고 변수에 선언한 다음 첫번째 글자와 마지막 글자를 출력하시오
# word = input("단어를 입력하세요 :")
# print("첫번째 글자-", word[0])
# print("마지막 글자-", word[-1])

#슬라이싱
print(a[0:4]) #life
print(a[5:7]) #끝 번호는 자기 자신을 포함하지 않는다.
print(a[19:])
print(a[:17])
print(a[19:-7])
print(a[::2])
print(a[::-1]) #문자열 뒤집기git