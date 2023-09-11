JadenCase 문자열 만들기
문제 설명
JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됩니다. (첫 번째 입출력 예 참고)
문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

제한 조건
s는 길이 1 이상 200 이하인 문자열입니다.
s는 알파벳과 숫자, 공백문자(" ")로 이루어져 있습니다.
숫자는 단어의 첫 문자로만 나옵니다.
숫자로만 이루어진 단어는 없습니다.
공백문자가 연속해서 나올 수 있습니다.
입출력 예
s	return
"3people unFollowed me"	"3people Unfollowed Me"
"for the last week"	"For The Last Week"

========================================

def solution(s):
    answer = ''
    s_split = s.split(' ')
    for i in s_split:
        for j,k in enumerate(i):
            if j == 0:
                answer += k.upper()
            else:
                answer += k.lower()
        answer += ' '
    return answer[:-1]

"""
이전에 풀었던 이상한 문자 만들기 복습 버전으로 문제를 풀어봤다.
풀이 방식은 똑같았는데 이번엔 enumerate 함수를 사용하여 인덱스 번호와 문자 그대로를 받아왔다.
너무 쉽게 풀리긴 했지만 복습 느낌으로 나쁘지 않았다.
"""