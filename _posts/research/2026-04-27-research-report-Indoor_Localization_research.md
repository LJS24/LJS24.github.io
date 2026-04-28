---
title: "기술 조사-smartphone-based indoor localization technology(과제 용도)"
date: 2026-04-27
categories: [research]
tags: [web research, report]
summary: "논문 및 학술 문서 기반, 기술 조사 및 조사 보고서 작성"
---

## Abstract(초록 번역)
현대 건축 환경에서 GPS 신호의 실내 도달이 불가능한 물리적 한계로 인해, 스마트폰 내장 센서와 무선 통신 모듈을 활용한 실내 로컬라이제이션 기술의 중요성이 급증하고 있다. 본 보고서는 현재 학계 및 산업계에서 주목받는 스마트폰 기반 실내 측위 핵심 기술 3종, 즉 Wi-Fi RTT(Round-Trip-Time) 기반 측위, 보행자 추측 항법(PDR) 및 다중 센서 융합, 실내 지자기장 지문(Magnetic Field Fingerprinting) 기반 측위에 대한 심층 분석 및 상호 비교를 수행한다.
Wi-Fi RTT 기술은 IEEE 802.11mc 표준에 기반하여 무선 패킷의 비행시간(ToF)을 나노초 단위로 측정함으로써 기존 RSSI 방식 대비 현저히 향상된 1~2미터 내외의 위치 정확도를 달성하며, Android 운영체제의 공식 API를 통해 상용 생태계에 이미 진입해 있다. PDR은 가속도계, 자이로스코프, 자력계, 기압계 등 관성 센서 배열만으로 외부 인프라 없이 보행자의 궤적을 실시간 추론하는 인프라 독립형 기술로, 적응형 머신러닝 모델 결합 시 1% 미만의 거리 오차율을 달성하지만 장거리 운용 시 누적 오차 발산이라는 구조적 한계를 지닌다. 지자기장 핑거프린팅은 건물 철골 구조물에 의해 왜곡된 실내 자기장의 공간적 고유성을 데이터베이스화하여 위치를 매칭하는 방식으로, 딥러닝 알고리즘과의 융합을 통해 최대 20cm 미만의 정밀도에 도달하나, 기기 간 센서 이질성 및 수동 맵핑 부담이 과제로 남는다.
비교 분석 결과, 세 기술은 신호 투과성, 오차 특성, 인프라 의존도, 프라이버시 보호 측면에서 상호 보완적인 구조를 이룬다. Wi-Fi RTT의 안정적 절대 좌표 제공 능력, PDR의 고빈도 연속 추적 능력, 지자기 기술의 무선 간섭 면역성이 결합된 다중 센서 융합(Multi-sensor Fusion) 프레임워크가 실내 측위의 표준 아키텍처로 수렴하고 있으며, 확장 칼만 필터(EKF) 및 딥러닝 기반의 소프트웨어 통합이 이를 구현하는 핵심 수단으로 자리잡고 있다. 본 보고서는 각 기술의 원리, 활용 센서, 성능 특성, 실제 적용 사례를 체계적으로 정리함으로써 실내 측위 분야의 기술 선택 및 융합 설계에 대한 실질적 참고 기반을 제공한다.

## 서론
 현대의 글로벌 내비게이션 위성 시스템(GNSS) 및 전 지구적 위치 파악 시스템(GPS)은 실외 환경에서 2~3미터 이내의 오차율을 보이며 거대한 위치 기반 서비스(Location-Based Services, LBS) 생태계를 구축하였다. 그러나 스마트 빌딩, 대형 쇼핑몰, 지하 교통망, 복합 의료 시설 등의 실내 활동 패턴의 증가 및 규모 거대화에 따라, 실내 환경에서의 정밀한 위치 추적에 대한 산업적, 학술적 요구가 급증하고 있다1. 특히 실내 환경에서는 콘크리트, 철골 구조물, 그리고 다양한 금속성 건축 자재로 인해 심각한 신호 감쇠(Signal attenuation)와 다중 경로 반사(Multipath reflection), 비가시선(Non-Line-Of-Sight, NLOS) 환경이 형성되며, 이로 인해 위성에서 송출되는 GPS 신호는 실내로 진입하는 순간 약화되거나 소실된다3.
 이러한 GPS의 물리적 한계를 극복하기 위해 등장한 대안 중 하나가 스마트폰에 내장된 센서 네트워크와 통신 칩셋을 활용한 실내 로컬라이제이션(Indoor Localization) 기술이다5. 전 세계적으로 보급된 스마트폰은 가속도계, 자이로스코프, 자력계, 기압계 등의 고정밀 관성 측정 장치(IMU)와 Wi-Fi, 블루투스 저전력(BLE), 초광대역(UWB) 등의 무선 주파수(RF) 통신 모듈을 집적하고 있는 이상적인 편재형 컴퓨팅(Ubiquitous computing) 플랫폼이다1. 스마트폰만을 단일 단말기로 활용하는 실내 로컬라이제이션 기술은 별도의 전용 추적용 하드웨어 장치를 휴대할 필요가 없다는 점에서 B2C(기업과 소비자 간 거래) 및 B2B(기업 간 거래) 시장 모두에서 높은 잠재력을 지닌다. 
스마트폰 기반 실내 로컬라이제이션 기술은 크게 두 가지 접근으로 나뉜다. 첫째는 건물 내부에 구축된 통신 인프라(AP, 비콘 등)가 송출하는 무선 신호를 스마트폰이 수신하여 위치를 연산하는 '인프라 기반(Infrastructure-based)' 방식이며, 둘째는 인프라에 의존하지 않고 지구 지자기장이나 보행자의 관성 등 자연적, 물리적 현상만을 스마트폰의 내장 센서로 측정하여 궤적을 추론하는 '인프라 독립적(Infrastructure-free)' 방식이다5.
 본 보고서는 학계 표준 문서(IEEE Std) 및 공신력 있는 저널 게재 논문, 글로벌 기술 기업(IBM, Cisco, Apple, Google 등)의 공식 문헌을 기반으로 스마트폰 기반 실내 로컬라이제이션 기술 3종에 대해 조사를 수행하였다. 이때 ‘로컬라이제이션(Localization)’과 ‘측위’ 는 같은 의미의 용어로 두고 혼용하여 서술하였다. 
분석 대상으로 선정된 기술은 다음과 같다:

-Wi-Fi RTT (Round-Trip-Time) 기반 로컬라이제이션 기술 
-보행자 추측 항법(Pedestrian Dead Reckoning, PDR) 및 센서 융합 기술 
-실내 지자기장 지문 기반 로컬라이제이션 기술(Magnetic Field Fingerprinting)


