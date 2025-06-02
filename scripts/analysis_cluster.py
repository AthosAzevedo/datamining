import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

input_file = 'data/cleaned_data.xlsx'

def cluster_analysis():
    df = pd.read_excel(input_file)

    features = ['pct_unique', 'pct_ambulatory', 'pct_inpatient_without_obstetric',
                'pct_inpatient_with_obstetric', 'contracts_qty', 'beneficiaries_qty']

    X = df[features]

    k = 3
    kmeans = KMeans(n_clusters=k, random_state=42)
    df['cluster'] = kmeans.fit_predict(X)

    df.to_excel('data/clustered_data.xlsx', index=False)

    plt.scatter(df['pct_unique'], df['pct_ambulatory'], c=df['cluster'], cmap='viridis')
    plt.xlabel('Percentual Único')
    plt.ylabel('Percentual Ambulatorial')
    plt.title('Clusterização KMeans')
    plt.savefig('output/cluster_plot.png')
    plt.show()

    print('Cluster analysis completed and results saved.')

if __name__ == '__main__':
    cluster_analysis()
