이상한 문자 만들기
문제 설명
문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 
각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

제한 사항
문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.
입출력 예
s	return
"try hello world"	"TrY HeLlO WoRlD"
입출력 예 설명
"try hello world"는 세 단어 "try", "hello", "world"로 구성되어 있습니다. 각 단어의 짝수번째 문자를 대문자로, 
홀수번째 문자를 소문자로 바꾸면 "TrY", "HeLlO", "WoRlD"입니다. 따라서 "TrY HeLlO WoRlD" 를 리턴합니다.


=================================================================
# 단어 별로 짝수번째 대문자 홀수번째 소문자
# split을 써보면?

def solution(s):
    answer = ''
    split_s = s.split()
    for i in split_s:
        for j in range(len(i)):
            if j%2 ==0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += " "
        
    return answer.rstrip(" ")

"""
split 함수를 사용하여 일단 문자별로 나눠주고
2번의 반복문을 수행해서 문자별 짝수는 upper메소르도 대문자,
홀수는 lower 함수로 소문자로 만들어줘서 answer에 넣어주고 
2번째 반복문이 끝나면 answer += " "로 하여 문자간 공백을 만들어준다.
마지막으로 answer.rstrip을 사용하여 마지막에 있는 공백을 없앴다.

코드는 통과됐으나 제출후 채점 했을때 31점을 맞았다.
어딘가 문젝 발생했나보다.
"""

=========================================

# 단어 별로 짝수번째 대문자 홀수번째 소문자
# split을 써보면?

def solution(s):
    answer = ''
    split_s = s.split(' ')
    print(split_s)
    for i in split_s:
        for j in range(len(i)):
            if j%2 ==0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += " "
        
    return answer[:-1]

"""
2가지가 문제였다.
하나는 split()을 split(' ')로 공백 문자를 지정해줬고
answer.rstrip(" ")가 아닌 answer[:-1]로 바꿔 주었더니 통과 되었다.
정확히 저기에서 어떤 부분이 문제인지는 정확하게 인지 하지 못했다.
"""