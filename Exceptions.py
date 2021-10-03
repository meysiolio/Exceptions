T = int(input())
result = []

for i in range(T):
    a, b =  input().split()
    try:
        c = int(a)//int(b)
        result.append(c)
    except ZeroDivisionError as e:
        result.append(f'Error Code: integer division or modulo by zero')
    except ValueError as e:
        result.append(f'Error Code: {e}')
    
for j in result:
    print(j)