# 📊 Projeto de Data Mining
# Aluno: Athos Azevedo

Este projeto realiza o pipeline completo de limpeza, análise, modelagem e visualização de dados, com scripts organizados em Python.

---

## 🚀 Como rodar o projeto

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
(Substitua seu-usuario e seu-repositorio pelo caminho correto do seu repositório.)

2️⃣ Instale as dependências
Certifique-se de ter o Python 3.11 ou superior instalado.
Para instalar as dependências, rode:

pip install -r requirements.txt
Se quiser, ative um ambiente virtual antes:

3️⃣ Execute o pipeline principal
O script main.py executa automaticamente todos os scripts do projeto, na ordem correta:

python main.py
✅ Após rodar, os arquivos de saída (gráficos, modelos, etc.) serão gerados na pasta output/.

📂 Estrutura do projeto
├── data/
│   ├── raw_data.csv            # Dados originais
│   ├── cleaned_data.xlsx       # Dados limpos
│
├── output/
│   ├── heatmap_corr.png        # Mapa de calor
│   ├── histogramas.png         # Histogramas
│   └── scatter_pct_unique_beneficiarios.png
├── report/
│   └── colocar o relatorio

├── scripts/
│   ├── data_cleaning.py        # Limpeza dos dados
│   ├── analysis_cluster.py     # Análise de cluster
│   ├── regression_model.py     # Modelo de regressão
│   ├── eda_analysis.py         # Análise exploratória
│   ├── validate_models.py      # Validação de modelos (se aplicável)
│   └── visualize_dashboard.py  # Visualizações finais (se aplicável)
│
├── requirements.txt
└── main.py                     # Script principal (pipeline)