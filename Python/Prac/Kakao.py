def solution(new_id):
    new_id = new_id.lower() #1단계
    answer=''
    for word in new_id:
        if word.isalnum() or word in '-_.':
            answer += word #2단계
    while '..' in answer:
        answer=answer.replace('..','.') #3단계
    if answer[0] == '.':
        answer = answer[1:]
    if answer[-1] == '.':
        answer = answer[:-1] #4단계
    if answer == '':
        answer ='a' #5단계
    if len(answer)>=16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    while len(answer)<3:
        answer+=answer[-1]

    return answer

a = solution("...!@BaT#*..y.abcdefghijklm")

print(a)
