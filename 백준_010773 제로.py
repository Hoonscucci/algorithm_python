n = int(input())
answer = []

for i in range(n):
    arr = int(input())
    if arr > 0:
        answer.append(arr)
    elif arr == 0:
        answer.pop()

print(sum(answer))

"""
n = int(input()) - n에 사용자 지정 정수를 받게함
answer을 empty list로 만들어줌

for i in range(n)을 통해서 입력받은 정수만큼 for문을 돌림
for문에 연결된 int(input())으로 for문이 수행되면서 입력받는 숫자
if문을 통해 arr 이 0보다 크면 answer에 arr을 append하고
0이면 pop함수를 통해서 마지막 숫자를 꺼냄
마지막으로 모든 숫잠들의 합을 sum함수를 사용하여 표시함
"""





"""
왜 안됐는지 궁금함
"""
# def solution(arr,k):
#     answer = []

#     for i in range(k):
#         if arr[i] > 0:
#             answer.append(arr[i])
#         elif arr[i] == 0:
#             answer.pop()
#     return sum(answer)

# print(solution([1,2,0,4],4))