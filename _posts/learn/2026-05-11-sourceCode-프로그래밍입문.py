import math

# 학번과 이름 출력
student_id = "26126041"  # 본인 학번으로 수정
name = "이재성"          # 본인 이름으로 수정
print(f"[학번: {student_id} 이름: {name}]")

# 학번 끝자리 추출 (문자열 슬라이싱)
last_digit = int(student_id[-1])

# 고정 음식 금액
chicken = 20000 * 2   # 치킨 2개
pizza   = 21000 * 1   # 피자 1개
burger  =  5000 * 3   # 햄버거 3개
food_total = chicken + pizza + burger  # 음식 총액

# 배달비 초기값
base_fee  = 3000
extra_fee = 0
surcharge = 1.00
total_fee = int((base_fee + extra_fee) * surcharge)

while True:
    # 메뉴 출력
    print()
    print("--------------------------------")
    print("1. 배달비 할증 적용")
    print("2. 결제 금액 확인")
    print("3. 종료")
    print("---------------------------------")

    choice = input()

    if choice == "1":
        # 비 여부 입력
        while True:
            rain = input("비가 오면 Y, 안오면 N으로 입력하세요. \n").strip().upper()
            if rain == "Y" or rain == "N":
                break
            print("Y나 N를 입력해주세요. ")

        # 배달거리 입력
        while True:
            try:
                distance = float(input("배달거리를 km 단위로 입력하세요. \n"))
                break
            except ValueError:
                print("실수 범위 숫자로 입력해주세요.") 

        # 배달비 계산
        extra_fee = math.ceil(distance - 2) * 1000 if distance > 2 else 0

        if rain == "Y":
            surcharge = 1.10 + last_digit * 0.01  # 학번 끝자리로 할증 계산
        else:
            surcharge = 1.00

        total_fee = int((base_fee + extra_fee) * surcharge)

        # 배달비 출력
        print("…………………………………………….")
        print("[배달비용]")
        print(f"기본배달비: {base_fee}원")
        print(f"추가배달비: {extra_fee}원")
        print(f"할증: {surcharge:.2f}")
        print(f"총 : {total_fee}원 ")
        print("………………………………………………")

    elif choice == "2":
        # 어떤 순서로 선택해도 작동
        print(f"[총 결재 금액 – {food_total + total_fee} 원]")
        print(f"<음식 금액 – {food_total}원>")
        print(f"치킨 = 20000원 * 2 = {chicken}원")
        print(f"피자 = 21000원 * 1 = {pizza}원")
        print(f"햄버거 = 5000원 * 3 = {burger}원")
        print(f"<배달비용 - {total_fee}원>")
        print(f"기본배달비: {base_fee}원")
        print(f"추가배달비: {extra_fee}원")
        print(f"할증: {surcharge:.2f}")

    elif choice == "3":
        break  # 종료

    else:
        print("**** 메뉴에 있는 숫자만 가능. 다시 입력하세요. ****")