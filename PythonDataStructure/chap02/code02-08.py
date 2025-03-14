singer = {}

print("요소 추가 이전 :", singer)

singer["이름"] = "트와이스"
singer["구성원 수"] = 9
singer["데뷔"] = "서바이벌 식스틴"
singer["대표곡"] = "우아하게"

for k in singer.keys() :
    print('%s --> %s' %(k, singer[k]))