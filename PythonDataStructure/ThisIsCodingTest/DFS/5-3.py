def recursive_function(i):
    # 100번째 출력했을 때 종료되도록 조건 명시
    if i == 100:
        return
    print(i, '번째 재귀 함수에서', i + 1, '번째 재귀 함수를 호출합니다.')
    recursive_function(i+1)

recursive_function(1)

# count = 1

# def recursive_function2():
#     global count
#     if count == 100:
#         return
#     print(count, '번째 재귀 함수에서', count + 1, '번째 재귀 함수를 호출합니다.')
#     count += 1
#     recursive_function2()

# recursive_function2()