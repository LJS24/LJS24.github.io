import math # 올림 계산(math.ceil)을 위한 math 모듈 불러오기

# 학번과 이름을 변수에 저장
student_id = "26126041" # 본인 학번
name= "이재성" # 본인 이름
print(f"[학번:{student_id} 이름:{name}]") # 학번과 이름 출력

# 학번 문자열의 마지막 문자를 슬라이싱하여 정수로 변환
last_digit = int(student_id[-1])

# 음식 금액 계산 (단가 × 수량)
chicken = 20000*2 # 치킨: 20,000원 × 2개
pizza = 21000*1 # 피자: 21,000원 × 1개
burger = 5000*3 # 햄버거: 5,000원 × 3개
food_total = chicken + pizza + burger # 음식 총액 합산

# 배달비 초기값 설정 (기본값으로 출력)
base_fee = 3000 # 기본 배달비: 3,000원 고정
extra_fee = 0 # 추가 배달비: 초기값 0원
surcharge = 1.00 # 할증: 초기값 1.00
total_fee = int((base_fee + extra_fee)*surcharge) # 초기 총 배달비 계산

while True: # 3번(종료)을 선택할 때까지 메뉴 반복

    # 메뉴 항목 출력
    print()
    print("--------------------------------")
    print("1. 배달비 할증 적용")
    print("2. 결제 금액 확인")
    print("3. 종료")
    print("--------------------------------")

    choice = input() # 사용자 메뉴 번호 입력

    if choice == "1": # 1번 선택: 배달비 할증 적용
        
        # 우천 여부 입력 (Y/N 외 입력 시 재입력 요청)
        while True:
            rain = input("비가 오면 Y, 안오면 N으로 입력하세요. \n").strip().upper()  # 입력값 공백 제거 후 대문자 변환
            if rain == "Y" or rain == "N":  # Y 또는 N이면 루프 탈출
                break
            print("Y나 N를 입력해주세요. ")  # Y/N 외 입력 시 오류 메시지 출력
        
        # 배달거리 입력
        while True:
            try:
                distance = float(input("*** 배달거리를 km 단위로 입력하세요. ***\n"))  # 실수로 변환 시도
                if distance < 0:  # 음수 입력 방지
                    print("0 이상의 숫자로 입력해주세요.")
                    continue # 재입력
                break  # 변환 성공 시 루프 탈출
            except ValueError:  # 숫자로 변환 불가능한 값 입력 시
                print("잘못된 입력입니다. 양수인 숫자를 입력해주세요.")  # 오류 메시지 출력 후 재입력

        # 추가 배달비 계산: 2km 초과분을 올림 처리하여 1km당 1,000원 추가
        extra_fee = math.ceil(distance - 2)*1000 if distance > 2 else 0

        # 우천 할증 계산: 비가 오면 학번 끝자리 반영, 안 오면 1.00
        if rain == "Y":
            surcharge = 1.10 + last_digit * 0.01  # 끝자리가 1이므로 1.11
        else:
            surcharge = 1.00  # 할증 없음
        
        total_fee = int((base_fee + extra_fee) * surcharge)  # 총 배달비 = (기본 + 추가) × 할증, 소수점 버림(규정이 없어 현금을 가정하고 소수점을 버렸습니다.))
        
        # 배달비 계산 결과 출력
        print("…………………………………………….")
        print("[배달비용]")
        print(f"기본배달비: {base_fee}원")   # 기본 배달비 출력
        print(f"추가배달비: {extra_fee}원")  # 추가 배달비 출력
        print(f"할증: {surcharge:.2f}")      # 할증 소수점 둘째 자리까지 출력
        print(f"총 : {total_fee}원 ")        # 총 배달비 출력
        print("………………………………………………")

    elif choice == "2":  # 2번 선택: 결제 금액 확인

        print(f"[총 결재 금액 – {food_total + total_fee} 원]")  # 음식 총액 + 배달비
        print(f"<음식 금액 – {food_total}원>")                  # 음식 총액
        print(f"치킨 = 20000원 * 2 = {chicken}원")              # 치킨 금액 상세
        print(f"피자 = 21000원 * 1 = {pizza}원")                # 피자 금액 상세
        print(f"햄버거 = 5000원 * 3 = {burger}원")              # 햄버거 금액 상세
        print(f"<배달비용 - {total_fee}원>")                    # 배달비 총액
        print(f"기본배달비: {base_fee}원")                      # 기본 배달비
        print(f"추가배달비: {extra_fee}원")                     # 추가 배달비
        print(f"할증: {surcharge:.2f}")                         # 할증

    elif choice == "3":  # 3번 선택: 프로그램 종료
        break

    else:  # 1, 2, 3 외의 값 입력 시
        print("**** 메뉴에 있는 숫자를 다시 입력하세요. ****")  # 오류 메시지 출력 후 메뉴 재출력