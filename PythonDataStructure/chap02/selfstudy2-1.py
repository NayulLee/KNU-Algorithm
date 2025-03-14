# 100과 20의 더하기, 빼기, 곱하기, 몫, 나머지, 제곱이 출력되도록 프로그램을 구현하자.

def multi(v1, v2):
    calc = [
        v1 + v2,
        v1 - v2,
        v1 * v2,
        v1 // v2,
        v1 % v2,
        v1 * v1,
        v2 * v2
    ]

    return calc

resultArr = multi(100, 20)
print("multi에서 반환한 값 ==>")
print(resultArr)

    

