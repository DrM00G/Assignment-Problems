def Factorial(x):
    if x != 0:
        result = x
        for n in range(1,x):
            result*= n
    else:
        return 1
    return result

def Probability(num_heads, num_flips):
    num_possibilities = 2**(num_flips)
    num_heads = Factorial(num_flips)/(Factorial(num_heads)*Factorial(num_flips - num_heads))
    return num_heads/num_possibilities


