행렬의 덧셈
문제 설명
행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

제한 조건
행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.
입출력 예
arr1	arr2	return
[[1,2],[2,3]]	[[3,4],[5,6]]	[[4,6],[7,9]]
[[1],[2]]	[[3],[4]]	[[4],[6]]


=====================================

import numpy as np
def solution(arr1, arr2):
    A = np.array(arr1)
    B = np.array(arr2)
    answer = A+B
    return answer.tolist()

"""
numpy 힌트를 받았지만 풀 수 없었다.
개념을 좀 더 확립하고 문제를 반복하며 내껄로 만들어야 할것 같다.
"""

====================================

def solution(arr1, arr2):
    answer = []
    for a,b in zip(arr1,arr2):
        l=[]
        for x,y in zip(a,b):
            l.append(x+y)
        answer.append(l)
    return answer

"""
이중 for문으로 작성된 코드 
처음엔 이해가 가지 않았지만 하나하나 뜯어보며 확인 해보니 실마리가 잡힌것 같다.
2x2 행렬에 zip 함수 와 for문을 사용하면
첫번쨰 반복에서는
a = arr1의 0행 0,1열, b = arr2의 0행 0,1열이
두번째 반복에서는
a = arr1의 1행 0,1열, b = arr2의 1행 0,1열이 나온다
for x,y in zip(a,b) 는
x에 arr1의 0행 열, arr2의 0행 열 y에 arr1 의 0행 1열 , arr2의 0행 1열 이 입력된다.

2x2 행렬에 zip 과 for 가 어떻게 적용 되는지 알 수 있는 문제였다.
"""
