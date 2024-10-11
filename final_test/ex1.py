count = 0
cast = []
def cal(n):
    if n % 2 == 0:
        cast.append(2)
        new_n = n/2
        return cal(int(new_n))
    else:
        cast.append(n)
        return cast
    
def prime_number(cast):
    i = 0
    sum = 0
    while i < len(cast):
        sum += cast[i]
        i += 1
    if (sum % 2 != 0 and sum % 3 != 0 and sum % 5 != 0 and sum % 7 != 0 and sum % 11 != 0):
        return f"{sum} เป็นจำนวนเฉพาะ" 
    else:
        return f"{sum} ไม่เป็นจำนวนเฉพาะ"

print(cal(int(input("Enter the number: "))))
print(prime_number(cast))

