큰 수 만들기
문제 설명
어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.

예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.

문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

제한 조건
number는 2자리 이상, 1,000,000자리 이하인 숫자입니다.
k는 1 이상 number의 자릿수 미만인 자연수입니다.
입출력 예
number	k	return
"1924"	2	"94"
"1231234"	3	"3234"
"4177252841"	4	"775841"
===================================

def solution(number, k):
    answer = ''
    list_num = list(number)


    for i in range(len(number)-k):
        for j in range(len(number)-k+1):
 
            if list_num[j] == max(list_num):
             
                answer+=list_num[j]
             
                list_num.pop(j)
             
                break


    return answer

"""
다양한 방법으로 시도해 보았으나 테스트 케이스 1번에 대해서만 통과했다.
기본적인 로직은 전체 길이에서 K만큼을 뺀 수만큼 반복문을 수행 (NUMBER-K 만큼의 수가 결과로 나와야 하기에)
그다음  반복문을 한 번 더 수행한다. 
두번째 반복문은 number에서 -k+1 까지의 인덱스 중 가장 큰 수를 찾고
answer에 그 숫자를 추가하고 그숫자는 리스트에서 빼준다.
라는 식으로 접근을 했는데 여러군데 이상이 발생했다. 
다시한번 정리하며 풀기위해 시도한 이력을 남겨 놓는다."""   

def solution(number, k):
    answer = [] # asnwer을 list 형태로 받는다.

    for i in number:           # i에 넘버를 대입하여 반복문을 수행한다.
        if len(answer) == 0:   # 만약 answer이 빈 list이면 answer에 i를 대입하고 새로운 반복문을 수행한다.
            answer.append(i)
            continue
        if k > 0:               # 만약 k가 0보다 크다면
            while answer[-1] < i: # while문을 확인한다 answer의 마지막 요소가 i보다 작다면
                answer.pop()      # answer에서 마지막 요소를 빼주고
                k -= 1            # k에서 1을 빼준다 를 계속 반복
                if len(answer) == 0 or k <= 0: #그러다 answer이 빈 list가 되거나 k가 0보다 작거나 같을때
                    break          # break로 while문을 빠져나오고
        answer.append(i)           # answer에 i를 추가 해준다.

    answer = answer[:-k] if k > 0 else answer #만약 남은 k가 0qhek 크면 answer의 -k요소까지가 answer이 되고 아니면 answer이 답이된다.
    return ''.join(answer)

"""
내가 만든 코드로 계속 실행하다가 도저히 실마리를 잡지 못해서 결국 인터넷 검색을 했다.
결국 이번 알고리즘 스터디에서는 내가 푼 문제는 하나도 없었다.
문제의 이해도 이해지만 자료구조에 대한 개념이 좀 더 확실하게 잡혀 있어야 겠다는 생각을 했다.
스택 큐 문제로 풀면 된다는 이야기는 들었지만 구현을 할 수가 없었어서 계속 도전했었는데
오히려 독이 된것 같다.
코드를 읽고 분석했을땐 이해가 갔는데 만약 다시 문제가 주어진다면 내가 풀 수 있을까?
이렇게 코드를 구현 할 수 있을까? 라는 생각을 했다.
예외로 처리해야할 부분도 많았고 코드 진행 플로우 자체도 쉽지 않았기 때문이다."""