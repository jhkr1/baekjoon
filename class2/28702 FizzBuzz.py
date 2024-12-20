# i % 3 == 0 and i % 5 == 0 -> FizzBuzz
# i % 3 == 0 and i % 5 != 0 -> Fizz
# i % 3 != 0 and i % 5 == 0 -> Buzz
# i % 3 != 0 and i % 5 != 0 -> i 출력

def FizzBuzz(i):
    if (i % 3 == 0 and i % 5 == 0):
        return 'FizzBuzz'
    elif(i % 3 == 0 and i % 5 != 0):
        return 'Fizz'
    elif(i % 3 != 0 and i % 5 == 0):
        return 'Buzz'
    else:
        return i




a = input()
b = input()
c = input()



while(1):
# 첫 번째 해야할일 
# 입력 받은 숫자를 is.digit()으로 판별 후 int 타입으로 변경.
    if(a.isdigit()):
        result = int(a)+3
        print(FizzBuzz(result))
        break
    elif(b.isdigit()):
        result = int(b)+2
        print(FizzBuzz(result))
        break
    elif(c.isdigit()):
        result = int(c)+1
        print(FizzBuzz(result))
        break
    






