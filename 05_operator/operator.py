#산술연산자
num1 =30
num2 =12
print(f"num1 + num2 = {num1 + num2}") #덧셈
print(f"num1 -num2 = {num1 - num2}") #뺄셈
print(f"num1 * num2 = {num1 * num2}") #곱셈
print(f"num1 / num2 = {num1 / num2}") #나눗셈 (실수 몫)
print(f"num1 // num2 = {num1 // num2}") #나눗셈 (정수 몫)
print(f"num1 % num2 = {num1 % num2}")

#대입연산자
X = 10
X += 5 # X = X+5 => 15
X *= 2 # X = X*2 => 30
# X =/ 5 # X = X / 5 => 6.0
X //= 5 #X =X // 5 => 6

#비교연산자
X =10
Y = 20
Z = 10
print(X == Z)
print(X > Y)
print(X == Y)
print(X != Z)
print(X <= Y)
print(X >= Z)

#논리연산자
a = True
b = False
print(not a and b)
print( a or b)
print( not b)

#조건연산자(상항연산자)
a = 10
b = 20

max_value = a if a > b else b

if a > b:
    max_value = a
else:
    max_value = b
print(max_value)

#홀수 판별
num = 13
result = "짝수" if num % 2 == 0 else "홀수"
print(result)

# 참일때 반환값 if 조건 else 거짓일때 반환값

