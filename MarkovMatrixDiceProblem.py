import pandas as pd

data = pd.read_csv("./DiceThrows.csv")

df = pd.DataFrame(data)

df = df["DiceA"]

transitions = df.values.tolist()

print(transitions)


def rank(c):
    return ord(str(c)) - ord(str(1))

T = [rank(c) for c in transitions]

print('------------------------------')
print(T)

M = [[0] * 6 for _ in range(6)]
print('------------------------------')

print(M)

#a = ("Gato", "Perro", "Raton")
#b = ("rojo", "azul", "morado")
#x = zip(a, b)
#print(tuple(x))
#(('Gato', 'rojo'), ('Perro', 'azul'), ('Raton', 'morado'))

print(tuple(zip(T,T[1:])))

for (i,j) in zip(T,T[1:]):
    print(i,j)
    M[i][j] += 1
print("--------  M  ---------")
print(M)


for row in M:
    n = sum(row)
    if n > 0:
        row[:] = [f/sum(row) for f in row]

print(M)        
























