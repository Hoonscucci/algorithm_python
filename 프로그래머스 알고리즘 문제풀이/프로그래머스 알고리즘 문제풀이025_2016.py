2016년
문제 설명
2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요? 두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요. 요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT

입니다. 예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 "TUE"를 반환하세요.

제한 조건
2016년은 윤년입니다.
2016년 a월 b일은 실제로 있는 날입니다. (13월 26일이나 2월 45일같은 날짜는 주어지지 않습니다)
입출력 예
a	b	result
5	24	"TUE"

==================================================

import calendar

def solution(a, b):
    answer = calendar.weekday(2016,a,b)
    if answer == 0:
        answer = 'MON'
    if answer == 1:
        answer = 'TUE'
    if answer == 2:
        answer = 'WED'
    if answer == 3:
        answer = 'THU'
    if answer == 4:
        answer = 'FRI'
    if answer == 5:
        answer = 'SAT'
    if answer == 6:
        answer = 'SUN'
    return answer

"""
import calendar 말고는 도저히 모르겠다.
calendar를 import 해와서 calendar.weekday(2016,a,b)로 2016년 a월 b일에 대하여
0,1,2,3,4,5,6으로 나오게 하였다
그 후 각 숫자마다 if문을 걸어서 
원하는 답이 나오게 설정했다.
"""
=================================================