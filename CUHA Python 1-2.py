# 문자열 인덱스를 이용하여 "안녕하세요. 저는 학생입니다."를 출력해 주세요. * 띄어쓰기 꼭 지켜주세요.

string = "안녕하세요. 저는 사람입니다."
student = "학생"

print(string[0:10] + student + string[12:16])

# 다음과 같이 [0:X]에서는 0을 생략 가능하고, [X:문자열의 끝]에서는 문자열의 끝을 생략 가능함
# print(string[:10] + student + string[12:])
