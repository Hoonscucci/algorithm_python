# # l길이의 문자열 l_str에서 2번이상 등장하는 부분 문자열중 가장 긴것!
# # hash & count? hash 사용하여 각 갯수에 맵핑 시키면?

# L = int(input())
# l_str = str(input())

# hash = {}

# for l_st in l_str:
#     if l_st not in hash:
#         hash[l_st] = 1
#     else:
#         hash[l_st] += 1
      
# if max(hash.values()) > 1:
#     print(max(hash.values()))
# else:
#     print(0)


"""
문제를 잘 못 이해했다. 문자열 중에서 반복되는 문자 수의 갯수를 가져오라는 말인줄 알았는데
반복되는 부분 문자열의 갯수중 가장 긴것을 찾으라는 것 이였다.
문제를 다시 풀어야 한다.
"""

========================================

# 반복되는 문자열 중에 가장 긴것을 고르라고 했음
# 그러면 문자열 하나씩 hash에 담는다 다만 2번이상 등장해야 하기에 전체 길이를 반으로 반으로 나눈 몫만큼만 수행해도 될듯?
# 이중포문으로 해볼까?
# i번 j번 반복해서 l_str[i]가 hash에 없으면 =1 해주고 j반복문으로 i+j가 hash에 없으면 +1 있으면 +=1

======================================

L = int(input())
l_str = str(input())

answer = 0
hash = {}

for i in range(len(l_str)):
    l_str2 = ''
    if l_str[i] not in hash:
        hash[l_str[i]] = 1
        l_str2 += l_str[i]
        l_str3 = l_str[i+1:]
        for j in l_str3:
            l_str2 += j
            if l_str2 not in hash:
                hash[l_str2] = 1
            else:
                hash[l_str2] += 1
    else:
        hash[l_str[i]] = 1
        l_str2 += l_str[i]
        l_str3 = l_str[i+1:]
        
        for j in l_str3:
            l_str2 += j
            if l_str2 not in hash:
                hash[l_str2] = 1
            else:
                hash[l_str2] += 1
                
ans = max(hash.values())
if ans == 1:
    print(0)
else:
    for k,v in hash.items():
        if v == ans:
            answer = max(answer,len(k))
    print(answer)


===============================================

L = int(input())
l_str = str(input())

answer = 0
hash = {}

for i in range(len(l_str)):
    for j in range(i, i+(len(l_str))/2):
        l_str2 = l_str[i:j+1]  # l_str[i]부터 l_str[j]까지의 부분 문자열 생성
        if l_str2 not in hash:
            hash[l_str2] = 1
        else:
            hash[l_str2] += 1
                
ans = max(hash.values())
if ans == 1:
    print(0)
else:
    for k,v in hash.items():
        if v == ans:
            answer = max(answer,len(k))
    print(answer)

"""
다시 풀어본 문제에서 시간초과가 나왔다 아무래도 이중포문으로 인한 시간 초과 현상인거 같은데
시간을 줄일수있는 방법은 없을까?
그리고 values의 최댓값을 찾앗는데 그럴 필요가 없고 k를 확인해야 했다.
아 도저히 모르겠다... 배추!
"""

