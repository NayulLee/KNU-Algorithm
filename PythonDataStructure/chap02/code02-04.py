# 반환 값이 여러 개인 함수
def multi(v1, v2):
    retList = []
    res1 = v1 + v2
    res2 = v1 - v2
    retList.append(res1)
    retList.append(res2)
    return retList


myList = []
hap, sub = 0, 0

myList = multi(100, 200)
hap = myList[0]
sub = myList[1]

print("multi()에서 반환한 값 ==> %d %d" %(hap, sub))