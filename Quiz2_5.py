import pandas as pd
import numpy as np
df = pd.read_csv('/home/runner/assignment-problems/quiz/StudentsPerformance.csv')

keep_cols = ['math score']
math_df = df[keep_cols]

# print(math_df[3:])

print("mean math:"+str(math_df.mean()))

# print(df['math score'].apply(lambda entry: df["test preparation course"]!="none").mean())


