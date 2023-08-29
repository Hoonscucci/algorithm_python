의상
문제 설명
코니는 매일 다른 옷을 조합하여 입는것을 좋아합니다.

예를 들어 코니가 가진 옷이 아래와 같고, 오늘 코니가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면 다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야합니다.

종류	이름
얼굴	동그란 안경, 검정 선글라스
상의	파란색 티셔츠
하의	청바지
겉옷	긴 코트
코니는 각 종류별로 최대 1가지 의상만 착용할 수 있습니다. 예를 들어 위 예시의 경우 동그란 안경과 검정 선글라스를 동시에 착용할 수는 없습니다.
착용한 의상의 일부가 겹치더라도, 다른 의상이 겹치지 않거나, 혹은 의상을 추가로 더 착용한 경우에는 서로 다른 방법으로 옷을 착용한 것으로 계산합니다.
코니는 하루에 최소 한 개의 의상은 입습니다.
코니가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.

제한사항
clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
코니가 가진 의상의 수는 1개 이상 30개 이하입니다.
같은 이름을 가진 의상은 존재하지 않습니다.
clothes의 모든 원소는 문자열로 이루어져 있습니다.
모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.
입출력 예
clothes	return
[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]	5
[["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]	3
입출력 예 설명
예제 #1
headgear에 해당하는 의상이 yellow_hat, green_turban이고 eyewear에 해당하는 의상이 blue_sunglasses이므로 아래와 같이 5개의 조합이 가능합니다.

1. yellow_hat
2. blue_sunglasses
3. green_turban
4. yellow_hat + blue_sunglasses
5. green_turban + blue_sunglasses
예제 #2
face에 해당하는 의상이 crow_mask, blue_sunglasses, smoky_makeup이므로 아래와 같이 3개의 조합이 가능합니다.

1. crow_mask
2. blue_sunglasses
3. smoky_makeup

===================================================

# 옷 종류 별로 한개씩만 입어야함
# 선글라스가 두종류면 겹치면 안됨
# 최소 1종류의 의상은 걸쳐야함
# 해시 로 문제 탐색을 해야하는데 어떻게???...


def solution(clothes):
    hash = {}
    answer = 1
    
    for cloth in clothes:
        if cloth[1] not in hash.keys():
            hash[cloth[1]] = 1
        else:
            hash[cloth[1]] += 1
            
    print(hash.items())
    for key, value in hash.items():
        answer *= (value + 1)
    
    
    
    return answer-1

"""
못풓었다 답지를 보고 이해하려 노력했다.
일단 hash라는 빈 딕셔너리를 만들고 answer = 1 로 설정해준다.
반복문을 수행하여 clothes 의 요소들을 cloth에 하나씩 담아서 조건을 확인한다.
만약 cloth[1] 이 hash.keys() 안에 없다면 hash[cloth[1]] = 1 을 해준다
처음 hash는 빈 딕셔너리 이기에 if문이 수행되면 
1번 예를 기준으로 headgerar : 1 이 될 것이다.
그 다음 반복문을 수행하면 eyewear는 hash에 없기에 if 문이 수행되고
hash = headgear:1, eyewear:1 이 될 것이다.
마지막 반복문을 수행하면 else로 걸릴 것이고 그러면 
hash = headgear : 2 , eyewear : 1이 될 것이다.

그후 hash.items() 라고 해줘서 key, value 값을 구분 할 수 있게 해주고 반복문을 수행하여 key와 value로 받는다.
answer = answer * (value+1) 을 해준다
두가지 다 입거나 다 안입거나 이기에 value에 +1 을 해준다.
마지막 return문에 -1을 한 이유는 무조건 하나의 옷은 입어야 하기 때문에
아무 옷도 입지 않는 경우의 수 1개를 빼주는 것이다.


===============

두번째 해시 문제인데 접근 하는데서 부터 많이 막혔다. 전 문제를 보면서 풀어보려 했지만 
.keys나 .items 같은 개념이 친숙하지 않았고 
(value+1)*(value2+1) -1 같은 수학 식이 친숙하지 않아서 문제를 푸는데 지장이 있었다.
"""