## 1.Wi-Fi RTT (Round-Trip-Time) 및 FTM 기반 실내 로컬라이제이션 기술
1.1. 기술명
Wi-Fi RTT(Round-Trip-Time) 및 정밀 시간 측정(FTM, Fine-Time-Measurement) 프로토콜 기반 실내 로컬라이제이션 기술
1.2. 기술의 원리
 초기의 Wi-Fi 기반 실내 로컬라이제이션 기술은 스마트폰이 주변 액세스 포인트(AP)로부터 수신하는 신호의 강도(RSSI, Received Signal Strength Indication)를 기반으로 거리를 추정하는 방식에 의존했다. 그러나 무선 전파는 실내의 벽면, 사람의 이동, 가구의 배치 등에 의해 다중 경로 페이딩(Multipath fading)과 산란 현상을 겪으므로, RSSI 모델은 환경적 노이즈에 극도로 취약하여 3~5미터 이상의 심각한 위치 오차를 유발하였다8.
이러한 RSSI의 한계를 극복하기 위해 제안된 기술이 IEEE 802.11mc 워킹그룹(TGmc)이 표준화한 Wi-Fi RTT 및 FTM(Fine-Time-Measurement) 기술이다9. 이 기술의 핵심 원리는 전파의 신호 강도를 무시하고, 전파가 공간을 이동하는 '비행시간(ToF, Time of Flight)' 자체를 나노초(Nanosecond) 단위로 직접 측정하는 데 있다2.
측정 메커니즘은 스마트폰(개시자, Initiator)과 무선 AP(응답자, Responder) 간의 하드웨어 타임스탬프 교환으로 이루어진다. 스마트폰이 FTM 요청 패킷을 AP에 전송하면, AP는 이를 수신하고 응답 패킷을 다시 스마트폰으로 반환한다. 이때 패킷이 왕복하는 데 걸린 총 시간(RTT)에서 AP가 신호를 처리하는 데 소요된 내부 지연 시간을 뺀 순수 비행시간을 도출한다. 산출된 비행시간에 진공에서의 빛의 속도(  m/s)를 곱하고 2로 나누면 단말기와 AP 간의 물리적 유효 거리가 정확하게 계산된다8. 스마트폰이 최소 3개 이상의 AP와 성공적으로 RTT 거리를 계산하게 되면, 삼변 측량(Trilateration) 또는 다변 측량(Multilateration)이라는 알고리즘으로 교차점을 연산하여 2차원 또는 3차원 공간상의 자신의 위치 좌표를 특정하게 된다.8
1.3. 사용되는 스마트폰 센서 또는 신호
 이 기술은 별도의 물리적 가속도 센서나 자력계를 요구하지 않으며, 오로지 스마트폰에 내장된 Wi-Fi 무선 통신 칩셋 및 안테나 시스템만을 센서로 활용한다.
작동을 위해서는 소프트웨어와 하드웨어의 특정 표준 지원이 필수적이다. 하드웨어에서는 스마트폰의 무선 칩셋이 IEEE 802.11-2016 FTM 표준을 네이티브 수준에서 지원해야 하고8, 소프트웨어에서는 Google Android 9 (API 레벨 28) 이상이 설치되어 있어야 RTT API에 접근할 수 있다8. 스마트폰 운영체제는 네트워크 스캐닝을 통해 주변 AP의 ScanResult 객체를 획득하고, 이를 기반으로 RangingRequest를 생성하여 다수의 AP에 동시다발적인 거리 측정 패킷을 송출한다8. 특히 Android 10 (API 29) 이상부터는 AP가 송출하는 LCI(Location Configuration Information, 위도/경도/고도 정보) 및 LCR(Location Civic Report, 층수/건물명 정보) 데이터를 직접 해석할 수 있어, 사전에 별도의 좌표 데이터베이스를 스마트폰에 다운로드하지 않아도 인프라의 응답만으로 위치를 연산하는 독립성을 확보하였다8. 또한 Android 15 (API 35)부터는 비 트리거 기반(NTB, Non-Trigger Based) 거리 측정을 지원하는 최신 IEEE 802.11az 규격을 융합 지원하여 센싱 주파수 신호의 밀도를 높이고 있다.
1.4. 장점
 첫 번째 장점은 데이터 프라이버시(Privacy) 보호 구조이다. RTT 프로토콜의 설계상 거리 연산과 위치 결정을 수행하는 주체는 전적으로 스마트폰 단말기(Client) 내부의 프로세서이다8. 즉, 무선 AP 인프라는 단말기에게 타임스탬프 정보만을 제공할 뿐, 사용자가 누구이며 어디에 위치해 있는지 역으로 계산하거나 중앙 서버로 전송할 수 없다. 
두 번째는 무연결성(Connection-less)이다. 거리를 측정하기 위해 대상 AP와 인터넷 통신을 위한 WPA/WPA2 인증을 거치거나 특정 네트워크(SSID)에 접속할 필요가 없으며, 단순히 인근에 떠 있는 Wi-Fi 신호와 FTM 패킷만 교환하면 즉시 거리가 도출된다8.
세 번째로는 RSSI 방식 대비 압도적인 신호 캘리브레이션의 간소화이다. 수신 강도는 주변 습도나 사람의 존재 여부에 따라 끊임없이 변화하므로 주기적인 핑거프린트 업데이트가 필요하나, RTT는 물리적인 빛의 이동 시간을 기반으로 하므로 매장의 진열장이나 가구 배치가 바뀌어도 성능의 저하가 거의 발생하지 않는다9. 기존 엔터프라이즈 환경에 설치된 Cisco 등 주요 제조사의 Wi-Fi AP 펌웨어 업데이트만으로 인프라를 전면 재활용할 수 있다는 점은 상업적으로 장점이다2.
1.5. 단점
 첫 번째 단점은 인프라 의존도(Infrastructure Dependency)이다. 공간 내부에 IEEE 802.11mc 또는 802.11az 를 만족하는 하드웨어를 내장한 AP가 최소 3대 이상, 이상적으로는 4대 이상이 가시선(LOS) 범위 내에 촘촘하게 배치되어 있어야 삼변 측량 알고리즘이 성립한다2.
두 번째는 다중 경로 환경에서 비가시선(NLOS) 조건에 직면할 경우 발생하는 물리적 오차이다. 스마트폰과 AP 사이에 콘크리트 기둥이나 두꺼운 방화문이 존재하여 전파가 굴절되거나 반사되어 도달하는 경우, 신호의 비행시간이 실제 직선거리보다 길어지게 되어 결과적으로 거리를 과대평가(Overestimation)하는 계통적 오차(Systematic bias)가 발생한다11.
세 번째로는 단말기의 전력 소모와 운영체제 정책에 따른 스로틀링(Throttling) 제약이다. Wi-Fi 칩셋을 반복적으로 가동하여 RTT를 수행하는 것은 배터리 소모를 가중시키므로, Android 운영체제는 앱이 백그라운드로 전환될 경우 RTT 연산 빈도를 강제로 제한(스로틀링)하여 실시간 동적 추적 성능을 억제하는 정책을 취하고 있다8.
1.6. 정확도 또는 성능 특징
 기존의 전통적인 Wi-Fi RSSI 핑거프린팅 기술이 약 3~5미터 수준의 오차를 보인 반면, 802.11mc 기반의 Wi-Fi RTT 기술은 평균 1~2미터 내외의 매우 정밀한 위치 정확도를 꾸준하게 달성한다2. 학계의 정밀 연구 결과에 따르면, 시스템 고유의 편향성을 제거하고 클러스터링 기반 삼변 측량(CbT, Clustering-based Trilateration) 및 가중 동심원 생성(WCCG) 알고리즘을 융합한 IEEE 논문 상의
