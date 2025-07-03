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