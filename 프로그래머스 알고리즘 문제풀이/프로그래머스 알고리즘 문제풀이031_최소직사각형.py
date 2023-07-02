최소직사각형
문제 설명
명함 지갑을 만드는 회사에서 지갑의 크기를 정하려고 합니다. 다양한 모양과 크기의 명함들을 모두 수납할 수 있으면서, 작아서 들고 다니기 편한 지갑을 만들어야 합니다. 이러한 요건을 만족하는 지갑을 만들기 위해 디자인팀은 모든 명함의 가로 길이와 세로 길이를 조사했습니다.

아래 표는 4가지 명함의 가로 길이와 세로 길이를 나타냅니다.

명함 번호	가로 길이	세로 길이
1	60	50
2	30	70
3	60	30
4	80	40
가장 긴 가로 길이와 세로 길이가 각각 80, 70이기 때문에 80(가로) x 70(세로) 크기의 지갑을 만들면 모든 명함들을 수납할 수 있습니다. 하지만 2번 명함을 가로로 눕혀 수납한다면 80(가로) x 50(세로) 크기의 지갑으로 모든 명함들을 수납할 수 있습니다. 이때의 지갑 크기는 4000(=80 x 50)입니다.

모든 명함의 가로 길이와 세로 길이를 나타내는 2차원 배열 sizes가 매개변수로 주어집니다. 모든 명함을 수납할 수 있는 가장 작은 지갑을 만들 때, 지갑의 크기를 return 하도록 solution 함수를 완성해주세요.

제한사항
sizes의 길이는 1 이상 10,000 이하입니다.
sizes의 원소는 [w, h] 형식입니다.
w는 명함의 가로 길이를 나타냅니다.
h는 명함의 세로 길이를 나타냅니다.
w와 h는 1 이상 1,000 이하인 자연수입니다.
입출력 예
sizes	result
[[60, 50], [30, 70], [60, 30], [80, 40]]	4000
[[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]	120
[[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]	133

========================================================================

def solution(sizes):
    list_max = []                           # h와 w 중 큰것만 모아놓은 리스트
    list_min = []                           # h와 w 중 작은것만 모아놓은 리스트
    answer = 0                              
    for h,w in sizes:                       # 2차원 배열 sizes를 h,w에 넣어주면서 반복문을 돌림 
        list_max.append(max(h,w))           # h,w중 큰것을 list_max에 넣어준다
        list_min.append(min(h,w))           # h,w중 작은것을 list_min에 넣어준다
    answer = max(list_max) * max(list_min)  # list_max중 max와 list_min중 max를 곱해준다.
    return answer

"""
길이와 높이중 큰것들을 모아서 그중 가장 큰것과
길이와 높이중 작은것들을 모아서 그중 가장 큰것을 곱하면
문제를 풀 수 있을것 같아 작성 해보았다.
"""