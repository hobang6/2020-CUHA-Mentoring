# 이번 과제는 업 다운 게임입니다.
# 사용자가 0을 입력하면 '프로그램 종료', 1을 입력하면 게임을 시작합니다.
# 변수 num에 랜덤 모듈을 사용하여 1~100 사이의 난수를 정답으로 저장해 주세요.
# 랜덤 모듈의 사용법은 구글 검색을 통해 확인해 주세요. (파이썬 랜덤 모듈, 파이썬 랜덤 함수 등의 키워드 활용)
# 정답을 맞힐 때까지 UP, DOWN 을 출력해 주세요.
# 정답을 맞히면 num에는 다시 1~100 사이의 난수가 저장되어야 합니다.
# 정답 입력을 시도한 횟수를 변수 count에 저장해 주세요.
# 게임마다 정답 입력을 시도한 횟수를 '시도한 횟수 : n'의 형식으로 파일에 저장해 주세요. (개행 필수)
# 프로그램은 무한 루프로 작동되어야 합니다.

# ex)
# 0. 프로그램 종료    1. 게임 시작 : 1 (사용자가 1 입력, num = 10)
# 숫자를 입력하세요 : 7
# UP
# 숫자를 입력하세요 : 9
# UP
# 숫자를 입력하세요 : 11
# DOWN
# 숫자를 입력하세요 : 10
# 정답!   (log.txt에 '시도한 횟수 : 4' 저장)
# 0. 프로그램 종료    1. 게임 시작 : 1 (사용자가 1 입력, num = 50)
# 숫자를 입력하세요 : 40
# UP
# 숫자를 입력하세요 : 60
# DOWN
# 숫자를 입력하세요 : 50
# 정답!   (log.txt에 '시도한 횟수 : 3' 저장)
# 0. 프로그램 종료    1. 게임 시작 : 0 (사용자가 0 입력)
# (프로그램 종료)
#
# <log.txt 파일>
# 시도한 횟수 : 4
# 시도한 횟수 : 3

import random


def main():
    while True:
        num = random.randint(1, 100)
        count = 0
        txt = int(input('0. 프로그램 종료    1. 게임 시작 : '))

        if txt == 0:
            break

        while True:
            user = int(input('숫자를 입력하세요 : '))
            count += 1

            if user < num:
                print('UP')

            elif user > num:
                print('DOWN')

            else:
                print('정답!')
                with open('./log.txt', 'a') as f:
                    f.write('시도한 횟수 : ' + str(count) + '\n')
                # with 문에서는 해당 with 문을 탈출하면 자동으로 f.close() 가 수행됨 따라서 작성할 필요 없음
                break


if __name__ == '__main__':
    main()