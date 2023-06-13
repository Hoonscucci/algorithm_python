완주하지 못한 선수
문제 설명
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

제한사항
마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
completion의 길이는 participant의 길이보다 1 작습니다.
참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
참가자 중에는 동명이인이 있을 수 있습니다.
입출력 예
participant	completion	return
["leo", "kiki", "eden"]	["eden", "kiki"]	"leo"
["marina", "josipa", "nikola", "vinko", "filipa"]	["josipa", "filipa", "marina", "nikola"]	"vinko"
["mislav", "stanko", "mislav", "ana"]	["stanko", "ana", "mislav"]	"misl

=============================================

def solution(participant, completion):
    answer = ''
    participant.sort()  #오름차순정렬
    completion.sort()   #오름차순정렬
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer+=participant[i] #서로 맞지 않으면 answer에 추가
            break # 한명만 실패니까 break
    if not answer: #for문이 종료 되었을때 answer이 빈 리스트이면 participant[-1]이 정답
        answer = participant[-1] # participant가 completion보다 1명 더 많기 때문에

"""
두 리스트를 sort하여 정렬하여 주었다(인덱스 번호로 구별하기위해)
for문을 사용하여 completion의 길이만큼 i에 넣어줬다.
두 리스트에 같은 인덱스 번호를 주고 다를경우 answer에 추가하고 break를 했다.
(break 안할시 다른 사람들도 정답에 추가되기 때문에)
participant 리스트가 competion리스트 보다 1명이 많기 때문에
for문을 다 돌고도 answer이 비어있다면 answer = participant의 마지막 요소가 나오게 했다.
"""
=============================================

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant)-1]

"""
if 다음에 return을 사용하여 break 없이 코드가 사용되게 하였고
마지막 return에 바로 paricipant의 마지막 인덱스를 걸어놔서
if문을 사용하지 않아도 되게 하였다
for문을 다 돌아도 return이 되지 않으면 마지막 return문이 사용됨을 알게 되었다.
"""
=============================================

def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
 
    return participant[-1]

"""
마지막 return 문을 줄여봤다.
"""