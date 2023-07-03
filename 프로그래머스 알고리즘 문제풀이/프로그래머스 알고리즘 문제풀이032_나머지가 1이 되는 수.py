나머지가 1이 되는 수 찾기
문제 설명
자연수 n이 매개변수로 주어집니다. n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 완성해주세요. 답이 항상 존재함은 증명될 수 있습니다.

제한사항
3 ≤ n ≤ 1,000,000
입출력 예
n	result
10	3
12	11

===============================

def solution(n):
    answer = 0
    for x in range(1,n):
        if n % x ==1:
            answer = x
            break
    return answer

"""
반복문을 사용했다.
x에 1~n까지 대입하면서
만약 n을 x로 나눈 나머지가 1이면 anser에 x 를 대입하고
가장 작은 수 이기에 break를 걸어줬다.
"""