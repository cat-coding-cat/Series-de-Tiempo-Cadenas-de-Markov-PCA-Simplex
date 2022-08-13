#--------------------------------------------------------------------------------
# El analisis de componentes principales puede ser utilizado para diversas cosas.
# Por ejemplo para reducir las dimensiones de un dataset y poder visualizarlo o
# acelerar la velocidad de ejecusion de los algoritmos de machine learning.
# En este ejemplo reducimos el iris dataset de 4 a dos dimensiones para poder visualizarlo.
#--------------------------------------------------------------------------------

import pandas as pd
from sklearn.preprocessing import StandardScaler # para escalar los datos



## Usaremos el dataset iris
df = pd.read_csv("./iris.csv")

# si tenemos el dataset iris.csv en el lugar correcto debería desplegarse el dataset sin problemas
# recuerda que la dirección "./iris.csv" es propia de sistemas operativos unix-based.
print(df)

# Ahora tenemos que ESCALAR o ESTANDARIZAR LOS DATOS ES DECIR
# necesitamos que tengan
#  mean = 0
#  variance = 1

# Para aplicar algoritmos como PCA es necesario estandarizar los datos.
# Hay muchas referencias sobre feature scaling:
# https://en.wikipedia.org/wiki/Feature_scaling
# https://scikit-learn.org/stable/auto_examples/preprocessing/plot_scaling_importance.html#sphx-glr-auto-examples-preprocessing-plot-scaling-importance-py


features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

# Si queremos seleccionar menos features solo tenemos que hacer esto.
#features = ['sepal_length', 'sepal_width', 'petal_length']


# CON CUAL COMBINACIÓN DE 3 FEATURES LA SUMA DE LA PRIMERA Y LA SEGUNDA COMPONENTES PRINCIPALES es MÁXIMA ?
# es decir, con que elección de 3 features la primera y segunda componentes principales explican mayor variabilidad.


x = df.loc[:, features].values
print(x)
y = df.loc[:,'species']
print(y)

x = StandardScaler().fit_transform(x)

# Aqui estan los features escalados
print("-----------------------------------")
print(" Features escalados ")
print(x)


# Como podemos ver el dataset tiene 4 columnas
# Aqui PROJECTAMOS las 4 columnas en 2
# esta reducción de dimensiones,
# crea dos dimensiones que representan la variación de los datos
# pero no tienen un significado particular.


from sklearn.decomposition import PCA

# elegimos el numero de componentes para la reducción de dimensiones
pca = PCA(n_components=2)

# Aplicamos la transformación
principalComponents = pca.fit_transform(x)


principalDf = pd.DataFrame(data = principalComponents, 
        columns = ['principal component 1', 'principal component 2'])
print(principalDf)

finalDf = pd.concat([principalDf, df[['species']]], axis = 1)
print(finalDf)

print("pca explained ratio: ")
pca_explained = pca.explained_variance_ratio_
print(pca_explained)
componente1 = str( pca_explained[0] )
componente2 = str( pca_explained[1] )
print(componente1)


# Visualizamos las dos componentes principales
#  
import matplotlib.pyplot as plt

fig = plt.figure(figsize = (9,9))
ax = fig.add_subplot(1,1,1)
ax.set_xlabel('Principal Component 1 : ' + componente1, fontsize = 11)


ax.set_ylabel('Principal Component 2 : ' + componente2, fontsize = 11)
ax.set_title('PCA 2 principal components', fontsize = 17)
targets = ['setosa', 'versicolor', 'virginica']
colors = ['r', 'g', 'b']

for target, color in zip(targets,colors):
    indicesToKeep = finalDf['species'] == target
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
               , finalDf.loc[indicesToKeep, 'principal component 2']
               , c = color
               , s = 50)
ax.legend(targets)
ax.grid()
plt.show()












