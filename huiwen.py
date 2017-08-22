# start = '信言不美'
# final = start+','+start[::-1]
# print(final)


# L = [1]
# while len(L)<11:
#     print(L)
#     L.append(0)
#     print(L)
#     L = [L[i - 1] + L[i] for i in range(len(L))]
#     print(L)

ret = [1]
while len(ret)<11:
        # print(ret)
        for i in range(1, len(ret)):
            ret[i] = pre[i]+pre[i-1]
        ret.append(1)
        pre = ret[:]
        print(pre)
        # pre = ret
        # print(pre)