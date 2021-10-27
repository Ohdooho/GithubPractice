score = []
STUDENT = 5
count=0
for i in range(STUDENT):
    a = int(input(f"{i+1} 번째 학생의 성적을 입력하세요 "))
    score.append(a)

print("성적 평균 =",sum(score)/STUDENT)
print("최대 점수 :",max(score))
print("최소 점수 :",min(score))
for i in range(STUDENT):
    if score[i] >=80:
        count+=1
print("80점 이상 :",count)