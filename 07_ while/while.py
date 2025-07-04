#반복문 (while)
""""

while 조건:
    반복할 코드
    (조건을 변경하는 코드)

"""

# num = 1
# while num <= 5:
#         print("숫자:", num)
#         num += 1
#
# num = 1
#
# while num <= 10:
#     print(num)
#
#     if num ==5: #num이 5가 되었을 때 반복 종료
#         break #반복을 종료하는 코드
#
#
#     num += 1

num = 0
while num < 10:
    num += 1

    if num % 3 == 0:
        continue

    print(num)
