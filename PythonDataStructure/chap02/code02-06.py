myList = [30, 10, 20]
print("현재 리스트 : %s " % myList)

myList.append(40) # 리스트 맨 끝에 추가한다.
print("append(40)후의 리스트 : %s" % myList)

print("pop()으로 추출한 값 : %s" %myList.pop()) # 리스트명.pop(인덱스)
print("pop()후의 리스트 : %s" % myList)

myList.sort() # 리스트의 항목 정렬 : 기본 오름차순, 내림차순 : sort(reverse = True)
print("sort()후의 리스트 : %s" % myList)

myList.reverse()
print("reverse()후의 리스트 : %s" % myList)

print("20 값의 위치 : %d" %myList.index(20))

myList.insert(2, 222)
print("insert(2, 222후의 리스트 : %s" % myList)

myList.remove(222)
print("remove(222)후의 리스트 : %s" % myList)

myList.extend([77, 88, 77])
print("extend([77, 88, 77])후의 리스트 : %s" % myList)

print("77값의 개수 : %d" % myList.count(77))