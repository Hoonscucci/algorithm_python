# 문제 설명
# String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환하는 함수, solution을 완성하세요. seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

# 제한 사항
# seoul은 길이 1 이상, 1000 이하인 배열입니다.
# seoul의 원소는 길이 1 이상, 20 이하인 문자열입니다.
# "Kim"은 반드시 seoul 안에 포함되어 있습니다.
# 입출력 예
# seoul	return
# ["Jane", "Kim"]	"김서방은 1에 있다"

=====================================

def solution(seoul):
    answer = ''
    for i in range(len(seoul)):
        if seoul[i] == 'kim':
            answer == i
    return ("김서방은 "+ str(i)+"에 있다")

"""
처음에 답인줄 알고 작성한 문장
for 문과 if문을 사용하여 답을 내려 했지만
첫번째 테스트는 통과했지만 제출 체점하니 통과못한 테스트가 많았다.
"""
=====================================

def solution(seoul):
    answer = ''
    
    return "김서방은 {}에 있다".format(seoul.index('Kim'))

"""
구글링을 통해 찾아낸 방법
상상도 못했다 더 솔직하면 문제도 잘 이해가 가지 않았다.
수학 교과서 깔짝보고 수학의정석 문제 푸는 기분이다...
풀다보면 늘지않을까 하는 마음에 계속 풀어본다
"""
=====================================

def solution(seoul):
    answer = ''
    i = seoul.index('Kim')
    return f"김서방은 {i}에 있다"

"""
구글링을 통해 얻은 답을 f -string 으로 나타내 보았다
좀 더 난잡해진 감이 있다
직관적으로 보기좋은 코드를 작성하는 연습이 필요하다
다음부터는 최대한 내 힘으로 풀어봐야겠다.
"""

================================================

def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            break
    return ('김서방은 '+str(i)+ '에 있다'
"""
첫번째 작성한 코드를 사용하기 위하여 if 문 다음에 break 를 걸어줌으로
Kim이 등장 했을때 종료되게 만들어주었다.
"""
