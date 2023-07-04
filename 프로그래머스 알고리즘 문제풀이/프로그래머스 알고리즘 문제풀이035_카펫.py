카펫
문제 설명
Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.

carpet.png

Leo는 집으로 돌아와서 아까 본 카펫의 노란색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.

Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한사항
갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.
카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.
입출력 예
brown	yellow	return
10	2	[4, 3]
8	1	[3, 3]
24	24	[8, 6]

========================================================

# 갈색카펫은 외부로 노란색 카펫은 내부로
# total = brown + yellow
# brown = 2return[0] + 2return[1] -4
# return[0] * return[1] = total
# brown 말고 yellow를 기준으로?
# yellow = return[0]-2 * return[1]-2
# return[0]은 return[1]보다 크거나 같다

def solution(brown, yellow):               
    answer = []   
    total = brown+yellow                    # 전체 타일수는 = brown + yellow이다
    for i in range(brown):                  # brown의 길이만큼 반복문을 수행하여 i에 대입한다.
        for j in range(brown):              # 똑같이 반복해 j에 대입한다.
                                            # brown 길이만큼 반복문을 수행한 이유는 위에 brown과 yellow를 구하는 식을 적어놓았는데 이식을 토대로 값을 구하기 위해서임
            if 2*i + 2*j -4 == brown:       # 위에 식에 대입해 브라운이 되는 수 i와 j를 구한다.
                if (i-2)*(j-2) == yellow:   # 그 값들중 yellow를 구하는 식에 대입했을떄 남는 숫자들
                    if i>=j:                # 그 값들 중에서 i가 j보다 크거나 같은값이 있을때
                        answer.append(i)    # answer에 값을 추가 해준다.
                        answer.append(j)    
            
    return answer

"""
확실히 문제를 풀기전에 요구하는바와
내가 풀어야할 코드를 상단에 정리해 놓으니
헤메는 일이 적어졌다.
정답 제출에는 성공했지만 시간이 너무 오래 걸렸다.
"""