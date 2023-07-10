기능개발
문제 설명
프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.

또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

제한 사항
작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
작업 진도는 100 미만의 자연수입니다.
작업 속도는 100 이하의 자연수입니다.
배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.
입출력 예
progresses	speeds	return
[93, 30, 55]	[1, 30, 5]	[2, 1]
[95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]

==========================================

from collections import deque
# 배포해야하는 순서대로,작업의진도와 개발 속도가 있을때 배포되는 갯수를 구하라
# [i-1]이 배포되기 전까지 [i]는 배포될 수 없다.
# deque를 사용하여 앞에서부터 뺀다? 라고 생각을 해보자
# 전체에 스피드 만큼 더해주는 반복문 생성 - progresses가 빈 list가 될때까지
# progresses[0]이 100이 아니면 반복문 수행하고 100보다 크면 deque
# for문을 수행해서 다음친구들이 100인지 확인하고 100이면 deque 아니면 stop
# 다시 while문 수행

def solution(progresses, speeds):
    answer = []
    dq = deque(progresses)
    while dq:
        cnt = 0
        for i in range(len(progresses)):
            dq_pop = dq.popleft()
            dq.append(dq_pop+speeds[i])
        if dq_pop < 100:
            continue
        else:
            for a in range(len(dq)):
                if dq[a] >= 100:
                    cnt+=1
                answer.append(cnt)
            
    return answer

"""
여러 방식으로 접근을 했으나 문제에 대한 결론을 찾아 내지 못했다.
먼저 추가해보고 확인하는 방식도 시도해보고
0번째 인덱스를 먼저 확인하고 후에 반복문으로 확인하는 방식도 해보고
했지만 방법을 찾을 수 없어 결국 검색을 했다 ㅜㅜ
확실히 lv2 문제라서 그런지 어려운 부분이 있다"""

===============================================

def solution(progresses, speeds):
    answer = []
    days = 0                 # 날짜가 지남을 카운트
    cnt = 0                  # 배포된 기능 카운트
    while progresses:        # progresses가 빈리스트가 아닐때 반복
        if (progresses[0]+days*speeds[0]) >=100: #progresses의 0번째 인덱스 +days*speeds[0]을 하여 100보다 크거나 같을때
            progresses.pop(0) # progresses의 0번째 인덱스를 빼고
            speeds.pop(0)     # apeeds의 0번쨰 인덱스를 뺀다
            cnt+=1            # 100이 넘었기에 cnt +1을 해준다.
        else:                 # progresses[0]+days*speeds[0]이 100보다 작을때
            if cnt > 0:       # cnt가 0보다크며 즉 첫번째 if문이 실해돼었으면(다음숫자 확인하는 flow)
                answer.append(cnt) # cnt를 answer에 추가
                cnt = 0       # cnt를 0으로 초기화
            else:             # progresses[0]+days*speeds[0]이 100보다 작을때 cnt가 0이면
                days+=1       # days +1을 해준다
    answer.append(cnt)        # 반복문이 종료되고 cnt를 append 해준다
    return answer

"""
사실 비슷한 문제를 다시 푼다고해도 이 문제를 풀 수 있을지 의문이 든다.
코드의 flow는 이해가 갔으나 전체 코드 구성을 다시 한다면 잘 모르겠다.
if구문과 else 또 else 달린 if와 else while 문 내에서의 append, 반복문 이후의 qppend
문제들을 풀때 조금 더 틀에 갇히지 않고 풀어 볼 수 있게 연습이 필요할것 같다.
"""

"""
검색결과 찾게된 코드 deque를 사용하지 않고 pop(0)을 사용 하였다.
전체적인 코드의 흐름은 나의 코드 흐름과 크게 다르지 않았는데
중간중간 디테일과 처리해야 할 것 들을 처리히지 못한것 같다.
확실히 lv2에 진입하면서 나의 생각대로 코드가 진행되지 않는것 같다... 
"""
    

   
