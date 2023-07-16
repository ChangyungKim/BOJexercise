import sys
while True:
    try:
        n=int(sys.stdin.readline().rstrip())
    except:
        break
    num=str(1)
    while(True):
        if int(num)%n==0:
            break
        else:
            num=num+str(1)
    print(len(num))
