# 3진법으로 만들고 뒤집어서 다시 10진법으로
# 3진법으로 만드는 메소드는 따로 없는것 같음
# k진법 만든는 코드 n,mode = divmod(n,k) 반복
# divmod는 나머지와 몫을 한번에 보여주는 코드임

def solution(n):
    answer = 0
    code = ''
    
    while n > 0:
        n, mod = divmod(n,3)
        code += str(mod)
        # code를 거꾸로 읽으면 그게 3진법
    # print(code) = 0021
    
    answer = int(code,3)
    # n진법을 10진법으로 바꾸는 방법 3의 위치에 n을 넣어주면 됨
    
    return answer