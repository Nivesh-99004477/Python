def digiRoot(n):
    if n == "0":
        return 0


    ans = 0
    for i in range(0, len(n)):
        ans = (ans + int(n[i])) % 9


    if (ans == 0):
        return 9
    else:
        return ans % 9





