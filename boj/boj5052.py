t = int(input())
for _ in range(t):
    phone = []
    n = int(input())
    for _ in range(n):
        phone.append(input())
    phone.sort()
    
    for i in range(n-1):
        if phone[i] in phone[i+1][:len(phone[i])]:
            print("NO")
            break
    else:
        print("YES")
