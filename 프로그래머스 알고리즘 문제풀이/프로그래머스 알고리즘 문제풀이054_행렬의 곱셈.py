행렬의 곱셈
문제 설명
2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.

제한 조건
행렬 arr1, arr2의 행과 열의 길이는 2 이상 100 이하입니다.
행렬 arr1, arr2의 원소는 -10 이상 20 이하인 자연수입니다.
곱할 수 있는 배열만 주어집니다.
입출력 예
arr1	arr2	return
[[1, 4], [3, 2], [4, 1]]	[[3, 3], [3, 3]]	[[15, 15], [15, 15], [15, 15]]
[[2, 3, 2], [4, 2, 4], [3, 1, 4]]	[[5, 4, 3], [2, 4, 1], [3, 1, 1]]	[[22, 22, 11], [36, 28, 18], [29, 20, 14]]

============================================

# 행렬의 곱셈
# arr1의 열 갯수 = arr2의 행 갯수
# answer는 arr1의 행 arr2의 열 갯수로 구성됨
# 반복문으로 행렬곱 수행
# 행렬의 반복문 for i in range(len(arr1)) - arr1의 행 길이 
# for j in range(len(arr1[i])) 이중 포문으로 열 뽑기 가능
# j로 arr1의 열이고 arr2의 행

def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    print(answer)
    
    for i in range(len(arr1)): #arr1 의 행
        for j in range(len(arr1[0])): # arr1의열 , arr2의 행
            for k in range(len(arr2[0])): # arr2의 열
                answer[i][k] += arr1[i][j] * arr2[j][k]
    
    return answer

"""
일단은 행렬의 곱셈에 대한 이해가 필요하다 
행렬의 곱셈은 a1의 열 갯수와 a2의 행 갯수가 동일해야 가능하다
그리고 answer은 a1의 행갯수 a2의 열갯수로 구성된다.
answer에 a1의 행 a2의 열 갯수만큼 0으로 채워주고
첫번째 반복문 i 에서 a1의 행갯수만큼 j에서는 a1의 열, a2의 행갯수 만큼 k에서는 a2의 열 갯수만큼 반복문을 수행해준다.
answer은 i행k열 이기때문에 저렇게 담아주고 행렬곱의 연산에 따라 += 을 붙여주었다
"""