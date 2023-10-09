# # 입력
# a = input()
# ##다중 입력
# a, b = input().split()
# # int 변환
# a, b = map(int, input().split())
# # 리스트
# list = list(map(int, input().split()))
# print(a, b)
# print(list)

# a,b,c = 'abc' 시 a = 'a', b= 'b', c='c'로 선언됨

# #입력 시간 최소화
# import sys
# s = sys.stdin.readline()
# print(s)
# #엔터키 등 개행문자삭제처리
# sn = sys.stdin.readline().strip()
# print(sn)
#
# #리스트 정렬
# list = [3, 2, 4, 1, 0, 9, 7]
# list.sort()
# list.sort(reverse=True) # 역정렬
# list.reverse()

# list.length 불가
# len(list)
# list = [0] + [0] #[0,0]

# 조건부 배열 선언
# list = [i for i in range(20) if i%2 == 1]

#iterator가 없는 for문
# for _ in range(50):

#파이썬 Boolean
# a = True
# b = False

# **파이썬은 증감연산자가 없음.. ++ -- 불가
# a, b = 0,0
# a += 1
# b += 1
