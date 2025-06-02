import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

input_file = 'data/clustered_data.xlsx'

def generate_dashboard():
    df = pd.read_excel(input_file)

    plt.figure(figsize=(8,6))
    sns.countplot(x='cluster', data=df, palette='viridis')
    plt.title('Distribuição de Operadoras por Cluster')
    plt.xlabel('Cluster')
    plt.ylabel('Número de Operadoras')
    plt.savefig('output/operadoras_por_cluster.png')
    plt.close()

    plt.figure(figsize=(8,6))
    sns.histplot(df['beneficiaries_qty'], bins=20, kde=True, color='skyblue')
    plt.title('Distribuição de Quantidade de Beneficiários')
    plt.xlabel('Quantidade de Beneficiários')
    plt.ylabel('Frequência')
    plt.savefig('output/distribuicao_beneficiarios.png')
    plt.close()

    plt.figure(figsize=(8,6))
    scatter = sns.scatterplot(
        x='pct_unique',
        y='pct_ambulatory',
        hue='cluster',
        data=df,
        palette='viridis'
    )
    plt.title('Dispersão: pct_unique vs pct_ambulatory (Cluster)')
    plt.xlabel('Percentual Único')
    plt.ylabel('Percentual Ambulatorial')
    plt.savefig('output/scatter_pct_unique_pct_ambulatory.png')
    plt.close()

    print("Dashboard gerado e imagens salvas em 'output/'")

if __name__ == '__main__':
    generate_dashboard()
