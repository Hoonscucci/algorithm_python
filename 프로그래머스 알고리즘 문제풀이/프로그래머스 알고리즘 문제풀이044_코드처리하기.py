코드 처리하기
문제 설명
문자열 code가 주어집니다.
code를 앞에서부터 읽으면서 만약 문자가 "1"이면 mode를 바꿉니다. mode에 따라 code를 읽어가면서 문자열 ret을 만들어냅니다.

mode는 0과 1이 있으며, idx를 0 부터 code의 길이 - 1 까지 1씩 키워나가면서 code[idx]의 값에 따라 다음과 같이 행동합니다.

mode가 0일 때
code[idx]가 "1"이 아니면 idx가 짝수일 때만 ret의 맨 뒤에 code[idx]를 추가합니다.
code[idx]가 "1"이면 mode를 0에서 1로 바꿉니다.
mode가 1일 때
code[idx]가 "1"이 아니면 idx가 홀수일 때만 ret의 맨 뒤에 code[idx]를 추가합니다.
code[idx]가 "1"이면 mode를 1에서 0으로 바꿉니다.
문자열 code를 통해 만들어진 문자열 ret를 return 하는 solution 함수를 완성해 주세요.

단, 시작할 때 mode는 0이며, return 하려는 ret가 만약 빈 문자열이라면 대신 "EMPTY"를 return 합니다.

제한사항
1 ≤ code의 길이 ≤ 100,000
code는 알파벳 소문자 또는 "1"로 이루어진 문자열입니다.
입출력 예
code	result
"abc1abc1abc"	"acbac"

=============================================

# 코드 처리하기
# 초기 mode 0으로 설정
# for 반복문 수행
# if mode =="0":
#   if code[i] == "1"
#       mode = "1"
#   else:   
#       if i%2 ==0: answer+=code[i]
# else:
#    if code[i] =="1":  
#       mode  = "0"
#    else:
#       if i%2==1: answer +=code[i]

# "1"이 등장하고나서 인덱스 번호는 1이후부터 초기화

def solution(code):
    answer = ''         
    mode = "0"                      # 초기모드 설정
    for i in range(len(code)):      # 반복문수행
        if mode == "0":             # mode가 0일경우
            if code[i] == "1":      # code[i]가 "1"이면
                mode ="1"           # mode를 1로 바꿔준다
                
            else:                   # code[i]가 "1"이 아닐경우
                if i%2== 0:         # 만약 i가 짝수이면? 0도 적용됨
                    answer+=code[i] # answer에 code[i]를 더해주기
        else:                       # mode가 1일경우
            if code[i] == "1":      # code[i]가 1이면
                mode = "0"          # mode를 0으로 바꿔준다
                
            else:                   # code[i]가 1이 아닐경우
                if i%2 == 1:        # 홀수번째 인덱스를
                    answer+=code[i] # answer에 넣어준다.
    answer = answer if len(answer) > 0 else "EMPTY" # answer이 빈상태면 EMPTY를 반환한다.
    return answer 

"""
프로그래머스 lv 0 문제라서 쉽게 생각했는데
lv1 보통급으로 느껴졌다... 기본기가 많이 부족한가보다.
이번에도 문제를 먼저 비판적으로 시뮬레이션을 돌렸는데
그래도 lv0 문제라서 그런지 꼬아진 부분은 없었어서 
그나마 수월하게 풀렸다.
전체 코드 구성은 
mode가 0일때와 1일때로 구분해서 수행하고
code의 i번째 인덱스의 상태에 따른 구분을 이용했다.
"""