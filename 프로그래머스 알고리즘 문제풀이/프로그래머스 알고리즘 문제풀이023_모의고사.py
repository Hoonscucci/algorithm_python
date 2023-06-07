모의고사
문제 설명
수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한 조건
시험은 최대 10,000 문제로 구성되어있습니다.
문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
입출력 예
answers	return
[1,2,3,4,5]	[1]
[1,3,2,4,2]	[1,2,3]

=======================================

def solution(answers):
    result = []
    a_answer = []
    b_answer = []
    c_answer = []
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        if answers[i] == a[i]:
            a_answer.append(i)
        elif answers[i] == b[i]:
            b_answer.append(i)
        elif answers[i] == c[i]:
            c_answer.append(i)
        else:
            pass
    if len(a_answer)>0:
        result.append(1)
    if len(b_answer)>0:
        result.append(2)
    if len(c_answer)>0:
        result.append(3)
    result.sort()
    return result

"""
가체점에는 성공했지만 체점 요청시 런타임 에러로 
틀린답임을 알려줬음"""
=====================================

from itertools import chain, repeat
def solution(answers):
    result = []
    a_answer = []
    b_answer = []
    c_answer = []
    a = list(chain.from_iterable(repeat([1,2,3,4,5], 2000)))
    b = list(chain.from_iterable(repeat([2,1,2,3,2,4,2,5], 1250)))
    c = list(chain.from_iterable(repeat([3,3,1,1,2,2,4,4,5,5], 1000)))
    for i in range(len(answers)):
        if answers[i] == a[i]:
            a_answer.append(i)
        if answers[i] == b[i]:
            b_answer.append(i)
        if answers[i] == c[i]:
            c_answer.append(i)
        
    if len(a_answer)> len(b_answer) and len(a_answer) > len(c_answer):
        result.append(1)
    elif len(a_answer)< len(b_answer) and len(b_answer) > len(c_answer):
        result.append(2)
    elif len(c_answer)> len(b_answer) and len(a_answer) < len(c_answer):
        result.append(3)
    elif len(a_answer)==len(b_answer)==len(c_answer):
        result.append(1)
        result.append(2)
        result.append(3)
    elif len(a_answer)==len(b_answer):
        result.append(1)
        result.append(2)
    elif len(a_answer)==len(c_answer):
        result.append(1)
        result.append(3)
    elif len(b_answer)==len(c_answer):
        result.append(2)
        result.append(3)
    result.sort()
    return result

"""
풀었다는거에 의의를 두기로했다 ㅋㅋㅋ
일단 리스트의 반복을 하기 위하여 itertools에 있는 chain과 repeat을 불러왔고
빈 리스트들을 만들고 문제가 최대 1만개 이기에
a는 2000번, b는 1250번 c는 1000번 반복하여 1만개의 찍은답을 설정해줌
그후 for문을 사용하여 answers에 인덱스번호와 a,b,c 각각의 답지 인덱스 번호를 비교해
맞으면 각각의 리스트에 append 해주었다

그 후 len을 사용하여 각 리스트별 들어있는수의 길이(정답수)를 기준으로
어떤 수가 return될지 설정 해주었다.
그리고 마지막에 result에 sort해주어 오름차순 정렬 해주었다.
"""

===============================================

def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

"""
아직 코드해석이 제대로 되지 않는다 
시간이 나면 코드 해석을 추가로 작성할 예정
"""