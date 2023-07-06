제일 작은 수 제거하기
문제 설명
정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요. 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요. 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.

제한 조건
arr은 길이 1 이상인 배열입니다.
인덱스 i, j에 대해 i ≠ j이면 arr[i] ≠ arr[j] 입니다.
입출력 예
arr	return
[4,3,2,1]	[4,3,2]
[10]	[-1]

====================================================

def solution(arr):
    answer = []
    arr.sort(reverse = True)
    if not arr:
        answer.append(-1)
    else:
        arr.pop()
        if not arr:
            answer.append(-1)
        else:
            return arr
    return answer

"""
테스트는 통과하는데 체점에서 0점을 맞는다...
코드구성은 다음과 같다
만약 arr이 빈 리스트이면 answer에 -1을 추가하고
아니라면 arr에서 마지막수를 빼준다
거기서 다시 arr이 빈 리스트이면 answer에 -1을 추가하고
아니라면 arr을 return한다"""

==================================================

def solution(arr):
    answer = []
    arr.remove(min(arr))
    if not arr:
        return [-1]
    return arr

"""
정렬 문제가 아니라 최소값만을 제거 했어야 했다.
그래서 arr에서 최솟값 min을 remove 해주고
remove한 arr의 리스트가 비어 있으면 -1을 리턴하게 했다.
테스트케이스에 속아서 답을 잘못 도출해냈다.
"""