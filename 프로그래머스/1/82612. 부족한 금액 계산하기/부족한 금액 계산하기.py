def solution(price, money, count):
    don = 0
    for i in range(1, count+1):
        don += price * i
    
    return don - money if don > money else 0
        
        