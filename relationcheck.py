# 관계가 정의된 집합 = A, 동치인지 파악할 집합 = R(인자)

# 추이 - R 내부의 두 순서쌍을 비교하면서 앞 순서쌍의 치역과 뒤 순서쌍의 정의역이 같은 경우, 앞 순서쌍의 정의역과 뒤 순서쌍의 치역으로 이루어진 순서쌍이 존재하는지 파악
def check_transitive(R) :
  for pair1 in R : # R집합 안의 순서쌍1(튜플)에 대해 for문 반복
    for pair2 in R : # R집합 안의 순서쌍2(튜플)에 대해 for문 반복 ~ 이중 for문
      if pair1[1] == pair2[0] : # 순서쌍1의 치역(튜플의 1번째 인덱스)과 순서쌍2의 정의역(튜플의 0번째 인덱스)이 같은 경우
        if (pair1[0],pair2[1]) not in R : # 순서쌍1의 정의역(튜플의 0번째 인덱스)과 순서쌍2의 치역(튜플의 1번째 인덱스)을 순서쌍(튜플)으로 하는 값이 R에 없는 경우
          return False # False
  return True # 아닌 경우 True ~ for문 반복에 대한 순서쌍(튜플)의 존재 여부이므로 else 사용하지 않음


# 대칭 - R 내부의 순서쌍에 대해 정의역과 치역의 순서가 바뀐 순서쌍이 반드시 존재하는지 파악
def check_symmetric(R) :
  for pair in R : # R집합 안의 순서쌍(튜플)에 대해 for문 반복
    if (pair[1],pair[0]) not in R : # 순서쌍의 인덱스가 서로 바뀐 순서쌍(튜플)이 존재하지 않는 경우
      return False # False
  return True # 아닌 경우 True ~ for문 반복에 대한 순서쌍(튜플)의 존재 여부이므로 else 사용하지 않음


# 반사 - 정의된 집합 A에서의 모든 원소에 대한 순서쌍 존재하는지 파악
def check_reflexive(R) :
  for a in A : # A의 원소 하나씩 for문 반복
    if (a,a) not in R : # 튜플 (a,a)가 R집합의 원소에 없는 경우
      return False # False
  return True # 아닌 경우 True ~ for문 반복에 대한 순서쌍(튜플)의 존재 여부이므로 else 사용하지 않음


# 동치 - 추이, 대칭, 반사 함수 종합
def check_equivalance(R) :
  return check_transitive(R) and check_symmetric(R) and check_reflexive(R) # 각 추이, 대칭, 반사 함수가 전부 True인 경우 True로 판별
