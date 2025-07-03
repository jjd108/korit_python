#딕셔너리

profile = {
    "이름": "jjd",
    "나이": 00,
    "취미":["책 읽기", "음악듣기"]}


# 요소 접근
print(profile["이름"])
print(profile["취미"][1])

#요소 수정
profile["나이"] = 1
print(profile)

#요소 추가
profile["직업"] = "학생"
print(profile)

#요소 삭제
del profile["직업"]
print(profile)
profile.clear() #전체 삭제



#키만 불러오기
print(profile.keys())

#r값만 불러오기
print(profile.values())

#키 값 둘다
print(profile.items())

pydoc_grade = {
    "kelly" : "b",
    "jison": "a",
    "ian" : "c",
    "elly" : "d"}
print(sorted(pydoc_grade.items())) #키 기준 오름차순 정렬
print(sorted(pydoc_grade.items(),reverse=True)) #키 기준 내림차순 정력

student = {}
#이름을 입력받고 해당 이름을 키로, 점수를 입력 받고 값으로 추가
name = input("이름을 입력하세요: ")
score = input(f"{name}의 점수를 입력하세요: ")
student[name] = score
print(student)