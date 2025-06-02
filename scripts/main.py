import subprocess

scripts = [
    'scripts/data_cleaning.py',
    'scripts/analysis_cluster.py',
    'scripts/regression_model.py',
    'scripts/eda_analysis.py',
    'scripts/validate_models.py',
    'scripts/visualize_dashboard.py',
]

for script in scripts:
    print(f"Executando {script}...")
    result = subprocess.run(['python', script], capture_output=True, text=True)

    print(result.stdout)

    if result.returncode != 0:
        print(f"Erro ao executar {script}:")
        print(result.stderr)
        break

print("\n✅ Todos os scripts executados com sucesso!")
