# 1. 반복문을 사용해 리스트 "arr" 에 숫자 1부터 10을 추가해주세요.
# 2. input 함수를 사용해 사용자에게 문자열을 입력받아주세요.
# 3. "짝수"를 입력받으면 리스트에 있는 숫자 중 짝수만, "홀수"를 입력받으면 홀수만 한 줄에 출력해주세요.
# 4. "짝수" 또는 "홀수"가 아닌 문자열을 입력받으면 "오류 발생!" 문자열을 출력하고 프로그램을 종료해주세요.
# 5. 프로그램은 무한 루프로 작동되어야 합니다. (while 문 사용)

# 숫자는 다음과 같이 한 줄에 출력되어야 합니다.
# 1 3 5 7 9
# 2 4 6 8 10

# ex)
# 문자열 입력 : 짝수       (사용자가 "짝수" 입력)
# 2 4 6 8 10
# 문자열 입력 : 홀수       (사용자가 "홀수" 입력)
# 1 3 5 7 9
# 문자열 입력 : 안녕       (사용자가 "안녕" 입력)
# 오류 발생!
# (프로그램 종료)

arr = []

for i in range(10):
    arr.append(i + 1)

print("문자열 입력 : ", end='')

while True:
    text = input()

    if text not in ["짝수", "홀수"]:
        print("오류 발생!")
        break

    for num in arr:
        if text == "짝수" and num % 2 == 0:
            print(num, end=' ')
        elif text == "홀수" and num % 2 != 0:
            print(num, end=' ')

    print("\n문자열 입력 : ", end='')
