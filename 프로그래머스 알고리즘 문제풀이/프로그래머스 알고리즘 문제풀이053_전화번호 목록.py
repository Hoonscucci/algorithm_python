전화번호 목록
문제 설명
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

구조대 : 119
박준영 : 97 674 223
지영석 : 11 9552 4421
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

제한 사항
phone_book의 길이는 1 이상 1,000,000 이하입니다.
각 전화번호의 길이는 1 이상 20 이하입니다.
같은 전화번호가 중복해서 들어있지 않습니다.
입출력 예제
phone_book	return
["119", "97674223", "1195524421"]	false
["123","456","789"]	true
["12","123","1235","567","88"]	false
입출력 예 설명
입출력 예 #1
앞에서 설명한 예와 같습니다.

입출력 예 #2
한 번호가 다른 번호의 접두사인 경우가 없으므로, 답은 true입니다.

입출력 예 #3
첫 번째 전화번호, “12”가 두 번째 전화번호 “123”의 접두사입니다. 따라서 답은 false입니다.

======================================

# 전화번호 목록
# 전화번호부 내에 있는 번호로 시작하는 번호가 있으면 false 리턴 없으면 true 리턴
# 반복문 수행해서 startswith 로 번호를 찾기? (길이가 가장 짧은 번호가 접두어인지 확인하면 될듯?)
# 근데 위에 해시라고 적혀있음 해시는 뭘까? 
# 일단 반복문 수행해서 답을 찾아보고 코드 실행 될때 해시 찾아서 해보기

def solution(phone_book):
    answer = True
    min_length = (min(phone_book,key=len))
    min_phone = []
    
    for phone in phone_book:
        if len(phone) == len(min_length):
            min_phone.append(phone)
            
    for phone in phone_book:
        for m_p in min_phone:
            
            if phone != m_p and phone.startswith(m_p):
                return False
    
    return answer

테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10.1MB)
테스트 7 〉	통과 (0.00ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10.1MB)
테스트 9 〉	통과 (0.00ms, 10.2MB)
테스트 10 〉 통과 (0.01ms, 10.1MB)
테스트 11 〉 통과 (0.01ms, 10.2MB)
테스트 12 〉 통과 (0.01ms, 10MB)
테스트 13 〉 통과 (0.01ms, 10.2MB)
테스트 14 〉 통과 (10.11ms, 10MB)
테스트 15 〉 실패 (20.09ms, 10.2MB)
테스트 16 〉 통과 (300.72ms, 10.3MB)
테스트 17 〉 통과 (428.48ms, 10.1MB)
테스트 18 〉 통과 (151.68ms, 10.4MB)
테스트 19 〉 실패 (202.70ms, 10.1MB)
테스트 20 〉 통과 (231.63ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (1.42ms, 10.9MB)
테스트 2 〉	통과 (1.95ms, 10.8MB)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실행 중단

=====================================

"""
코드 구현 로직간에 큰 실패가 없는듯 구현 되었다
그치만 중간에 실패가 있는거로 봐서는 어딘가 실패한 부분이 있다는거 같은데
예외에 대한 더 고민이 필요한거 같다
일단은 효율성 테스트에서도 실패한것 보면 역시 for말고 해시로 접근해서 새로운 
코드를 작성 해봐야겠다.
"""

===================

def solution(phone_book):
    
    for i in phone_book:
        temp=''
        for j in i:
            temp+=j
            if temp in phone_book and temp != i:
                return False
    return True

=========================================

def solution(phone_book):
    phone_book.sort()  # 전화번호를 사전순으로 정렬
    
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    
    return True

"""
hash를 이용한 방법은 아니지만 좀 충격받은 코드
문자열로 저장되어 있기에 sort 함수를 사용하였다.
ex) (["12","8","888","134","55","123555"]).sort = "12","123555","134","55","8","888" 이 된다.
이 구조를 이용해서 풀었는데 개인적인 입장에서는 신선한 충격 이였다. 앞으로 문제를 풀때 한가지만 생각하는게 아니라
고민의 영역을 확장할 필요가 있다고 느꼈다.
"""

========================================

def solution(phone_book):
    hash = {}
    
    for i in phone_book:
        hash[i]=1     # {'전화번호':1}로 담긴다.
        
    for i in phone_book:
        temp=''
        for j in i:
            temp+=j
            
            if temp in hash and temp != i:
                return False
    return True

"""
해시를 이용한 문제 풀이
hash 라는 딕셔너리를 만들고
반복문을 수행하여 phone_book의 요소들을 hash에 담아놓는다

그후 반복문을 수행하여 i에 phone_book의 요소를 담아 반복문을 수행해준다
j에는 i의 요소들을 담아 한번더 반복문을 수행해주면서 temp에 j를 추가해주면 if 문에 걸리는 지 확인해준다.
119,11923232을 예로 들면 첫 i에 들어갈 119 temp는 j를 계속해서 추가해주다 119가 되면 temp in hash가 되기에 temp가 i와 다른지 확인하지만 119로 같기에 넘어간다.
다음 11923232가 들어가서 반복문을 수행하다가 temp에 119가 들어가면 temp in hash가 되고 temp는 i와 다르기에 Fasle가 반환된다.
"""