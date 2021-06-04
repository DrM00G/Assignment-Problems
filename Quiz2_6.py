import pandas as pd
import numpy as np
df = pd.read_csv('/home/runner/assignment-problems/quiz_2_6_data.csv')


# keep_cols = ['training_hours']
# train_hours_df = df[keep_cols]

# print("mean training hours:"+str(train_hours_df.mean()))

# keep_cols1 = ['target']
# target_df = df[keep_cols1]

# count_1 = 0
# count=0
# for n in target_df["target"]:
#     if n==1:
#         count_1+=1
#     count+=1
# print(count_1/count)

# keep_cols = ['city']
# city_code_df = df[keep_cols]
# codes=[]
# for code in city_code_df['city']:
#     if code not in codes:
#         codes.append(code)
# code_dict = dict.fromkeys(codes,0)
# for code in city_code_df['city']:
#     code_dict[code]+=1
# max_code=None
# max_pop=0
# for key in code_dict:
#     if code_dict[key]>max_pop:
#         max_code=key
#         max_pop=code_dict[key]
# print(max_code)
# print(max_pop)

#e
# keep_cols = ['city']
# city_code_df = df[keep_cols]
# codes=[]
# for code in city_code_df['city']:
#     if code not in codes:
#         codes.append(code)
# print(codes)

#f
keep_cols = ['company_size']
comp_siz_df = df[keep_cols]
comp_count=0
for emploees in comp_siz_df['company_size']:
    if str(emploees)!= "":
        if '-' in str(emploees):

            print(emploees)
    else:
        print(emploees)
        comp_count+=1
print(comp_count)


