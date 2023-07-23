뒤에 있는 큰 수 찾기
문제 설명
정수로 이루어진 배열 numbers가 있습니다. 배열 의 각 원소들에 대해 자신보다 뒤에 있는 숫자 중에서 자신보다 크면서 가장 가까이 있는 수를 뒷 큰수라고 합니다.
정수 배열 numbers가 매개변수로 주어질 때, 모든 원소에 대한 뒷 큰수들을 차례로 담은 배열을 return 하도록 solution 함수를 완성해주세요. 단, 뒷 큰수가 존재하지 않는 원소는 -1을 담습니다.

제한사항
4 ≤ numbers의 길이 ≤ 1,000,000
1 ≤ numbers[i] ≤ 1,000,000
입출력 예
numbers	result
[2, 3, 3, 5]	[3, 5, 5, -1]
[9, 1, 5, 3, 6, 2]	[-1, 5, 6, 6, -1, -1]
입출력 예 설명
입출력 예 #1
2의 뒷 큰수는 3입니다. 첫 번째 3의 뒷 큰수는 5입니다. 두 번째 3 또한 마찬가지입니다. 5는 뒷 큰수가 없으므로 -1입니다. 위 수들을 차례대로 배열에 담으면 [3, 5, 5, -1]이 됩니다.

입출력 예 #2
9는 뒷 큰수가 없으므로 -1입니다. 1의 뒷 큰수는 5이며, 5와 3의 뒷 큰수는 6입니다. 6과 2는 뒷 큰수가 없으므로 -1입니다. 위 수들을 차례대로 배열에 담으면 [-1, 5, 6, 6, -1, -1]이 됩니다.

============================

# 이중 for문을사용?
# for i in range(len(numbers)) i번 반복 numbers의 길이만큼
#   for j in range(i,len(numbers)) i~ numbers의 크기까지 반복문 수행
# numbers[i]와 numbers[j]를 비교하면서 < 되면 answer.append(numbers[j]) break

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i,len(numbers)):
            if numbers[i] < numbers[j]:
                answer.append(numbers[j])
                break
        if numbers[i] >= numbers[j]:
            
            answer.append(-1)
                
    return answer

""" 
첫 시도 문장이다 2중 for문으로 작성을 했고
첫번째 반복문에서는 numbers의 길이만큼
두번째 반복문에서는 i~ 탐색을해서 
j번째 인덱스가 더 크면 answer에 numbers[j]를 append 해주고 break를 걸어준다.
모든 반복문을 수행하고 i번째 인덱스 모든 j번째 인덱스 보다 크면 -1을 추가
하려고 코드를 작성했는데 사실 이건 아닌거 같다.
그리고 마지막 4문제 에대허서 시간초과가 일어났다.
인덱스 구분도 확인해보고 2중for문 말고 새로운 방법을 찾아봐야겠다. 
"""

=================================================

def solution(numbers):
    stk = []
    answer = [-1]*len(numbers)
    for idx,num in enumerate(numbers):
        while stk and numbers[stack[-1]] < num:
            answer[stk.pop()] = num
        stk.append(idx)

    return answer

"""
풀지 못해서 결국 찾아봤다.
스택 개념으로 풀어야 하는 문제였다.
answer을 -1로 전부 다 바꿔놓고 stk라는 빈 list를 만들어 놓는다.
for 반복문을 통해서 idx와 num을 enumerate 함수를 사용하여 만들어 주었다.
stk가 비어있지않고 numbers[stk의 마지막요소] < num일때
answer[stack의 마지막요소] = num 으로 바꿔준다.
while문을 수행할 조건이 아니라면 stk에 idx를 append 해준다.

2중 for 문으로 풀수없는 문제여서 아쉽다
stack 개념이 완전히 성립되지 않은것 같다.
stack을 쓰면 될거같은데 코드 구현이 아직 어렵다.
"""
