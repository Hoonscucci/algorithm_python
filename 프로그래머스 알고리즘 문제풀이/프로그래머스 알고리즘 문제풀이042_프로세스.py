프로세스
문제 설명
운영체제의 역할 중 하나는 컴퓨터 시스템의 자원을 효율적으로 관리하는 것입니다. 이 문제에서는 운영체제가 다음 규칙에 따라 프로세스를 관리할 경우 특정 프로세스가 몇 번째로 실행되는지 알아내면 됩니다.

1. 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.
2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.
  3.1 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료됩니다.
예를 들어 프로세스 4개 [A, B, C, D]가 순서대로 실행 대기 큐에 들어있고, 우선순위가 [2, 1, 3, 2]라면 [C, D, A, B] 순으로 실행하게 됩니다.

현재 실행 대기 큐(Queue)에 있는 프로세스의 중요도가 순서대로 담긴 배열 priorities와, 몇 번째로 실행되는지 알고싶은 프로세스의 위치를 알려주는 location이 매개변수로 주어질 때, 해당 프로세스가 몇 번째로 실행되는지 return 하도록 solution 함수를 작성해주세요.

제한사항
priorities의 길이는 1 이상 100 이하입니다.
priorities의 원소는 1 이상 9 이하의 정수입니다.
priorities의 원소는 우선순위를 나타내며 숫자가 클 수록 우선순위가 높습니다.
location은 0 이상 (대기 큐에 있는 프로세스 수 - 1) 이하의 값을 가집니다.
priorities의 가장 앞에 있으면 0, 두 번째에 있으면 1 … 과 같이 표현합니다.
입출력 예
priorities	location	return
[2, 1, 3, 2]	2	1
[1, 1, 9, 1, 1, 1]	0	5

==================================================

# 실행 대기큐에서 대기중인 프로세스를 꺼낸다.
# 뺀 프로세스보다 우선순위가 더 높은 프로세스가 있다면 뺀 프로세스 다시 큐로
# 없다면 꺼낸 프로세스 실행
# 실행한 프로세스는 다시넣지 않고 종료

# location은 인덱스 번호라고 생각해도 될듯
# 그럼 for in range를 priorities[i] 개념으로쓸수 있지않을까?

# answer에 append 하고 다음 수와 비교해서 정렬을 하고 
# answer[i] == priorities[location]  return i+1
# 똑같은 수가 있으면 에반데?
# 그렇다면 큰수 찾기랑 다른 개념으로 접근을 해야함

# 같은수를 어떻게 처리해야할까? 확인할수 있는방법은 answer이 아닌 priorities 에서 확인을 해야 할텐데?

# 큰 수 찾기에서 k를 줄이던것 처럼 해당 answer에 priorities[location]이 answer에 append 될때 까지 count를 세서 return 한다면????
# len(priorities) 로 반복문을 돌리면서 i가 location일때까지 아니야 그러면 답이 안맞아

# 결국 맞추려면 priorities[location]이 answer[return] 이여야함 같은 숫자는 어떻게 처리할거냐
# 그럼 어떻게 해야 할까?
# count 하면서 ?
# 0번 인덱스가 1등일수도 있으니 answer = 1부터 시작
# deque 사용하여 left pop을 하고 max값이 아니면 deque에 다시 que
# max 값이면 location 확인 location 0 이면  return answer
# max값인데 location이 0이 아니면 location -1 , answer +1 하고 다시 반복문 수행
# 그럼 반복문을 while deque가 0보다 클때


"""
이번엔 코드를 작성하기 전에 가설을 먼저 설정을 했었다.
여러 가지 가설을 설정하고 그렇게 플로우를 진행했을때 일어날 변수들을 먼저 생각했다.
최대한 비판적으로 바라 보면서 틀릴수 있는 부분들을 체크했다.
index번호 기준으로 구분하기엔 같은 숫자들을 구분할수가 없었다.
그렇다 생각해낸 방법은 count를 하는 방법이였고 그것에 맞는
코드 플로우를 대충 적어보았다.
"""

#시도 1 
from collections import deque

def solution(priorities, location): 
    answer = 1
    que = deque(priorities)
    ind = location
    while len(que) > 0:
        q = que.popleft()
        if q < max(que):
            que.append(q)
        else:
            if ind == 0:
                return answer
            else:
                answer+=1
                ind-=1
                
    return answer

"""
결과가 3이 나왔다 테스트 세트에 대해 몇가지 가설을 설정 해봤다.
else문에는 더이상 추가 할게 없어 보였고 
첫번째 if 문에서 추가적인 조치가 필요 하다고 느꼈다.
첫번째 if문에도 ind의 감소가 필요 하다고 생각 되었다.
"""


#시도 2 
from collections import deque

def solution(priorities, location): 
    answer = 1
    que = deque(priorities)
    ind = location
    while len(que) > 0:
        q = que.popleft()
        if q < max(que):
            que.append(q)
            if ind == 0:
                ind = len(que)-1
            else:
                ind-=1
        else:
            if ind == 0:
                return answer
            else:
                answer+=1
                ind-=1
                
    return answer

"""
첫번째 if문에서도 ind가 0인지 확인을 했다 
사실 왜 저렇게 작성이 되어야 하는지는 모르겠다
입출력예를 보고 때려맞췄다.
테스트 케이스는 통과했으나 2,5,8,에서 런타임 에러가 났다.
"""

#시도 3
from collections import deque

def solution(priorities, location): 
    answer = 1
    que = deque(priorities)
    ind = location
    while len(que) > 1:
        q = que.popleft()
        if q < max(que):
            que.append(q)
            if ind == 0:
                ind = len(que)-1
            else:
                ind-=1
        else:
            if ind == 0:
                return answer
            else:
                answer+=1
                ind-=1
                
    return answer

"""python tutor로 시각화 했을때 while len(q) > 0으로 했을때
테스트 세트에 대해서 len(q)가 1일때 이미 세션이 모두 종료 되어서
len(q) > 1 로 바꿨더니 정답이제출 되었다."""