고도화된 아키텍처는 정적(Static) 환경에서  미터, 보행자가 움직이는 동적 모션 추적 환경에서  미터의 초정밀 성능을 일관되게 입증하였다.11 최소 자승법(LS) 대비 정확도를 68.5%가량 극적으로 향상시킨 이 수치는 이론적 한계인 크래머-라오 하한(Cramer-Rao Bound, CRB)에 매우 근접한 성능이다11 . 나아가 IEEE 802.11az (차세대 포지셔닝 표준) 규격을 지원하는 하드웨어의 경우 대역폭 확장과 각도 분해능 개선을 통해 1미터 미만 수준의 위치 해상도 도달을 목표로 하고 있다2.
1.7. 실제 활용 사례 (논문, 서비스, 프로젝트 등)

분류	사례 명칭 및 주요 내용 분석	출처
운영체제 API	Google Android Wi-Fi RTT Framework: 
Google은 API 레벨 28 (Android 9)부터 개발자들이 WifiRttManager 클래스를 호출하여 직접 FTM 기반 다변 측량 내비게이션 앱을 개발할 수 있도록 지원 중이다. API 레벨 33에서는 NEARBY_WIFI_DEVICES 런타임 권한을 통해 개인정보 보호를 강화하였고, API 레벨 35부터 802.11az NTB 레인징을 전격 도입하여 생태계를 주도하고 있다.	8
글로벌 서비스	Cisco Spaces 클라우드 플랫폼: 
글로벌 네트워크 인프라 리더인 Cisco는 기업용 무선 LAN 컨트롤러와 'Cisco Spaces' 클라우드 솔루션을 통합하여 FTM 기반 실내 위치 서비스를 상용화하였다. 이를 통해 병원, 공항, 대형 물류 창고 등에서 자산 추적(Asset tracking), 병목 현상 완화, 작업자 실내 내비게이션, 인력 할당 최적화 등의 B2B 로케이션 분석 인프라를 제공한다.	2
학술 논문	IEEE Transactions on Mobile Computing 게재 연구: 상용(COTS) 스마트폰과 Wi-Fi AP만을 사용하여 CbT 및 WCCG 알고리즘 기반의 3단계 포지셔닝 기법을 설계한 연구이다. 여러 교차점이 발생하거나 아예 교차점이 생성되지 않는 다중 경로 환경의 왜곡을 칼만 필터(Kalman filter)를 통해 수학적으로 제거하여, 1.2~1.3미터 수준의 오차 감소 결과를 입증하였다.	11


## 2. 보행자 추측 항법 (Pedestrian Dead Reckoning, PDR) 및 다중 센서 융합 Localization 기술
2.1. 기술명
보행자 추측 항법(Pedestrian Dead Reckoning, PDR) 및 다중 내장 센서 융합 기반 실내 로컬라이제이션 기술
2.2. 기술의 원리
 보행자 추측 항법(PDR)은 선박이나 항공기에서 기원한 전통적인 추측 항법(Dead Reckoning)을 인체의 2족 보행 역학계에 적용한 기술이다. 외부의 무선 인프라(AP, 위성 등)와 일절 통신하지 않고 오로지 스마트폰 내부에 장착된 미세 전자기계 시스템(MEMS) 기반의 센서 데이터만을 실시간으로 분석하여, 사전에 알고 있는 출발점(Known starting point)으로부터 상대적인 변위 벡터를 누적 연산해 현재 위치를 추정해 나가는 철학을 지닌다5.
