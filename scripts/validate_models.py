import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

df = pd.read_excel('data/cleaned_data.xlsx')

X = df[['pct_unique', 'pct_ambulatory', 'pct_inpatient_without_obstetric',
        'pct_inpatient_with_obstetric', 'contracts_qty', 'beneficiaries_qty']]

distortions = []
K = range(1, 10)
for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    distortions.append(kmeans.inertia_)

plt.figure(figsize=(8,5))
plt.plot(K, distortions, 'bx-')
plt.xlabel('Número de Clusters')
plt.ylabel('Inércia (Distância Média)')
plt.title('Método do Cotovelo')
plt.savefig('output/elbow_method.png')
plt.show()

k = 3
kmeans = KMeans(n_clusters=k, random_state=42)
labels = kmeans.fit_predict(X)
score = silhouette_score(X, labels)
print(f'Silhouette Score para k={k}: {score:.3f}')

X_reg = df[['pct_unique', 'pct_ambulatory', 'pct_inpatient_without_obstetric',
            'pct_inpatient_with_obstetric', 'contracts_qty']]
y_reg = df['beneficiaries_qty']

X_train, X_test, y_train, y_test = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

plt.figure(figsize=(7,6))
plt.scatter(y_test, y_pred, alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.xlabel('Valores Reais')
plt.ylabel('Valores Preditos')
plt.title('Regressão Linear: Real vs. Predito')
plt.savefig('output/regressao_real_vs_predito.png')
plt.show()
