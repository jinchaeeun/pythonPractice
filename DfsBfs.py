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
# 인접 리스트 리스트로 그래프의 연결관계를 표현

#    0
# 7/   \5
# 1     2
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

#    0
# 7/   \5
# 1     2
# 행이 3개인 2차원 리스트로 인접리스트 표현
graph = [[] for _ in range(3)] #초기화
# 노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1,7))
graph[0].append((2,5))

# 노드 1에 연결된 노드 정보 저장(노드,거리)
graph[1].append((0,7))

# 노드 2에 연결된 노드 정보 저장(노드, 거리)
graph[2].append((0,5))
print(graph)
##[[(1,7),(2,5)],[(0,7)],[(0,5)]]

# DFS 예제
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)

# 결과
# 1 2 7 6 8 3 4 5


# BFS 너비우선탐색. 가까운 노드부터 탐색. (큐 이용)
# 알고리즘
# 탐색시작노드를 큐에 삽입하고 방문 처리
# 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
# 바로 위의 과정을 수행할 수 없을 때까지 반복
#   1 - 2
#  / \   \
# 3   \   7
# |\   \ / |
# 4 5   8  6

# 시작노드인 1을 큐에 삽입하고 방문 처리.
# 큐에서 노드 1을 꺼내고 인접노드 2,3,8 큐 삽입 후 방문처리
# *DFS는 인접노드 중 가장 작은 노드의 깊이부터 팜
# 큐에서 노드 2를 꺼내고 인접노드 7을 큐에 삽입하고 방문처리
# 큐에서 노드 3을 꺼내고 인접노드 4,5를 큐에 삽입하고 방문처리
# 큐에서 노드 8을 꺼내고 인접노드가 없으므로 무시
# 큐에서 노드 7을 꺼내고 인접노드 6을 큐에 삽입하고 방문처리
## 1->2->3->8->7->4->5->6

# 일반적으로 DFS보단 BFS가 좀 더 빠르다. 다만 O(N)의 시간이 소요된다

# BFS 예제

from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
bfs(graph, 1, visited)

## 1 2 3 8 7 4 5 6


#
# ----------------------------------------------
#             |      DFS      |      BFS        |
# ----------------------------------------------|
# 동작 원리     |     스택       |      큐         |
# 구현 방법     |  재귀 함수 이용 |  큐 자료구조 이용  |
# -----------------------------------------------

# 게임 맵 같은 문제를 만났을 때 좌표를 그래프 형태로 바꿔서 풀면 좀 더 쉽다
