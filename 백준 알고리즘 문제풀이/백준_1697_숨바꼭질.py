문제
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

예제 입력 1 
5 17
예제 출력 1 
4

========================================

from collections import deque

n = int(input())
k = int(input())
MAX = 100000
dist = [0]*(MAX+1)
    
def bfs():
    q = deque()
    q.append(n)
        
    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            break
                
        for j in (x-1, x+1, x*2):
            if 0<= j <= MAX and not dist[j]:
                dist[j] = dist[x] + 1
                q.append(j)



bfs()

"""
bfs 문제였다 bfs에 대하여 이해를 잘 못하겠다. 그나마 이 코드로 조금 감은 잡은거 같은데
그래도 아직 bfs만 만나면 막막하다...
또 이코드는 답으로 제출 되지 않았다

일단 코드 해석은 이와 같다
collection에 있는 deque를 불러오고
n과 k에 백준에서 주는 정수를 받는다
시간초과에 대비해서 MAX 값은 100000 으로 잡아둔다
방문한곳을 확인하기 위해 dist라는 리스트에 0을 MAX+1 한만큼 넣어준다

bfs 함수를 만든다
q는 deque로 만들어주고 n을 넣어준다
q가 정수일동안 반복한다
x 는 q의 첫번째 인자로 받아오고
x값이 동생의 위치 k 이면 dist[x]를 print 하게 했다 - 이로써 몇 초인지 확인 할 수 있다

if 문에 걸리지 않으면 반복문을 수행한다
j에 x-1 x+1 2*x를 담아서 if문을 수행한다
j가 범위 내에 있고 dist[j] 즉 방문한 노드가 아니라면
dist[j] = dist[x] +1 = dist[4,6,10] = dist[5] +1 로 1초 지났을때 갈 수 있는곳 이란 뜻
그후 q에 4,6,10을 append 해준다 그럼 q 4,6,10이 되고 다음 while 문에서 x는 4가된다 
위와같이 수행되고 10이 들어가면 j = 9,11,20 dist[9,11,20] 은 dist[10]+1 이니까 2가 된다 2초 지났을때 갈수 있는 위치라는 뜻
이렇게 로직이 반복되고 x가 k 가되면 dist[x]를 반환해서 몇 초 후 인지 답이 나온다.
"""

from collections import deque

n,k = map(int,input().split())
MAX = 100000
dist = [0]*(MAX+1)
    
def bfs():
    q = deque()

    q.append(n)
        
    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            break
                
        for j in (x-1, x+1, x*2):
            if 0<= j <= MAX and not dist[j]:
                dist[j] = dist[x] + 1
                q.append(j)
                    
bfs()

5 - 0

5 - 2

"""
n,k 받는 부분만 바꿔주니까 답지가 제출이 됐다 
도대체 첫번째꺼랑 다른게 뭔지 ㅜㅜ 왜 제출이 안되는지 
아... 애초에 5 17 이라고 입력을 줘서 그런가 보다
5
17 이 아니라 백준은 참 까다롭다 ㅜㅜ
bfs dfs 아직 많이 부족한것 같다 풀었던 문제를 다시 풀면서 로직이나 개념들을 
내것으로 만드는 시간이 필요할것같다.
"""