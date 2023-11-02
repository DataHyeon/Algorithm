# 최대 공약수
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def solution(numer1, denom1, numer2, denom2):
    # 분모의 최소공배수(LCM)를 구함
    lcm_denom = denom1 * denom2 // gcd(denom1, denom2)
    
    # 분모를 통일하고 분자를 더함
    total_numer = (numer1 * (lcm_denom // denom1)) + (numer2 * (lcm_denom // denom2))
    
    # 분자와 분모의 최대공약수로 나누어 기약분수를 만듦
    gcd_numer_denom = gcd(total_numer, lcm_denom)
    
    return [total_numer // gcd_numer_denom, lcm_denom // gcd_numer_denom]