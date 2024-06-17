## realationcheck

이 모듈은 이산수학 관계의 동치와 관련한 함수를 불러줍니다. 

- 'check_transitive(R)' : 관계 R이 추이적 성질을 띠는지 True/False로 출력해주는 함수
- 'check_symmetric(R)' : 관계 R이 대칭적 성질을 띠는지 True/False로 출력해주는 함수
- 'check_reflexive(R)' : 관계 R이 반사적 성질을 띠는지 True/False로 출력해주는 함수
- 'check_equivalance(R)' : 관계 R이 동치 관계인지 True/False로 출력해주는 함수

## How to download

모듈을 다운 받기 위해 

## How to use



## Detail

모듈 속 함수에 관한 내용입니다.

check_transitive(R)

> 추이성 판별을 위해 관계 R의 비교할 첫 순서쌍의 1 인덱스와 두번째 순서쌍의 0 인덱스를 각각 비교하여 관계 R에 첫번째 순서쌍의 0 인덱스와, 두번째 순서쌍의 1 인덱스를 순서쌍으로 가진 원소가 있는지 파악

> for 문을 이용하여 관계 R의 순서쌍 pair1과 pair2를 반복하고 if 문을 이용하여 pair1[1] == pair2[0] 즉, 두 순서쌍을 비교할 때 첫번째 순서쌍의 치역과 두번째 순서쌍의 정의역이 같은 경우 (pair1[0],pair2[1]) 순서쌍이 관계 R에 존재하는지 파악하여 True/False 판별


check_symmetric(R)

> 대칭성 판별을 위해 관계 R에 속한 순서쌍의 인덱스 0과 1이 서로 바뀐 순서쌍도 관계 R에 속해있는지 파악

> for 문을 이용하여 관계 R의 순서쌍 pair를 반복하고 if 문을 이용하여 (pair[1],pair[0])과 같은 순서쌍이 관계 R에 존재하는지 파악하여 True/False 판별


check_reflexive(R)

> 반사성 판별을 위해 집합 A에 관한 관계 R에서 집합 A의 모든 원소에 대하여 정의역과 치역이 동일한 순서쌍이 모두 존재하는지 파악

> for 문을 이용하여 집합 A에 관한 원소 a를 반복하고 if 문을 이용하여 (a,a) 순서쌍이 관계 R에 존재하는지 파악하여 True/False 판별


check_equivalance(R)

> 관계 R이 동치 관계인지 파악하기 위해 추이성, 대칭성, 반사성을 모두 가지는지 파악

> True/Fasle로 판별되는 위의 세 함수를 이용하여 and 연산자를 이용해 모두 True인 경우 True가 출력되도록 True/False 판별
