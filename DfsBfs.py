# 대표적인 탐색 알고리즘
# 자료구조: 데이터를 표현하고 관리하고 처리하기 위한 구조
# 삽입 Push, 삭제 Pop
# 스택: FILO/LIFO
# 큐: FIFO
# OverFlow와 UnderFlow 고려 필요.

# # Stack
# stack = []
# stack.append(3)
# stack.pop()
#
# # Queue
# from collections import deque
# queue = deque()
#
# queue.append(5)
# queue.popleft()
# #queue list변환
# list(queue)

#재귀함수: 자기자신을 다시 호출하는 함수. 반드시 종료조건을 명시할 것
# def recursive_function():
#     print('재귀함수 호출')
#     recursive_function()
## recursive_function() # 실행 시 무한호출

# def recursive_function(i):
#     if(i == 100):
#         return
#     print(i+1, '번째 재귀함수 호출')
#     recursive_function(i+1)
#     print(i + 1, '번째 재귀함수 종료')
#
# recursive_function(1)

#재귀함수는 팩토리얼 문제에 활용됨

#반복적으로 구현한 n!
# def factorial_iterative(n):
#     result = 1
#     #1부터 n까지의 수를 차례대로 곱하기
#     for i in range(1, n+1):
#         result *= i
#     return result
# #재귀적으로 구현한 n!
# def factorial_recursive(n):
#     if(n<=1):
#         return 1
#     # n! = n * (n -1)! 코드 작성
#     return n * factorial_recursive(n-1)
#
# # 두 방식 다 출력
# print('반복적 구현', factorial_iterative(5))
# print('재귀적 구현', factorial_recursive(5))

# DFS(Depth-First Search): 깊이 우선 탐색
# BFS(Breadth First Search): 너비 우선 탐색

#그래프
# Node(=Vertex), Edge

# 그래프 2가지 표현 방식
# 인접행렬: 2차원 배열로 그래프의 연결관계 표현
# 인접 리스틔 리스트로 그래프의 연결관계를 표현
# 인접행렬 방식 예제
# 2차원 배열에 각 노드가 연결된 형태를 기록하는 방식
INF = 9999999999999 #무한 비용 선언
# 2차원 리스트를 이용해 인접 행렬 표현
graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]
print(graph)
#인접 리스트 방식
#모든 노드에 연결된 노드에 대한 정보를 차례대로 연결하여 저장
#연결리스트 자료구조 이용해 구현함 파이썬은 리스트 자료형이 append()와 메소드 제공
# 행이 3개인 2차원 리스트로 인접리스트 표현
graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1,7))
graph[0].append((2,5))

# 노드 1에 연결된 노드 정보 저장(노드,거리)
graph[1].append((0,7))

# 노드 2에 연결된 노드 정보 저장(노드, 거리)
graph[2].append((0,5))
print(graph)
# DFS

