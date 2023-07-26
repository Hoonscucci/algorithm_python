from tkinter import *

주식가격
문제 설명
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

제한사항
prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
prices의 길이는 2 이상 100,000 이하입니다.
입출력 예
prices	return
[1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]
입출력 예 설명
1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.
※ 공지 - 2019년 2월 28일 지문이 리뉴얼되었습니다.

===================================================

# 주식가격
# 스택 큐
# 초단위 기록된 주식가격 prices 몇초동안 가격이 떨어지지 않는지
# 다음 수들을 탐색하며 자신보다 크면 초가 증가 while문?
# while que?
# que.popleft()  for 반복문 que 비교
#  > 면 break <면 time+=1


from collections import deque

def solution(prices):
    answer = []
    que = deque(prices)         # popleft를 사용하기 위해 deque를 사용해줬다.
    while que:                  # que가 있는동안
        time = 0                # time은 반복문 한바퀴가 돌면 0으로 설정
        que_pop = que.popleft() # 맨앞의 요소를 꺼내준다
        
        for q in que:           # que요소들을 하나씩 비교
            time+=1             # 요소를 하나 꺼낼때마다 time의 증가
            if que_pop > q:     # 4321 이 있으면 que_pop은 4, que = 3,2,1 q =3 첫번째 반복문에서  
                break           # for문 종료하고 while문 재실행 
                
        answer.append(time)     # 한번의 반복문이 끝나면 answer에 time을 append 해준다.
    return answer

"""
스택/큐로 풀 수 있던 문제
처음 가설과 다른 부분은 TIME 설정 위치와 else문의 존재 유무였다.
while이 먼저 올때와 for가 먼저올때의 지문의 차이를 좀 더 명확하게 확인해보고
예외처리가 될 수 있는것들이 무엇이 있나 좀 더 확인하는 연습을 해야겠다.
또한 로직의 동작 과정들을 잘 이해할 필요가 있을것같다."""