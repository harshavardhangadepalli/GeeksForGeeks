import pandas as pd
df1 = pd.read_csv('signals_new.csv')
df2 = pd.read_csv('strategy.csv')
all_strategies = df2['name']
repeated = df1['strategy']
ids = df1['id']
ans = [all_strategies[0]]
j = 0
for i in range(1,len(repeated)):
    if repeated[i] == repeated[i-1]:
        ans.append(all_strategies[j])
    if repeated[i] != repeated[i-1]:
        j += 1
        ans.append(all_strategies[j])
final_list = []
for i in range(len(repeated)):
    final_list.append([ids[i],repeated[i],ans[i]])
new_df = pd.DataFrame(final_list, columns =["id","strategy_present","actual_strategy"])
new_df.to_excel("output1.xlsx")