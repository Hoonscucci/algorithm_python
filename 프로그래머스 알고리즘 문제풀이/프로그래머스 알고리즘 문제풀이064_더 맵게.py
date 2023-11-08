더 맵게
문제 설명
매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.

제한 사항
scoville의 길이는 2 이상 1,000,000 이하입니다.
K는 0 이상 1,000,000,000 이하입니다.
scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.
입출력 예
scoville	K	return
[1, 2, 3, 9, 10, 12]	7	2
입출력 예 설명
스코빌 지수가 1인 음식과 2인 음식을 섞으면 음식의 스코빌 지수가 아래와 같이 됩니다.
새로운 음식의 스코빌 지수 = 1 + (2 * 2) = 5
가진 음식의 스코빌 지수 = [5, 3, 9, 10, 12]

스코빌 지수가 3인 음식과 5인 음식을 섞으면 음식의 스코빌 지수가 아래와 같이 됩니다.
새로운 음식의 스코빌 지수 = 3 + (5 * 2) = 13
가진 음식의 스코빌 지수 = [13, 9, 10, 12]

모든 음식의 스코빌 지수가 7 이상이 되었고 이때 섞은 횟수는 2회입니다.

------------------------------------------------------

# 스코빌 지수 를 k 이상으로 만들기
# 가장 안매운 음식 스코빌 + (두번째로 안매운 음식 스코빌 * 2) = 섞은 음식
# 지수 k 이상으로 못 만들경우 -1 return
# 힙 안배운거 같은데...
# for 문으로 수행?

def solution(scoville, K):
    cnt = 0
    s = sorted(scoville)
    
    for i in s:
        if i < K:
            s.append(s[0]+s[1]*2)
            s.sort()
            s = s[2:]
            cnt += 1
            if s[0] > K:
                break
        if len(s) == 1 and s[0] < K:
            return -1 
    return cnt

"""
정확성에서 74.2 점을 맞고 효율성에서 0점을 맞았다
아무래도 힙으로 풀어야만 풀리는 문제인가보다 다시 시도해봐야겠다.
"""

---------------------------------------------------

import heapq # heapq 모듈 임포트 - 이거 없었으면 꽤나 어려웠을것 같다.

def solution(scoville, K):
    heap = [] 
    for i in scoville:
        heapq.heappush(heap, i) # heap 정렬 
        
    cnt = 0
    while heap[0] < K: # heap의 첫번째 인자값이 k보다 작을때 계속 수행
        heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)
        # heappop(heap)으로 가장 작은 인자값을 빼주고 그다음 작은 인자값을 * 2 해서 heappush로 넣어준다.
        # 힙정렬은 자동으로 작은수가 앞으로 나온다.
        cnt += 1
        
        if len(heap) == 1 and heap[0] < K: # heap의 인자값이 1개이고 그 인자값이 k보다 작으면 더이상 섞을 음식이 없음으  로 -1 을 리턴한다.
            return -1
    return cnt

"""
heap 정렬을 새로이 배우게 되었다.
자료구조를 보고 이걸 내가 이걸 써먹을수 있을까? 생각했는데
heapq 모듈을 임포트 해서 하니 사용 할 수 있을것 같았다.
선배 개발자들의 노력에 감사함을 느낀다."""