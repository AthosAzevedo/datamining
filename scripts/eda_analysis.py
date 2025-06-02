import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('data/cleaned_data.xlsx')

print(df.head())

print(df.describe())

num_cols = df.select_dtypes(include=['number']).columns
corr = df[num_cols].corr()
print(corr)

plt.figure(figsize=(10,8))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Matriz de Correlação')
plt.savefig('output/heatmap_corr.png')
plt.show()

df[num_cols].hist(bins=20, figsize=(12,10))
plt.tight_layout()
plt.savefig('output/histogramas.png')
plt.show()

if 'pct_unique' in df.columns and 'beneficiaries_qty' in df.columns:
    sns.scatterplot(x='pct_unique', y='beneficiaries_qty', data=df)
    plt.title('Pct Unique vs. Beneficiários')
    plt.savefig('output/scatter_pct_unique_beneficiarios.png')
    plt.show()
else:
    print("🚫 As colunas 'pct_unique' ou 'beneficiaries_qty' não existem no DataFrame.")
