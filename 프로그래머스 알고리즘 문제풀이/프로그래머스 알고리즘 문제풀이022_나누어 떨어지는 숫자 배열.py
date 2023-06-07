나누어 떨어지는 숫자 배열
문제 설명
array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.

제한사항
arr은 자연수를 담은 배열입니다.
정수 i, j에 대해 i ≠ j 이면 arr[i] ≠ arr[j] 입니다.
divisor는 자연수입니다.
array는 길이 1 이상인 배열입니다.
입출력 예
arr	divisor	return
[5, 9, 7, 10]	5	[5, 10]
[2, 36, 1, 3]	1	[1, 2, 3, 36]
[3,2,6]	10	[-1]


===============================

def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])
        elif not answer:
            answer.append(-1)
    answer.sort()
    return answer

"""
코드실행 초기 3개는 통과했지만 
제출하니 정확도가 31점이 나왔다
틀린점을 찾아보고 수정해야함."""
===============================

def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])
    if not answer:
        answer.append(-1)
    answer.sort()
    return answer

"""
처음에는 elif를 걸어줬었는데 그렇게 되니 arr의 처음 숫자가 나누어 떨어지지 않을때 -1이 append되었다.
그런 문제를 해결하기 위해 -1을 append 해주는 if 문을 따로 작성해서 for if 문이 완전히 끝났을때
answer이 빈 list이면 -1을 append 하게 코드를 작성해주었다.
"""

=================================