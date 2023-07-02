수 찾기

문제
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

출력
M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

예제 입력 1 
5
4 1 5 2 3
5
1 3 7 9 5
예제 출력 1 
1
1
0
0
1

===========================================================

n = int(input())                            # 정수를 받아서 n에 넣는다
n_list = list(map(int, input().split()))    # n_list에 입력받는 숫자로 list를 만든다
m = int(input())                            # 정수를 받아서 m에 넣는더
m_list = list(map(int, input().split()))    # m_list에 입력 받는 숫자로 list를 만든다
n_list.sort()                               # sort를 하는 이유는 이분탐색을 해야하기에 순서대로 정렬을 해야 기준점을 정할 수 있음
    
def search(array, target):                  # 
    left = 0                                # start
    right = n-1                             # end 
       
    while left <= right:                    # 시작하는 부분이 끝보다 작거나 같을때 까지
        mid = (left+right)//2               # mid 는 시작과 끝의 중간부분
        
        if array[mid] == target:            # array(n_list)의 [mid] 인덱스가 target이면
            return 1                        # 1을 return
        elif array[mid] > target:           # elif array(n_list)의 [mid] 인덱스가 target보다 크면 mid 이후의 데이터는 다 버려도 되기에
            right = mid-1                   # end 부분을 mid-1로 해준다
        elif array[mid] < target:           # elif array(n_list)의 [mid] 인덱스가 target보다 작다면 mid 이전의 데이터는 다 버려도 되기에
            left = mid+1                    # start 부분을 mid + 1 로 해준다.
    return 0                                #

for i in m_list:
    print(search(n_list, i))

"""
백준 문제는 적응이 안되는것 같다
그래서 답을 좀 찾아 봤다...
"""