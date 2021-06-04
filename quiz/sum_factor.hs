sumFactors n = sum([x*x*x| x <-[1..n]])
main = print(sumFactors 10) -- should come out to 1+2+5+10 = 18