# $0.25(Q), $0.10(D), $0.05(N), $0.01(P)
# 동전 갯수를 최소!
Q, D, N, P = 25, 10, 5, 1
# 각 동전별 갯수

T = int(input()) # 테스트케이스 갯수
for i in range(T):
    C = int(input()) # 센트(C)
    Qn, Dn, Nn, Pn = 0, 0, 0, 0
    Qn = C//Q
    Dn = (C % Q) // D 
    Nn = ((C % Q) % D) // N
    Pn = (((C % Q) % D) % N) // P
    print(Qn, Dn, Nn, Pn) 




# 개선된 코드(divmod() 사용)
Q, D, N, P = 25, 10, 5, 1

T = int(input())  # 테스트케이스 갯수
for _ in range(T):
    C = int(input())  # 센트(C)
    
    Qn, C = divmod(C, Q)
    Dn, C = divmod(C, D)
    Nn, Pn = divmod(C, N)
    
    print(Qn, Dn, Nn, Pn)