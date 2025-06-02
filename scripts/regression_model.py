import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df = pd.read_excel('data/cleaned_data.xlsx')

X = df[['pct_unique']]
y = df['beneficiaries_qty']

model = LinearRegression()

model.fit(X, y)

df['predicted_beneficiaries'] = model.predict(X)

plt.scatter(X, y, color='blue', label='Dados reais')
plt.plot(X, df['predicted_beneficiaries'], color='red', label='Regressão Linear')
plt.xlabel('Percentual Único')
plt.ylabel('Beneficiários')
plt.legend()
plt.title('Regressão Linear: Beneficiários vs. Percentual Único')
plt.savefig('output/regression_plot.png')
plt.show()

print(f'Coeficiente (inclinação): {model.coef_[0]}')
print(f'Intercepto: {model.intercept_}')
