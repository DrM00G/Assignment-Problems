sumFactors n = sum([x| x <-[1..n], n `mod` x == 0])
main = print(sumFactors 10) -- should come out to 1+2+5+10 = 18