import math
n = int(input())
m = math.floor(n**(1/2)+1)
answer = []
num = 2
if n == 1 or n ==2:
        print(n) # 1일때 0, 2일때 1 아니라 왜 1,2인지 궁금
else:
    for i in range(m+1):
        if n > 2**i:
            answer.append(i)

    print((n - num**answer.pop())*2)

"""
시간 80ms
deque 함수를 사용하기 싫어서 패턴을 분석했음
n이 1,2가 아니였을때
(n > 2**m
(n - 2**m) *2) 라는 패턴을 발견 할 수 있었음
n은 입력받는 정수 
m은 인력받는 정수의 제곱근을 내림한 후 1을 더해줌
if n=1 or 2 일경우 n을 프린트 하게 해주고
else문에 for문을 돌려서 i에 range(m+1)을 해줌
if n > 2**i 이면 answer에 append해주고
그중 가장 큰수는 마지막에 있는 수 일테니 answer.pop()으로 가장 큰 수를 꺼낼 수 있음
(n - num(2)**answer.pop())*2 로 패턴에 맞는 값을 도출 할 수 있게 만들어 줬음
"""





# n = int(input())
# answer = list(range(2,n+1,2))

# while (len(answer) > 1):
#     answer.pop(0)
#     a = answer.pop(0)
#     answer.append(a)

# print(answer.pop())

"""
시간초과 나옴
"""

from collections import deque

n = int(input())
deque = deque([i for i in range(1, n+1)])

while(len(deque) >1):
    deque.popleft()
    a = deque.popleft()
    deque.append(a)
    
print(deque.pop())

"""
시간 292ms
전체적인 코드 구성은 depue를 쓰지않았을때랑 같음
"""