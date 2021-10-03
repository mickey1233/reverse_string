def reversetring(s):
    s
    # 解一
    # s.reverse()
    # print(s)
    # 解二
    end = 1
    temp = ""
    for i in range(int(len(s)/2)):
        temp = s[i]
        s[i] = s[-end]
        s[-end] = temp
        end = end + 1
    print(s)


if __name__ == "__main__":
    reversetring(["h", "e", "l", "l", "o"])
    reversetring(["H", "a", "n", "n", "a", "h"])
