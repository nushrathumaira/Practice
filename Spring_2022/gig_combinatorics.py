def main():
    count1 = 0
    count12 = 0
    res = 0 #output res whenever you see 3?
    M = 1000000007
    for _ in range(int(input())):
        cur = int(input())
        #print(cur)
        if cur== 1:
            count1 += 1
        elif cur == 2:
            count12 = ((2 * count12)+count1) % M
        else:
            res = (res + count12) % M
    print(res)
                  



if __name__ == "__main__":
    main()