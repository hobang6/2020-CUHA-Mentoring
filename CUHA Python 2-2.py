# 현재 컴퓨터가 랜덤으로 가위, 바위, 보 중 하나를 출력하는 스크립트가 작성되어 있습니다.
# input 함수를 사용해 사용자에게 문자열을 입력받아주세요. 
# 사용자가 이겼다면 "승리!", 비겼다면 "무승부!", 졌다면 "패배!"를 출력해주세요.
#
# 문자열은 반드시 가위, 바위, 보를 입력받아야 합니다.
# 그 외의 문자열을 입력받으면 "오류 발생!" 문자열을 출력하고 프로그램을 종료해주세요.
# 
# 프로그램은 무한 루프로 작동되어야 합니다. (while 문 사용)

import random   # 랜덤 모듈 import

arr = ['가위', '바위', '보']

while True:
    pc_choice = random.choice(arr)      # arr 배열의 요소 중 하나를 랜덤으로 선택
    print("PC:", pc_choice)
    user_choice = input("User: ")

    if user_choice not in arr:      # 사용자가 '가위', '바위', '보' 외의 문자열을 입력했을 경우
        print("오류 발생!")
        break

    if pc_choice == user_choice:
        print("무승부!")
        
    elif pc_choice == "가위" and user_choice == "바위":
        print("승리!")
    elif pc_choice == "가위" and user_choice == "보":
        print("패배!")
        
    elif pc_choice == "바위" and user_choice == "가위":
        print("패배!")
    elif pc_choice == "바위" and user_choice == "보":
        print("승리!")
        
    elif pc_choice == "보" and user_choice == "가위":
        print("승리!")
    elif pc_choice == "보" and user_choice == "바위":
        print("패배!")
