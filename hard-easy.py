def hard_easy(a, b):
    result = 0
    for _ in range(abs(a)):
        result += abs(b)
    if (a < 0 and b > 0) or (a > 0 and b < 0):
        result = -result
    elif a == 0 or b == 0:
        result = 0
    print("Only '+' and '-' operations:", result)
    print("                  Expected:", a * b)
    
hard_easy(2, 3)
hard_easy(-2, 3)
hard_easy(-2, -3)
hard_easy(-34553, -343535353)
hard_easy(-0, -343535353)
hard_easy(10, 0)
