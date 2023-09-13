알고리즘 입문방 오픈 채팅방에서는 새로운 분들이 입장을 할 때마다 곰곰티콘을 사용해 인사를 한다. 이를 본 문자열 킬러 임스는 채팅방의 기록을 수집해 그 중 곰곰티콘이 사용된 횟수를 구해 보기로 했다.

ENTER는 새로운 사람이 채팅방에 입장했음을 나타낸다. 그 외는 채팅을 입력한 유저의 닉네임을 나타낸다. 닉네임은 숫자 또는 영문 대소문자로 구성되어 있다.

새로운 사람이 입장한 이후 처음 채팅을 입력하는 사람은 반드시 곰곰티콘으로 인사를 한다. 그 외의 기록은 곰곰티콘을 쓰지 않은 평범한 채팅 기록이다.

채팅 기록 중 곰곰티콘이 사용된 횟수를 구해보자!

입력
첫 번째 줄에는 채팅방의 기록 수를 나타내는 정수 
$N$ 이 주어진다. (
$1 \le N \le 100\,000$)

두 번째 줄부터 
$N$ 개의 줄에 걸쳐 새로운 사람의 입장을 나타내는 ENTER, 혹은 채팅을 입력한 유저의 닉네임이 문자열로 주어진다. (문자열길이
$1 \le \texttt{문자열 길이} \le 20$)

첫 번째 주어지는 문자열은 무조건 ENTER이다.

출력
채팅 기록 중 곰곰티콘이 사용된 횟수를 출력하시오.

예제 입력 1 
9
ENTER
pjshwa
chansol
chogahui05
lms0806
pichulia
r4pidstart
swoon
tony9402
예제 출력 1 
8
예제 입력 2 
7
ENTER
pjshwa
chansol
chogahui05
ENTER
pjshwa
chansol
예제 출력 2 
5
첫번째 새로운 사람이 들어온 뒤  pjshwa, chansol, chogahui05은 모두 곰곰티콘으로 인사했다.

두번째 새로운 사람이 들어온 뒤  pjshwa와 chansol은 다시 곰곰티콘으로 인사했다.

예제 입력 3 
3
ENTER
lms0806
lms0806
예제 출력 3 
1

===================================

n = int(input())
l = input().split(" ")

cnt = 0

for i in range(n):
    if l[i] == "ENTER":
        continue
    else:
        cnt+=1

print(cnt)

"""
튜터 에서는 돌아가는데 백준에서 돌아가지 않는다 
아마도 l을 받는 부분에서 문제가 있는거 같은데
참으로 까다로운 백준...
"""

====================================

n = int(input())

cnt = 0

for _ in range(n):
    l = input()
    if l == "ENTER":
        check_name = []
        continue
    else:
        if l not in check_name:
            check_name.append(l)
            cnt+=1
        else:
            continue
        

print(cnt)

"""
hash로 접근해야 한다고 하는데
hash말고 풀어보고 싶어서 풀었는데 시간 초과가 뜬다
파이썬 튜터에서는 정상적으로 작동이 되는데...
hash를 이용해서 풀어봐야겠다.
"""

=============================================

import sys
input = sys.stdin.readline

s = set()
n = int(input())

cnt = 0

for _ in range(n):
    l = input().strip()
    if l == "ENTER":
        s.clear()
        continue
   
    if l not in s:
        s.add(l)
        cnt+=1
    else:
        continue
        

print(cnt)
        
"""
백분에서 여러 문장을 받을때 반복문으로 받으면 시간초과가 뜬다는걸 알아서 sys.stdin.readline 을 추가해줬고
set함수를 사용해서 반복된것들을 제거했다.
전체적인 로직은 전꺼와 별반 다를게 없는데...
백준이 밉다...
"""
        