# 트럭 무게에 제한이 없을 때 동물 태우는 경우의 수 구하기

# 조합(Combination) : 순서를 고려하지 않고 특정 개수의 원소를 선택한다.(<> 순열 Permutation)
# Python 에서는 조합을 구하는 데 itertools 모듈의 combinations 함수를 사용한다.
# itertools.combinations(iterable, r) 함수
# 주어진 iterable에서 r개의 원소를 선택한 모든 조합을 반환한다. 반환값은 튜플
from itertools import combinations

# 동물 목록
animals = ["코끼리", "하마", "기린", "코뿔소", "호랑이", "사자", "얼룩말"]

# 경우의 수 저장 변수
total_cases = 0

print(" << 각 경우의 동물 조합 >>")
for i in range(len(animals) + 1): # 0마리 태우기 ~ 7마리 태우기
    cases = list(combinations(animals, i)) # 튜플 반환값을 리스트로 변환
    total_cases += len(cases)
    # print("%d마리 태우는 경우 : %d 가지" % (i, len(cases)))
    print(f"{i}마리 태우는 경우 : {len(cases)} 가지")

print(f"총 경우의 수 : {total_cases}가지지")

