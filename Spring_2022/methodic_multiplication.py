def main():
    x = input()
    y = input()
    S_in_x = x.count('S')
    S_in_y = y.count('S')
    z = S_in_x * S_in_y
    z = 'S('* z + '0' + ')' * z
    print(z)



if __name__ == "__main__":
    main()