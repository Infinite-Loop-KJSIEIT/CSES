for i in range(1,int(input())+1):
    total_ways = (((i*i))*((i*i)-1))/2
    kills = (i-1)*(i-2)*2*2
    print(int(total_ways - kills))