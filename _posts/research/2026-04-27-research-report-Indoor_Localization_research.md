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


## Wi-Fi RTT (Round-Trip-Time) 및 FTM 기반 실내 로컬라이제이션 기술
dataset description, environment, procedure

## 보행자 추측 항법 (Pedestrian Dead Reckoning, PDR) 및 다중 센서 융합 Localization 기술
metric values, interpretation.

## 실내 지자기장 지문 (Magnetic Field Fingerprinting) 기반 로컬라이제이션 기술 
assumptions list, potential biases

## 스마트폰 기반 실내 로컬라이제이션 기술 간 비교 및 분석
- Environment:
- Data:
- Commands:

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

