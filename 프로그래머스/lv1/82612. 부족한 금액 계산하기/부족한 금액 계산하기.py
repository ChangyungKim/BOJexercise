def solution(price, money, count):
    answer = 0
    sum_count=0
    for i in range(1,count+1):
        sum_count+=i
    if money<sum_count*price:
        answer=sum_count*price-money
    else:
        answer=0
    
    return answer