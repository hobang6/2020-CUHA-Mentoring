# 입력받은 인자의 구구단을 출력하는 함수 gugudan을 작성해 주세요
# 입력받은 인자 n에 대하여 n!을 출력하는 함수 factorial을 작성해 주세요
#
# 사용자의 입력에 따라 함수를 호출하는 메인 함수 main을 작성해 주세요
# main 함수는 무한 루프로 작동되어야 합니다.
# 사용자가 'n단'을 입력하면 gugudan 함수를 호출합니다
# 사용자가 'n!'을 입력하면 factorial 함수를 호출합니다
# 사용자가 입력한 문자열에 '단' 또는 '!'가 없다면 프로그램을 종료해 주세요
#
# ex)
# 명령을 입력해 주세요 : 5단  (사용자가 5단 입력)
# 5 x 1 = 5
# (생략)
# 5 x 9 = 45
# 명령을 입력해 주세요 : 4!  (사용자가 4! 입력)
# 24
# 명령을 입력해 주세요 : 안녕
# (프로그램 종료)


def gugudan(n):
    for i in range(1, 10):
        print('%d x %d = %d' % (n, i, n * i))
    # 반환값이 없을 때는 return 을 작성하지 않아도 무방함, 자동으로 return None 으로 인식함
    # 반환값이 없을 경우, return == return None == (return 작성 X), 세 경우 모두 사용 가능하며 아무것도 반환하지 않는다는 의미임


def factorial(n):
    return 1 if n == 1 else n * factorial(n - 1)    # 아래 코드의 축약형
    # 위 코드와 아래 코드는 완전히 동일한 코드임
    # if n == 1:
    #     return 1
    # else:
    #     return n * factorial(n - 1)


def main():
    while True:
        order = input('명령을 입력해 주세요 : ')
        if '단' in order:
            gugudan(int(order[:-1]))        # ex) text = 'abcd', text[:-1] = 'abc', text[-1:] = 'dcba'

        elif '!' in order:
            print(factorial(int(order[:-1])))

        else:
            break
    return


if __name__ == '__main__':
    main()
