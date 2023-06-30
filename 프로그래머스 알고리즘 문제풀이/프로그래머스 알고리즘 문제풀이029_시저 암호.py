시저 암호
문제 설명
어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"가 됩니다. 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

제한 조건
공백은 아무리 밀어도 공백입니다.
s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
s의 길이는 8000이하입니다.
n은 1 이상, 25이하인 자연수입니다.
입출력 예
s	n	result
"AB"	1	"BC"
"z"	1	"a"
"a B z"	4	"e F d"

=====================================================

# 65 ~ 90 A to Z
# 97 ~ 122 a to z
# ord("A") == 65
# chr(65)  == "A"
def solution(s, n):
    answer = ''
    for i in s:
        if 65 <= ord(i)+n <= 90 or 97 <= ord(i)+n <= 122:
            answer = answer +chr(ord(i)+n)
        elif 90 < ord(i)+n < 97:
            answer = answer + chr(ord(i)+n-26)
        elif ord(i)+n > 122:
            answer = answer + chr(ord(i)+n-26)
        elif ord(i) == 32:
            answer = answer + chr(ord(i))
            
    return answer

"""
코드 실행은 통과 했으나 제출시
61.5 이라는 점수로 실패했음
원인을 찾아야 할것 같음
"""

======================================================

# 65 ~ 90 A to Z
# 97 ~ 122 a to z
# ord("A") == 65
# chr(65)  == "A"
def solution(s, n):
    answer = ''
    for i in s: # s에 있는 문자열을 하나씩 i에 대입
        if 65 <= ord(i) <= 90: # 만약 i의 아스키 코드가 65~90 이면 그안에 조건문 확인
            if ord(i)+n > 90:  # 만약 i의 아스키 코드에 n만큼을 더해 줬을때 90보다 크면
                answer = answer + chr(ord(i)+n-26) # -26 을 해서 처음으로 돌아가게 ex) 91-26 = 65
            else: # 90보다 작다면
                answer = answer + chr(ord(i)+n) # 그냥 그대로 answer에 넣어주기
                
        elif 97 <= ord(i) <= 122: #위와 같은 flow
            if ord(i)+n > 122:
                answer = answer + chr(ord(i)+n-26)
            else:
                answer = answer + chr(ord(i)+n)
                
        elif ord(i) == 32: # 공백에 대한 아스키코드 공백은 밀어도 공백 이기에 그냥 넣어줌
            answer = answer + chr(ord(i))
            
    return answer

"""
문제를 찾기위해 여러 방면으로 시도해본 결과
X라는 문자를 25만큼 밀었을떄 q가 나왔다
+n을 기준으로 경계값을 설정 하였더니 그런 결과가 나온것 같다
그래서 첫 경계값은 +n을 하지 않고 그안에 if문을 추가해서 +n에 대한 경계값을 따로 설정했다.
"""