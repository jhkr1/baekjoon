# i % 3 == 0 and i % 5 == 0 -> FizzBuzz
# i % 3 == 0 and i % 5 != 0 -> Fizz
# i % 3 != 0 and i % 5 == 0 -> Buzz
# i % 3 != 0 and i % 5 != 0 -> i 출력


##  직접 작성한 코드 ##
# def FizzBuzz(i):
#     if (i % 3 == 0 and i % 5 == 0):
#         return 'FizzBuzz'
#     elif(i % 3 == 0 and i % 5 != 0):
#         return 'Fizz'
#     elif(i % 3 != 0 and i % 5 == 0):
#         return 'Buzz'
#     else:
#         return i




# a = input()
# b = input()
# c = input()



# while(1):
# # 첫 번째 해야할일 
# # 입력 받은 숫자를 is.digit()으로 판별 후 int 타입으로 변경.
#     if(a.isdigit()):
#         result = int(a)+3
#         print(FizzBuzz(result))
#         break
#     elif(b.isdigit()):
#         result = int(b)+2
#         print(FizzBuzz(result))
#         break
#     elif(c.isdigit()):
#         result = int(c)+1
#         print(FizzBuzz(result))
#         break



## 개선된 코드 ##
# FizzBuzz 함수 정의
def FizzBuzz(i):
    if i % 3 == 0 and i % 5 == 0:
        return "FizzBuzz"
    elif i % 3 == 0:
        return "Fizz"
    elif i % 5 == 0:
        return "Buzz"
    else:
        return i

# 입력값 처리 및 다음 FizzBuzz 계산
def process_input(inputs):
    for idx, value in enumerate(inputs):
        if value.isdigit():  # 숫자인지 확인
            result = int(value) + (3 - idx)  # 위치에 따라 적절한 값 추가
            return FizzBuzz(result)
    return "Invalid input"  # 유효한 숫자가 없는 경우

# 입력 받기
inputs = [input() for _ in range(3)]

# 결과 출력
print(process_input(inputs))