이 시스템은 정교하게 설계된 네 단계의 순차적인 수학적 파이프라인으로 구성된다.
1.	모션 상태 인식 및 걸음 감지 (Step Detection): 가속도계에서 입력되는 3축 가속도의 합벡터(Magnitude) 데이터의 파형을 분석한다. 사용자가 발을 디딜 때 발생하는 주기적인 파형에서 특정 피크(Peak)와 밸리(Valley) 임계값을 동적으로 적용하는 '피크 감지 방법(Peak detection method)'을 통해 오탐지를 거르고 정확히 한 걸음이 발생한 시점을 특정한다5.
2.	보폭 추정 (Step Length Estimation): 걸음을 감지한 후 해당 걸음의 물리적 이동 거리를 추정한다. 학계에서 가장 널리 쓰이는 경험적 수학 모델인 와인버그 모델(Weinberg's model)이 주로 사용된다. 수식은   으로 정의되며, 여기서 $a_{max}$와 $a_{min}$은 한 걸음 사이클 내의 최대/최소 수직 가속도 값이고,  는 보행자의 성별, 신장, 보행 속도 등에 따라 동적으로 튜닝되는 상수(Coefficient)다5.
3.	방향 및 헤딩 추정 (Heading Estimation): 자이로스코프의 각속도 데이터와 자력계의 지구 자기장 방향 데이터를 융합하여 보행자의 진행 방향(요 앵글, Yaw angle)을 도출한다. 센서 노이즈를 제어하기 위해 경사 하강법 기반의 Madgwick 필터나 상보 필터(Complementary Filter), 혹은 칼만 필터가 적용된다. 
4.	층수 및 고도 전환 감지 (Floor Detection): 기압계 데이터를 지속 모니터링하여 엘리베이터 이동이나 계단 등반 시 발생하는 급격한 기압 변동을 포착해 3D 공간상의 층수 표고를 재계산한다5. 결과적으로 산출된 보폭 및 방향 스칼라 값은 삼각함수에 의해 X, Y 좌표의 미세 변위벡터로 변환되어 직전 좌표에 지속적으로 누적 합산된다.
2.3. 사용되는 스마트폰 센서 또는 신호
PDR 시스템은 통신을 배제하고 다음과 같은 복합 관성 및 환경 센서 배열의 동기화된(Synchronized) 시계열 데이터를 융합하여 활용한다.
활용 센서 명칭	실내 측위 연산에서의 핵심 역할 및 기능 분석
가속도계 (Accelerometer)	3차원 선형 가속도를 측정한다. 보행자의 상태(정지, 걷기, 뛰기 등)를 식별하고 걸음 발생 횟수(Step detection)를 인식하며, Weinberg 모델에   변수를 공급하여 보폭을 도출하는 기저 데이터를 제공한다.
자이로스코프 (Gyroscope)	코리올리 힘(Coriolis force)의 원리를 이용해 3축 각속도를 정밀 측정한다. 보행자의 방향 전환(Turn)을 즉각적으로 감지하고 진행 방향(Heading)의 회전율을 계산한다. 단독 사용 시 누적 오차(Drift)가 크다.
자력계 (Magnetometer)	지구의 자기장을 감지하여 변치 않는 '절대 북쪽'의 참조 프레임을 제공한다. 자이로스코프 센서가 지닌 수학적 드리프트 오차를 주기적으로 보정하여 일관된 방향성을 유지하도록 돕는다.
기압계 (Barometer)	대기압을 파스칼 단위로 측정한다. 실내 복층 건물 구조에서 평면 이동(X,Y)이 아닌 고도 이동(Z), 즉 계단이나 엘리베이터를 통한 층(Floor) 변동 여부를 초정밀도로 식별하는 데 결정적 역할을 수행한다.
2.4. 장점
 가장 돋보이는 장점은 완벽한 인프라 독립성(Infrastructure-free)이다5. 공간 소유주가 수천만 원의 비용을 들여 비콘이나 UWB, 특정 Wi-Fi 장비를 천장이나 벽에 부착할 필요가 없으며, 정기적인 장비 유지보수나 배터리 교체, 전원 공급 공사가 생략된다. 
다음은 서비스의 연속성(Continuity)이다. 화재나 정전 등 비상 상황으로 인해 실내 통신망이 전면 마비되거나 지하 5층 주차장 같은 극단적 통신 음영 구역에서도 스마트폰의 전원이 켜져 있다면 끊김 없이 추적 궤적을 렌더링할 수 있다1.
통신 기반 측위 방식들(Wi-Fi, BLE)보다 높은 데이터 프라이버시 보장성 또한 장점이다. 모든 관성 계산은 프로세서(Edge) 단위에서 종결되므로 네트워크 해킹에 의한 위치 데이터 유출 위험이 0에 수렴한다5.
2.5. 단점
 이 기술이 단독으로 상용화되기 어려운 주된 이유는 누적 오차 현상(Cumulative error/Drift) 때문이다. MEMS 센서 자체가 지닌 극미한 하드웨어 노이즈와 걸음 수 산정 및 보폭 계산 과정의 휴리스틱(Heuristic) 근사치 오차가 매 걸음이 발생할 때마다 누적된다. 따라서 시작점에서 10미터를 이동했을 때보다 500미터를 이동했을 때 추정 좌표와 실제 좌표 간의 편차가 이동 거리에 비례하여 선형적(Linear)으로 증가, 결국 벽을 뚫고 지나가는 궤적을 그리는 현상이 발생한다5. 
또한, 궤적 산출의 강건성(Robustness)이 보행자의 개별적 행동 특성에 극심하게 종속되는 문제도 있다. 사용자가 스마트폰을 바지 주머니에 넣고 걷는지, 화면을 보며 문자를 입력(Texting)하는지, 귀에 대고 통화(Calling)하는지, 짐을 들고 팔을 흔드는지(Swinging)에 따라 센서에 가해지는 G포스와 각속도 파형이 달라지며, 이를 보정하기 위해서는 고도화된 딥러닝 기반의 맥락 인식(Context recognition)이 동반되어야만 한다5.
2.6. 정확도 또는 성능 특징
 PDR 성능의 평가는 통상적으로 절대적인 1미터, 2미터의 수치보다는 총 이동 거리 대비 상대적 거리 추정 오차율(%)로 표현된다. 최신 머신러닝(SVM, 의사결정 트리 모델 등)을 적용해 스마트폰의 파지 모드, 성별 차이, 보행 속도를 실시간 식별하여 상수 파라미터를 자동 조율하는 '적응형 PDR(Adaptive PDR)'의 경우 높은 정확도를 입증하였다5.

구분	파지 상태 (Mode)	식별 정확도	거리 추정 상대 오차율 (%)	평균 절대 위치 오차 (m)
여성 보행자	문자를 치며 걷기 (Texting)	평균 97.03%	0.87%	1.28 m
	통화하며 걷기 (Calling)		0.66%	0.98 m
	팔을 흔들며 걷기 (Swinging)		0.92%	1.29 m
남성 보행자	문자를 치며 걷기 (Texting)	평균 97.67%	1.14%	1.26 m
	통화하며 걷기 (Calling)		0.92%	1.17 m
	팔을 흔들며 걷기 (Swinging)		0.76%	1.25 m
 표에서 보듯 파지 모드를 성공적으로 식별한 이상적 조건 하에서는 거리 오차율을 1% 미만으로 억제하며, 약 160m를 이동해도 오차가 1미터 내외에 불과한 고정밀 추적을 실현한다5. 개인화된 보폭 맥락 인식(Context-assisted personalized step length) 모델을 결합하면 기존 7.06%의 고질적 오차율을 2.01%로 통제하여 위치 오차를 1.63m로 방어하는 성과도 입증되었다21. 단, 이는 단기적인 주행 결과이며, 장시간 운용을 위해서는 외부 참조 신호와의 센서 융합(Sensor Fusion)이 필수적이라는 한계성을 내포한다.
2.7. 실제 활용 사례 (논문, 서비스, 프로젝트 등)

분류	사례 명칭 및 주요 내용 분석	출처
학술 논문	순환 신경망(RNN) 기반 거리 측정 및 빔포밍 최적화: 
IEEE 학술회의에서 발표된 연구는 전통적 수식 의존 모델 대신, LSTM(Long Short Term Memory) 기반 순환 신경망 딥러닝 아키텍처에 스마트폰 IMU 데이터를 시계열로 주입하여 거리 자체를 회귀 분석했다. 100m 구간에서 97.98%, 400m 구간에서 95.98%의 거리 예측 정확도를 도출하였으며, 산출된 고정밀 PDR 데이터를 차세대 5G/6G 밀리미터파(mmWave) WLAN 환경에서 단말기와 AP 간의 무분별한 빔 트레이닝(Beam training) 탐색 빈도를 줄이는 통신 최적화 알고리즘에 접목하였다.	22
알고리즘 프레임워크	크리깅(Kriging) 보간법 및 EKF 기반 Wi-Fi-PDR 융합 기술: 
PDR의 누적 오차 문제를 해결하기 위해 제시된 하이브리드 아키텍처이다. 희소하게 수집된 Wi-Fi 지문 데이터를 공간통계학적 크리깅 기법으로 2배 증폭시켜 지도 데이터 밀도를 높이고, 자이로스코프와 자력계의 헤딩 방향을 제약 조건으로 묶은 PDR의 관성 연산 값을 '확장 칼만 필터(Extended Kalman Filter, EKF)'로 융합하였다. 단일 PDR 사용 시 평균 2.02m의 오차율을 보이던 궤적을 0.71m(90% 확률 구간 1.42m 이내)까지 획기적으로 압축하는 데 성공하여 산업계 프레임워크 설계의 모범 답안으로 평가받는다.	24
내비게이션 컨텍스트	공간 맥락 맵핑(Spatial Context Mapping): 
다층 건물의 실내 지도 데이터(통로, 계단, 벽 등 기하학적 제약 요건)를 사전 정보(Prior information)로 입력해 둔 상태에서, 사용자가 벽을 투과하여 지나가는 비현실적인 PDR 궤적 벡터가 도출되면 이를 가장 가까운 정상 보행 통로로 자동 보정(Map-matching)하는 3D 다층 융합 내비게이션 알고리즘 프로젝트들이 활발히 구현되고 있다.	26


## 3. 실내 지자기장 지문 (Magnetic Field Fingerprinting) 기반 로컬라이제이션 기술 
3.1. 기술명
실내 지자기장 지문(Magnetic Field Fingerprinting) 및 공간 매핑 기반 로컬라이제이션 기술
3.2. 기술의 원리
 철새나 특정 곤충들이 지구 자기장을 나침반 삼아 장거리를 이동하는 생물학적 원리처럼, 실내 지자기장 핑거프린팅 기술은 실내 공간 특유의 지구 자기장 왜곡 현상을 위치 추적의 핵심 지표로 역이용하는 기술이다7. 지구가 발생시키는 기본 자기장(통상 25 ~ 65  T범위)은 본래 균일한 흐름을 유지하지만, 현대 건축물을 구성하는 철근 콘크리트 골조, H빔(솔리드 스틸), 엘리베이터, 금속성 방화문 등 다양한 강자성 물질(Ferromagnetic materials)에 의해 부딪히고 굴절되면서 복잡하게 일그러진다3.
이렇게 왜곡되어 형성된 미세한 국소적 자기장 변화를 '지자기 이상(Geomagnetic anomalies)'이라고 부르며, 이 이상 패턴은 건물의 구조가 해체되지 않는 이상 영구적이고 공간적으로 매우 독특한 고유의 특성인  '자기장 지문(Magnetic Fingerprint)' 을 형성한다1.
기술의 구현은 크게 오프라인 수집 단계와 온라인 매칭 및 추적 단계로 이등분된다6. 오프라인 단계에서는 작업자가 스마트폰이나 수집 로봇을 들고 실내 공간 전체의 그리드(Grid)를 누비며 X, Y 좌표별 자기장 수치를 스캔하여 데이터베이스(자기 지도, Magnetic Map)를 조밀하게 구축한다. 이후 온라인 단계에서 실제 사용자가 스마트폰을 들고 이동하면, 단일 포인트의 순간적 수치 비교가 아닌 사용자의 이동 경로에 따라 연속적으로 수집된 시계열 자기장 패턴(Magnetic sequence)을 동적 시간 워핑(DTW, Dynamic Time Warping)이나 CNN, LSTM과 같은 딥러닝 인공지능에 주입해 방대한 DB 내부의 특정 궤적과 일치(Pattern matching)하는지를 수학적으로 확률 연산하여 절대 위치를 특정한다29.
3.3. 사용되는 스마트폰 센서 또는 신호
 이 방식의 데이터 취득 통로는 오직 스마트폰에 내장된 저전력 3축 자력계(Magnetometer) 하나에
의존한다1. 자력계는 X, Y, Z 세 가지 직교축을 기준으로 자기장 벡터의 성분( )과 전체 자기장 벡터의 모듈러스(강도 합)를 헤르츠(Hz) 단위로 스캐닝한다7. 외부의 무선 주파수(RF) 신호를 전혀 수신할 필요가 없으므로 Wi-Fi 칩셋이나 블루투스 모듈은 오프 상태여도 무방하다.
3.4. 장점
 첫 번째 장점은 무선 통신 신호(Wi-Fi, BLE)가 태생적으로 겪는 비가시선(NLOS) 환경 및 무선 간섭으로 인한 오차에 대해 면역성(Immunity)을 지닌다는 점이다3. 자기장은 인체, 나무 테이블, 가벽 등 비자성 물질을 아무런 감쇠 없이 투과하므로, 통신 기반 측위 기법들이 애를 먹는 혼잡한 환경에서도 굳건하게 동작한다. 특히 철제 엘리베이터나 자판기 같은 구조물은 통신 전파에겐 방해물이지만, 지자기 기술 관점에서는 공간 식별력을 극대화하여 핑거프린트 매칭의 정확도를 급격히 상승시키는 랜드마크 (Guideposts)로 작용한다3. 두 번째는 시간적 안정성(Temporal stability)이다. Wi-Fi AP는 고장이나 교체로 인해 MAC 주소나 송출 강도가 변동될 수 있지만, 건물의 철골 뼈대가 발산하는 지자기장 구조는 수십 년간 훼손되지 않으므로 맵핑 데이터의 유효 기간이 매우 길다7 . 세 번째로 PDR과 마찬가지로 비콘 등 부가 인프라 배선 공사가 불필요하여 하드웨어 구축 자본 지출(CAPEX)이 0에 수렴한다는 경제적 이점이 있다7.
3.5. 단점
 가장 심각한 기술적 장벽은 기기 간 이질성(Device Heterogeneity) 문제다. 스마트폰 제조사(Apple, Samsung 등)마다 채택한 자력계 센서 칩의 공정 편차 및 하드웨어 스펙이 다르고, 각 기기 내부의 배터리 등 전자기 부품이 발산하는 자체 자기장(Soft and hard iron interference)이 상이하다. 이로 인해 동일한 위치, 동일한 시간에 스캔하더라도 이기종 기기 간의 측정값이 불일치하는 현상이 발생하므로, 이를 일관성 있게 정규화하기 위한 복잡한 센서 캘리브레이션 및 RLOWESS(Robust Locally Weighted Scatterplot Smoothing)와 같은 이상치 제거 전처리 알고리즘이 필수적으로 선행되어야 한다7. 
둘째는 낮은 공간 식별력(Low discernibility)이다. 로비의 중앙이나 넓은 강당 등 강자성 구조물과 멀리 떨어진 공간에서는 자기장 측정값이 거의 유사하여, 위치를 구별해내는 데 한계가 뚜렷하다7. 셋째, 단말기의 방향 및 회전에 극도로 민감하다(Orientation Sensitivity). 사용자가 기기를 들고 걷다가 Z축을 중심으로 단말기를 수평 회전시키면, X축과 Y축 센서가 수집하는 벡터 값이 순식간에 뒤틀려 알고리즘이 이를 전혀 다른 장소로 오인하는 치명적 오류를 낳는다7. 
마지막으로, 구축 비용은 0이지만 오프라인 지문 지도를 생성하기 위해 사람이 직접 해당 건물 구석구석을 돌아다니며 데이터를 기록해야 하는 이른바 사이트 서베이(Site Survey) 수작업의 유지보수 비용(OPEX)이 발생한다7.
3.6. 정확도 또는 성능 특징
 지자기 측위의 공간 정확도는 추출된 자기장 벡터의 시계열 처리 알고리즘의 지능화 수준에 따라 오차 범위가 매우 극적으로 차이 난다32. 단순히 과거의 DTW(동적 시간 워핑) 알고리즘을 사용해 파형을 비교하던 시기에는 위치 오차가 약 1미터 ~ 3.4미터 내외의 범위를 형성하였다32. 
그러나 최근 인공지능이 융합되면서 성능이 크게 상승하였다. 10.2미터 그리드에서 지자기 강도를 시계열 합성곱 신경망(TCN)으로 분석한 연구에서는 오차를 0.7m 미만으로 통제하였다32. 특히 단일 스텝의 헤딩 오차를 제어하기 위해 CNN과 SVM 머신러닝 기법을 앙상블 조합한 모델(CNN-SVM)은 지자기 상태 인식률을 99.38%까지 끌어올리며 자력계 교란 상황에서도 궤적을 복원해냈다36. 
딥러닝 사례인 랜덤 포레스트(Random Forest) 회귀 모델 기반 맵핑 시스템의 경우, 통제된 실험 환경이지만 환경 보정 절차 없이 2D 실내 공간에서 20cm 미만(Sub-20cm), 3D 공간에서 30cm 미만이라는 UWB(초광대역) 통신에 버금가는 로컬라이제이션 성능을 달성하였다33. 
복수의 자력계 배열을 탑재한 MAINS(Magnetic Field Aided INS) 기반 실험에서도, 자기장 이상 환경을 통과한 후 2분간 인프라 없이 항법을 진행하여 위치 오차를 3미터 이하로 억제하는 강건성을 보였다37.
3.7. 실제 활용 사례 (논문, 서비스, 프로젝트 등)

분류	사례 명칭 및 주요 내용 분석	출처
빅테크 연구	IBM 및 Naverlabs의 무보정 딥러닝 지자기 추적 프로젝트: 
IBM 리서치는 자기장의 복잡한 인버전 연산이나 환경별 수동 캘리브레이션 과정을 완전히 폐기하고, 순수하게 데이터 기반(Data-driven)으로 자기장 측정치 자체를 공간 좌표에 직접 맵핑하는 지도 학습(Supervised learning) 랜덤 포레스트 회귀 프레임워크를 발표하였다. 이는 스마트폰의 회전에 독립적인 특징점(Rotation-invariant feature)을 추출해내어 실내뿐만 아니라 실외 공간까지 전이 학습(Transferability)이 가능함을 입증하였다. 유럽 기반의 인공지능 연구소 Naverlabs Europe 역시 자력계 센서와 딥러닝을 결합하여 GPS가 차단된 공간에서 고정밀 맵핑을 구현하는 아키텍처를 공식 블로그를 통해 선보였다.	30
상용 생태계 및 표준화	Apple Indoor Maps Program (IMDF): 
Apple은 자사의 Core Location 생태계를 실내로 확장하기 위해 기관 및 기업 소유주가 내부 지도를 배포할 수 있는 프로그램을 제공한다. 이 시스템의 근간에는 실내 매핑 데이터 포맷(IMDF)이 자리한다. Apple의 위치 보정 기술(IPS)은 단순히 핑거프린팅 기반 Wi-Fi RF 인프라 수신에만 의존하지 않고, Apple Indoor Survey 앱을 통해 작업자가 실내 공간을 거닐며 Wi-Fi RF 패턴과 동시에 스마트폰 내장 센서 기반의 기하학적 자기장, 기압 데이터를 종합적으로 매핑(Survey)하게끔 지시한다. 이 데이터를 Apple 클라우드로 검증하여 제출하면, 건물 내 사용자들의 iPhone 화면에 GPS 수준의 정확도로 파란색 위치 표식(Blue-dot)을 매끄럽게 렌더링하는 엔터프라이즈급 API를 지원한다.	40
상용 솔루션	IndoorAtlas 기술 상용화: 
핀란드의 딥테크 기업 IndoorAtlas는 건물 환경의 자기장 지문을 이용해 모바일 로컬라이제이션 서비스를 실현한 선구자적 서비스 제공자다. 일본 야후(Yahoo! Japan) 등과 전략적 파트너십을 체결하여 대형 역사 및 쇼핑몰 등에서 복잡한 철골 구조물이 만들어내는 자기장 패턴 맵핑 기반의 실내 내비게이션 및 자산 관리 솔루션을 클라우드 기반으로 상용 서비스 중이다.	1
학술 논문	DeepML (Deep Machine Learning) 시스템 연구: 
안드로이드 스마트폰에 탑재된 자력계로 자기장 데이터를 추출하여 딥러닝으로 학습하는 DeepML 연구 논문이다. 이 연구는 기존 시스템들이 단순히 기둥(Pillars)과 같은 랜드마크에 의존해 방 단위(Room-level) 정확도에 머무르던 것을 지적하며, 지역적 지자기장 이상 현상(Anomalies)을 노이즈가 아닌 핵심 피처로 추출하는 심층 신경망을 도입하여 성능 베이스라인을 폭발적으로 증가시켰다.	29


## 4. 스마트폰 기반 실내 로컬라이제이션 기술 간 비교 및 분석
상기 분석된 세 가지 실내 로컬라이제이션 기술은 활용하는 물리적 매개체, 필요로 하는 하드웨어 생태계, 그리고 본질적으로 취약성을 띠는 에러(Error) 메커니즘이 다르다. 이들의 특성을 객관적이고 거시적인 관점에서 대조하여, 각 기술이 어떠한 시나리오에서 최적의 효용을 발휘할 수 있는지, 왜 단일 기술만으로는 한계가 명확한지에 대해 고찰하였다. 

4.1. 3대 핵심 기술 요약 비교표
 다음 표는 세 가지 로컬라이제이션 기술에 대해 요소별로 비교 및 분류한 결과를 나타낸다.

비교 분석 지표	Wi-Fi RTT 및 FTM 포지셔닝	보행자 추측 항법 (PDR)	실내 지자기장 핑거프린팅
위치 산출 원리	단말과 무선 AP 간 패킷 비행시간(ToF) 교차점 연산	가속도/각속도 기반 보폭 및 방향 벡터 누적 합산	지구 자기장 왜곡(이상) 지형도 DB 시계열 매칭
활용 스마트폰 센서	무선 통신 칩셋 및 안테나	IMU 
(가속도계, 자이로스코프, 자력계, 기압계)	3축 자력계 
(Magnetometer)
인프라 독립성	3위 
(사전 측위가 완료된 호환 AP 3~4대 필수 배치)	1위 (공동) 
(외부 인프라 통신 일절 불필요, 자가 연산)	1위 (공동) 
(공간 자체의 고유한 자연 자기장 환경만 이용)
구축/유지 경제성	3위 
(AP 하드웨어 구매, 배선, 소프트웨어 라이선스 발생)	1위 
(스마트폰 내부 앱 기반 구동으로 인프라 추가 비용 0원)	2위 
(인프라 비용은 없으나 사전 오프라인 맵핑 인건비/시간 소요)
최고 위치 정확도	2위 
(기본 1~2m 내외, 최신 az 규격 융합 시 1m 미만)	3위 
(오차율 1% 미만이나 이동 누적 오차 한계로 단독 절대 좌표 산출 불가)	1위 
(AI 딥러닝 융합 최적화 시 20~30cm 미만의 정밀도 도달)
환경 제약(장애물) 극복	3위 
(콘크리트, 철골 구조물 등 비가시선(NLOS) 환경에 가장 취약)	1위 
(통신 음영, 화재 정전 등 물리적 외부 환경의 변화에 제약 없음)	2위 
(모든 장애물을 투과하나, 특이점이 없는 넓은 개방 공간에서 식별력 저하)
장기 연속 운용 안정성	1위 
(인프라 범위 내라면 시간에 따른 오차 발산 없이 일관된 성능 유지)	3위 
(시간 및 보행 거리가 늘어날수록 궤적이 이탈하는 누적 오차 발생)	2위 
(맵핑 유효기간은 영구적이나 스마트폰 기종 편차나 회전 각도에 따른 민감도 존재)
프라이버시 보안성	3위 
(연산은 단말에서 이뤄지나 무선 패킷 교환에 따른 최소한의 네트워크 노출)	1위 (공동) 
(단말기 내부 프로세서 연산으로 외부 유출 원천 차단)	1위 (공동) 
(지도 데이터 다운로드 후 단말기 내부 매칭 가능)

4.2. 기술간 연관 분석 및 시너지(Synergy) 통찰
세 가지 포지셔닝 기술의 한계와 성과를 교차 분석해 보면, 하나의 기술이 무너지는 지점이 다른 기술이 가장 찬란하게 빛을 발하는 지점이라는 기막힌 상호 보완성(Complementarity)의 법칙을 발견할 수 
있다. 이는 최신 실내 로컬라이제이션 학계가 단일 기술의 고도화보다 다중 센서 데이터 융합(Multi-sensor Data Fusion) 프레임워크 연구에 매진하는 본질적 이유이기도 하다4.
1. 신호 왜곡 및 매질 투과성 관점에서의 상보성: 
Wi-Fi RTT는 비행시간을 측정하므로, 두꺼운 콘크리트 기둥, 육중한 철제 방화문, 혹은 거대한 금속제 엘리베이터 샤프트 뒤로 넘어가면 비가시선(NLOS)에 직면하여 패킷이 우회하거나 속도가 지연되면서 심각한 거리 오버슛(Overshoot) 및 오차 편향을 낳는다4. 그러나 역설적이게도 지자기장 핑거프린팅 기술의 관점에서 엘리베이터나 방화문과 같은 막대한 강자성체(Ferromagnetic body)는 이점이다. 이런 철골 구조물은 지구 자기장의 흐름을 가장 크게 비틀기 때문에, 주변의 흔한 복도 공간과는 확연히 대비되는 자기장 이상(Magnetic Anomaly) 파형을 생성한다3. 즉, 무선 통신(Wi-Fi)의 구조적 사각지대에서, 지자기 센서는 가장 선명하고 뚜렷한 식별력을 지닌 랜드마크 좌표를 제공함으로써 무선 통신의 공백을 채울 수 있다.
2. 시계열적 오차 발산과 절대 좌표 보정 역학 (Drift vs Reset): 
PDR 기술은 사람이 발을 딛고 회전하는 미세한 보행 역학계(Gait dynamics)를 초당 수백 번의 샘플링으로 추적해내는 민첩성(Agility)을 지녔다5. 하지만 PDR은 시간이 흐를수록 오차의 누적 텐서가 팽창하여 결국 지도의 외벽을 뚫고 지나가는 궤적을 그리게 된다5. 반면, Wi-Fi RTT나 지자기 핑거프린팅은 1초 혹은 그보다 더 넓은 간격으로 위치를 스캔하지만, 일단 매칭이 되면 절대적인 세계 좌표계의 고정점(Absolute anchor point)을 제공한다. 따라서 최근 학계의 EKF(확장 칼만 필터)나 딥러닝 융합 논문들은 PDR을 추적의 연속적인 뼈대(Baseline)로 지속 구동시키되, 사용자가 Wi-Fi AP 3대 이상이 선명하게 스캔되는 로비로 나오거나, 강력한 철골 지지대가 만든 지자기 특이점을 스치고 지나가는 찰나의 순간에 도출된 절대 위치 좌표를 강제 주입하여 PDR 알고리즘의 오차 누적 카운터를 0으로 깎아내는(Reset) 협력적 융합 시스템을 표준 아키텍처로 수용하고 있다24.
3. 인공지능(AI/ML)의 진입으로 인한 인프라 패러다임의 혁신: 
최근 실내 로컬라이제이션 기술의 가장 주요한 동인은 센서 하드웨어의 개선이 아니라 데이터를 다루는 인공지능 소프트웨어 파이프라인의 진화이다. 과거 PDR 알고리즘은 사용자가 스마트폰을 보면서 걷는지 통화하며 걷는지 일일이 지정해 줘야만 보폭 상수를 연산할 수 있었으나, 최근에는 의사결정 트리와 SVM 앙상블이 밀리초 단위로 파지 모드와 보행 성별, 걸음의 스피드를 97% 이상의 확률로 자동 적응(Adaptive) 분류해 내어 오차율을 1% 이하로 압축시켰다5. 
가장 큰 문제 요소인 지자기 기술의 기기 간 편차나 노동 집약적인 수동 맵핑(Site survey) 문제 역시, IBM 연구소가 증명한 랜덤 포레스트(Random Forest) 및 RNN 회귀 모델 등 데이터 주도형(Data-driven) 딥러닝 네트워크를 통해 소프트웨어적으로 캘리브레이션 튜닝을 대체함으로써 해결되는 양상이다33. 이러한 AI 기반의 알고리즘 고도화는 공간 소유주로 하여금 값비싼 AP나 UWB 앵커를 추가로 매설하는 대규모 인프라 자본 지출(CAPEX) 없이도 기존 스마트폰의 관성/지자기 자원만으로 서브 미터(Sub-meter) 급 내비게이션 환경을 구현할 수 있도록 경제적 패러다임을 혁신하고 있다.
종합하자면 단일 로컬라이제이션 기술의 한계를 고집하는 시대는 종식되었다고 볼 수 있겠다. 다변화되고 극도로 복잡한 실내 건축물이라는 지형적 맥락 속에서 GPS의 빈자리를 대체하기 위해서는, 통신의 안정성(Wi-Fi RTT), 관성의 민첩함과 연속성(PDR), 지자기의 무선 간섭 면역력(Magnetic Fingerprinting)이 맞물려 작동하는 하이브리드 플랫폼이 필요하다.


## References
1.	Indoor Localization with Smartphones - Colorado State University, https://www.engr.colostate.edu/~sudeep/wp-content/uploads/j40.pdf
2.	Indoor Positioning with Wi-Fi Location: A Survey of IEEE 802.11mc/az/bk Fine Timing Measurement Research - arXiv, 
https://arxiv.org/pdf/2509.03901
3.	Indoor Localization Using Magnetic Fields - UNT Digital Library, https://digital.library.unt.edu/ark:/67531/metadc103371/m2/1/high_res_d/dissertation.pdf
4.	On Indoor Localization Using WiFi, BLE, UWB, and IMU Technologies - PMC, https://pmc.ncbi.nlm.nih.gov/articles/PMC10610672/
5.	Sensors | Free Full-Text | A Context-Aware Smartphone Based 3D ..., https://www.mdpi.com/1424-8220/22/24/9968
6.	Indoor Smartphone Localization: A Hybrid WiFi RTT-RSS Ranging Approach - IEEE Xplore, 
https://ieeexplore.ieee.org/iel7/6287639/6514899/08924707.pdf
7.	Sensors | Free Full-Text | Analysis of Magnetic Field Measurements ..., https://www.mdpi.com/1424-8220/22/11/4014
8.	Wi-Fi location: ranging with RTT | Connectivity | Android Developers, https://developer.android.com/develop/connectivity/wifi/wifi-rtt
9.	IEEE 802.11mc - Wikipedia, 
https://en.wikipedia.org/wiki/IEEE_802.11mc
10.	An In-Depth Guide to Indoor Location Services - Cisco Spaces, https://spaces.cisco.com/what-are-indoor-location-services-a-guide/
11.	Wi-Fi RTT Ranging Performance Characterization and Positioning ..., https://ieeexplore.ieee.org/document/9151400/
12.	WiFi-RTT Indoor Positioning - IEEE Xplore,
https://ieeexplore.ieee.org/document/9110232/
13.	WiFi RTT Indoor Positioning Method Based on Gaussian Process Regression for Harsh Environments | IEEE Journals & Magazine,
http://ieeexplore.ieee.org/document/9274298
14.	A Testing and Evaluation Framework for Indoor Navigation and Positioning Systems - MDPI,
https://www.mdpi.com/1424-8220/25/7/2330
15.	Cisco Unified Wireless Location-Based Services,
https://www.cisco.com/en/US/docs/solutions/Enterprise/Mobility/emob30dg/Locatn.pdf
16.	Cisco Spaces: Advanced Location Based Services for Enterprise Networks, https://www.ciscolive.com/c/dam/r/ciscolive/apjc/docs/2025/pdf/BRKEWN-2658.pdf
17.	Daily Action Dead Reckoning Using Smartphone Sensors - CEUR-WS.org,
https://ceur-ws.org/Vol-2498/short50.pdf
18.	Smartphone-Based Indoor Localization Systems: A Systematic Literature Review - MDPI, 
https://www.mdpi.com/2079-9292/12/8/1814
19.	Pedestrian Dead Reckoning Based on Motion Mode Recognition Using a Smartphone, 
https://www.mdpi.com/1424-8220/18/6/1811
20.	Indoor Localization Methods for Smartphones with Multi-Source Sensors Fusion: Tasks, Challenges, Strategies, and Perspectives - MDPI, https://www.mdpi.com/1424-8220/25/6/1806
21.	Full article: Context-assisted personalized pedestrian dead reckoning localization with a smartphone - Taylor & Francis, https://www.tandfonline.com/doi/full/10.1080/10095020.2024.2338225
22.	A Novel Distance Estimation Framework for PDR Based Indoor Localization Using RNNs,
https://ieeexplore.ieee.org/document/10271636/
23.	A Novel Distance Estimation Framework for PDR Based Indoor Localization Using RNNs - IEEE Xplore, https://ieeexplore.ieee.org/iel7/10271384/10271386/10271636.pdf
24.	Gyroscope-constrained magnetometer PDR/Wi-Fi indoor positioning algorithm - PMC - NIH, 
https://pmc.ncbi.nlm.nih.gov/articles/PMC12551869/
25.	A Survey on Fusion-Based Indoor Positioning - IEEE Xplore, https://ieeexplore.ieee.org/iel7/9739/9031610/08889728.pdf
26.	A Survey of Selected Indoor Positioning Methods for Smartphones - IEEE Xplore, https://ieeexplore.ieee.org/document/7782316/
27.	A Review of Indoor Localization Methods Leveraging Smartphone Sensors and Spatial Context - PMC, 
https://pmc.ncbi.nlm.nih.gov/articles/PMC11548474/
28.	Enhancing Performance of Magnetic Field Based Indoor Localization Using Magnetic Patterns from Multiple Smartphones - PMC, https://pmc.ncbi.nlm.nih.gov/articles/PMC7249215/
29.	Indoor Localization Using Smartphone Magnetic and Light Sensors: a Deep LSTM Approach - Samuel Ginn College of Engineering, https://www.eng.auburn.edu/~szm0001/papers/DeepML_journal.pdf
30.	[2108.11824] Magnetic Field Sensing for Pedestrian and Robot Indoor Positioning - arXiv, 
https://arxiv.org/abs/2108.11824
31.	Magnetic-Field-Based Indoor Positioning Using Temporal Convolutional Networks - MDPI, 
https://www.mdpi.com/1424-8220/23/3/1514
32.	Current Status and Future Trends of Meter-Level Indoor Positioning Technology: A Review, 
https://www.mdpi.com/2072-4292/16/2/398
33.	Calibration-Free Induced Magnetic Field Indoor and Outdoor Positioning via Data-Driven Modeling - arXiv, 
https://arxiv.org/html/2602.00817v1
34.	Analysis of Magnetic Field Measurements for Indoor Positioning - PMC - NIH, 
https://pmc.ncbi.nlm.nih.gov/articles/PMC9183029/
35.	AMID: Accurate Magnetic Indoor Localization Using Deep Learning - PMC - NIH, https://pmc.ncbi.nlm.nih.gov/articles/PMC5982601/
36.	Improving Indoor Pedestrian Dead Reckoning for Smartphones under Magnetic Interference Using Deep Learning - PMC, https://pmc.ncbi.nlm.nih.gov/articles/PMC10708641/
37.	MAINS: A Magnetic-Field-Aided Inertial Navigation System for Indoor Positioning - Search for publications in DiVA, https://liu.diva-portal.org/smash/get/diva2:1855561/FULLTEXT01.pdf
38.	MAINS: A Magnetic Field Aided Inertial Navigation System for Indoor Positioning - arXiv,
https://arxiv.org/abs/2312.02599
39.	Magnetic sensor-based localization and deep learning - NAVER LABS Europe, https://europe.naverlabs.com/blog/magnetic-sensor-based-localization-and-deep-learning/
40.	Introducing the Indoor Maps Program - WWDC19 - Videos - Apple Developer, https://developer.apple.com/videos/play/wwdc2019/245/
41.	© 2019 Apple Inc. All rights reserved. Redistribution or public display not permitted without written permission from Apple., https://devstreaming-cdn.apple.com/videos/wwdc/2019/245hrnwbhlkgmim8y/245/245_introducing_the_indoor_maps_program.pdf?dl=1
42.	Apple Indoor Positioning for ArcGIS Indoors - Esri, https://www.esri.com/arcgis-blog/products/arcgis-indoors/indoor-gis/1948632-2

