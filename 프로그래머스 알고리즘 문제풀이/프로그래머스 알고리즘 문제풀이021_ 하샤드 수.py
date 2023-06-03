하샤드 수
문제 설명
양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.

제한 조건
x는 1 이상, 10000 이하인 정수입니다.
입출력 예
x	return
10	true
12	true
11	false
13	false

=======================================

def solution(x):
    str_x = str(x)
    ls = []
    for i in range(len(str_x)):
        ls.append(str_x[i])
    x_sum = sum(map(int, ls))
    if x%x_sum == 0:
        answer= True
    else:
        answer = False
    return answer

"""
x를 str로 바꿔 주고 빈 list를 만들어준다
for문을 돌려 i에 str의 길이를 range 해주고
스트링의 i번째 인덱스를 list에 넣어줍니다.
x_sum 은 그 리스트를 정수형으로 바꿔주고 합쳐주고
if 문에 정수x를 x_sum으로 나는 나머지가 0이면 True
아니면 False를 반환한다.
"""
=======================================

def Harshad(n):
    # n은 하샤드 수 인가요?
    st = str(n)
    a = 0
    for i in range(len(st)):
        a += int(st[i])

    return True if n%a == 0 else False

"""
결은 비슷했는데 리스트를 활용한게 아니라 a+= 이라는 식으로 접근했다.
덕분에 x_sum을 따로 계산하는 식을 만들지 않아도 되는 편리함이 있다.
또 return문에 바로 True와 if를 달아줘서 코드가 훨씬 더 간결하게 표현할수 있었다.
"""