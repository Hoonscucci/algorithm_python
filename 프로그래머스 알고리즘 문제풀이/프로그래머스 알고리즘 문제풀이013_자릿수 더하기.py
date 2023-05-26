자릿수 더하기
문제 설명
자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

제한사항
N의 범위 : 100,000,000 이하의 자연수
입출력 예
N	answer
123	6
987	24

=====================================

def solution(n):
    answer = 0
    str_n = str(n)
    for i in range(len(str_n)):
        answer += int(str_n[i])
    return answer

"""
입력받는 정수 n을 문자열로 바꿔주고
그 문자열의 길이를 range 함수를 사용하여 i에 넣어준다
그리고나서 answer에 문자열로 바꾼 n의 i로 인덱스 하여 더하기 해준다.
"""

=========================

def sum_digit(number):
    return sum(map(int, str(number)))

"""
map 함수에 대한 개념이 잡혀 있지 않았었다.
map 함수를 사용하여 str(number)을 int로 바꿔주면
만약 n이 123 이였다면 [1,2,3]이 된다.
그렇게 map을 사용한 후 sum을 사용하면 쉽게 구할 수 있다.
다른분들의 많은 답중에 개인적으로 가독성도 좋고 간단한거 같아서 가져왔다.
"""
