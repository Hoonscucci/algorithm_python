약수의 개수와 덧셈
문제 설명
두 정수 left와 right가 매개변수로 주어집니다. left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ left ≤ right ≤ 1,000
입출력 예
left	right	result
13	17	43
24	27	52
입출력 예 설명
입출력 예 #1

다음 표는 13부터 17까지의 수들의 약수를 모두 나타낸 것입니다.
수	약수	약수의 개수
13	1, 13	2
14	1, 2, 7, 14	4
15	1, 3, 5, 15	4
16	1, 2, 4, 8, 16	5
17	1, 17	2
따라서, 13 + 14 + 15 - 16 + 17 = 43을 return 해야 합니다.

===============================================

def solution(left, right):
    answer = 0
    
    for i in range(left,right+1):
        cnt = 0
        
        for j in range(1,i+1):
            if i%j == 0:
                cnt +=1
        
        if cnt %2 == 0:
            answer+=i
        else:
            answer-=i
    return answer

"""
두정수 사이의 모든 수 들중 약수의 갯수가 짝수이면 + 홀수이면 -를 하라
바로 2중for문으로 문제를 풀기 시작했다.
left~right 까지 반복을 하고 
j에는 1~i 까지로 반복문을 수행하여 나누어 떨어지면 cnt+=1을 해준다.
글래서 하나의 i에 맞는 cnt를 얻고 첫번째 for문에 cnt=0을 두어서 cnt를 초기화 해주고
 cnt가 짝수이면 answer에 +를 해주고 홀수이면 -하게 해주었다.
"""