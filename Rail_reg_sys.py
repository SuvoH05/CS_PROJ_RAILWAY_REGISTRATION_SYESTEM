def vow(a):
    p=len(a)
    v=""
    c=""
    for i in range(p):
        if (a[i]== "a" or a[i]== "e" or a[i]== "i" or a[i]== "o" or a[i]== "u") :
            v+= a[i]
        else:
            c+=a[i]
    vl = sorted(v)
    s1=""
    for i in vl:
        s1+=i
    fina = s1+c
    final = fina+" "
    return final
def kiddo(s):
    str1=s.split()
    final1=""
    for i in str1:
        final1+=vow(i)
    print(final1)


s = input("Enter your string: ")
print(s)
kiddo(s)