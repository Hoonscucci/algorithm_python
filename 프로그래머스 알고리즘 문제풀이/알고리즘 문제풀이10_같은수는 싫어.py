문제 설명
배열 arr가 주어집니다. 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다. 이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다. 단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다. 예를 들면,

arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.
arr = [4, 4, 4, 3, 3] 이면 [4, 3] 을 return 합니다.
배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요.

제한사항
배열 arr의 크기 : 1,000,000 이하의 자연수
배열 arr의 원소의 크기 : 0보다 크거나 같고 9보다 작거나 같은 정수
입출력 예
arr	answer
[1,1,3,3,0,1,1]	[1,3,0,1]
[4,4,4,3,3]	[4,3]

========================================

def solution(arr):
    answer = []
    count = 0
    arr.append(10)
    for i in arr:
        if arr[count-1]!=arr[count]:
            answer.append(i)
        count+=1
    answer.pop()

    return answer

"""
9이하의 정수를 포함하는 arr에서
10을 appned 하여 주고
for문과 if 문을 사용하여
arr의 요소를 인덱스하여 전에있는 수와 같지않으면 answer에 append 하게 하였다
마지막에 append 되어있는 10을 빼주기 위하여 pop함수를 사용하였다.
"""