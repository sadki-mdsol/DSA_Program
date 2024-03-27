# def get_ch(s,next,prev):
    



s = "baab"
ch = "b"

curr = next = prev = 0
arr =[]



while curr < len(s):
    if prev != 0  and curr == next:
        prev = next
    while next < len(s) and s[next]!=ch and curr == next:
        next+=1
    if next == len(s):
        next = prev
    if prev ==0 :
        prev = next
    print("arr:{} curr:{} prev:{} next:{} ".format(arr,curr,prev,next))
    # break
    arr.append(min(abs(prev-curr),abs(next-curr)))
    curr+=1
        

print(arr)
