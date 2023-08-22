스킬트리
문제 설명
선행 스킬이란 어떤 스킬을 배우기 전에 먼저 배워야 하는 스킬을 뜻합니다.

예를 들어 선행 스킬 순서가 스파크 → 라이트닝 볼트 → 썬더일때, 썬더를 배우려면 먼저 라이트닝 볼트를 배워야 하고, 라이트닝 볼트를 배우려면 먼저 스파크를 배워야 합니다.

위 순서에 없는 다른 스킬(힐링 등)은 순서에 상관없이 배울 수 있습니다. 따라서 스파크 → 힐링 → 라이트닝 볼트 → 썬더와 같은 스킬트리는 가능하지만, 썬더 → 스파크나 라이트닝 볼트 → 스파크 → 힐링 → 썬더와 같은 스킬트리는 불가능합니다.

선행 스킬 순서 skill과 유저들이 만든 스킬트리1를 담은 배열 skill_trees가 매개변수로 주어질 때, 가능한 스킬트리 개수를 return 하는 solution 함수를 작성해주세요.

제한 조건
스킬은 알파벳 대문자로 표기하며, 모든 문자열은 알파벳 대문자로만 이루어져 있습니다.
스킬 순서와 스킬트리는 문자열로 표기합니다.
예를 들어, C → B → D 라면 "CBD"로 표기합니다
선행 스킬 순서 skill의 길이는 1 이상 26 이하이며, 스킬은 중복해 주어지지 않습니다.
skill_trees는 길이 1 이상 20 이하인 배열입니다.
skill_trees의 원소는 스킬을 나타내는 문자열입니다.
skill_trees의 원소는 길이가 2 이상 26 이하인 문자열이며, 스킬이 중복해 주어지지 않습니다.
입출력 예
skill	skill_trees	return
"CBD"	["BACDE", "CBADF", "AECB", "BDA"]	2
입출력 예 설명
"BACDE": B 스킬을 배우기 전에 C 스킬을 먼저 배워야 합니다. 불가능한 스킬트립니다.
"CBADF": 가능한 스킬트리입니다.
"AECB": 가능한 스킬트리입니다.
"BDA": B 스킬을 배우기 전에 C 스킬을 먼저 배워야 합니다. 불가능한 스킬트리입니다.

===============================================

# 스킬트리
# skill을 찍을때 순서가 들어 있음
# ex) CBD이면 C를 찍어야 B를 찍을 수 있음
# skill 순서만 변하지 않으면 중간에 skill 이외의 스킬을 찍을 수 있음
# ex) CAFBD you know?
# skill_trees에는 스킬 트리 들이 들어있고 이걸 skill과 비교하여 사용할 수 있는 스킬 수만 리턴
# 이중 반복문 + find? skill_trees 만큼 반복하여 스킬 트리 하나하니씩 탐샘
# skill만큼 반복문 수행 find(i) 
# 로 로직을 작성해보려 했지만 다짜고짜 for를 쓰기보다는 자료구조를 이해하고 문제가 원하는 방식을 생각해 봐야한다.
# 스택/큐로 구현을 해볼수도 있고
# skill_trees에서 skill에 없는 알파벳을 제거하고 skill과 비교해서 답을 찾을 수 도 있을것 같다.

def solution(skill, skill_trees):
    answer = len(skill_trees)
    for skill_tree in skill_trees:
        skill_tree_my = ''.join(s for s in skill_tree if s in skill)
        
        # print(skill_tree_my)
        for i in range(len(skill_tree_my)):
            if skill[i] != skill_tree_my[i]:
                answer-=1
                break
        
        
   
    return answer

==================================================

"""
이중 for문 + find 함수로 답을 찾으려고 했는데
자료구조 공부도 했으니 다른 방식으로도 풀어보라는 스터디장의 말에
스택과 큐로 구현 하려 했지만 str형태 이기에 번거 로울것 같아서 다른 방식으로 풀어 보았다.
처음 answer에 skill_trees 만큼의 길이를 넣어주고
첫 반복문에 skill_trees로 돌려주고
skill_tree_my에 skill_tree를 반복문을 수행하여 skill내에 있으면 넣어 주었다.
ex) skill_tree 가 BCDAF이면 s에 B,C,D,A,F를 순서대로 넣어서 skill에 있는지 확인 하고 있으면 넣어주기
그렇게 skill_tree_my 가 완성되면
skill_tree_my의 길이만큼 반복문을 수행한다 (BD) 이렇게 2개만 들어 가 있을수도 있어서
skill[i]가 skill_tree_my[i]와 다르면 answer 에서 1을 빼주고 반복문을 종료한 후 처음 반복문으로 돌아가서 이 로직을 반복한다.
"""