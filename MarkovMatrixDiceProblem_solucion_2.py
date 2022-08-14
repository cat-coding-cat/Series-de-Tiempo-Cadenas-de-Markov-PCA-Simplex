import pandas as pd

data = pd.read_csv("./DiceThrows.csv")
#print(data)

df = pd.DataFrame(data)
df = df["DiceA"]
transitions = df.values.tolist()

print('transitions')
print(transitions)
#
M = [[0]*6 for _ in range(6)]
#print(M)
#
for i in range(len(transitions)-1):
#    print(transitions[i],transitions[i+1])
    j = transitions[i]; k = transitions[i+1]
#    print(j, k)
    M[j-1][k-1] += 1
#
##print(M)
for row in M:
    print(row)

