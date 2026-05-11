stdNum = 26126041
stdName = "이재성"
print(stdNum, stdName)

foodInfo= {
    "치킨": 20000, 
    "피자": 21000,
    "햄버거": 5000 
    }


distance = float(input("배달 거리 입력(km 단위로 입력됩니다): "))
weather = input("우천 여부 입력(우천 시 Y, 아닐 시 N):")
delivPrice = 3000

if distance > 2:
    delivPrice += (1000*(math.ceil(distance-2)))