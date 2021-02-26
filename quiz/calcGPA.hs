calcGPA xs = sum [if x == "A" then 4 else if x == "B" then 3 else if x == "C" then 2 else if x == "D" then 1 else if x == "F" then 0 | x <- xs] `div` length xs



main = print(calcGPA(["A", "B", "B", "C", "C", "C", "D", "F"]))