자연수 뒤집어 배열로 만들기
문제 설명
자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

제한 조건
n은 10,000,000,000이하인 자연수입니다.
입출력 예
n	return
12345	[5,4,3,2,1]

========================================
def solution(n):
    answer =[]
    list_n = list(str(n))
    list_n.reverse()
    for i in list_n:
        answer.append(int(i))
    return answer
        
"""
answer 이라는 빈 list를 만들어주고
list_n에 정수n을 문자열로 바꿔주고 list로 감싼 후 
reverse 함수를 써서 배열을 거꾸로 바꾸어 주었다.
그 후 for문을 사용하여 하나하나 int로 바꾸어 answer에 추가하였다.
"""
========================================

def digit_reverse(n):
    return list(map(int, reversed(str(n))))

"""
map 함수를 생각했었는데 활용 방법이 정확하지 않아 다시 지웠었다
문자열로 바꾼 n을 reversed로 뒤집어 주고 map함수로 int로 바꿔주고
list로 감싸 주었다.
"""
========================================
def digit_reverse(n):
    a=[]
    for i in str(n):
        a.append(int(i))
    a.reverse()
    return a

"""
코드 자체는 내가 푼것과 비슷 했지만
이 코드는 먼저 append 하고 reverse 함수를 사용하였다.
"""
========================================
