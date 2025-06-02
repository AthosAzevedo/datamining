import pandas as pd
import os
import sys

input_file = 'data/raw_data.csv'
output_file = 'data/cleaned_data.xlsx'

def clean_data():
    df = pd.read_csv(input_file, sep=';')


    df.rename(columns={
        'REGISTRO_OPERADORA': 'operator_registration',
        'CICLO': 'cycle',
        'TP_AGRUPAMENTO': 'group_type',
        'PCT_UNICO': 'pct_unique',
        'PCT_AMBULATORIAL': 'pct_ambulatory',
        'PCT_INT_SEM_OBSTET': 'pct_inpatient_without_obstetric',
        'PCT_INT_COM_OBSTET': 'pct_inpatient_with_obstetric',
        'QT_CONTRATOS': 'contracts_qty',
        'QT_BENEF': 'beneficiaries_qty',
        'RAZAO_SOCIAL': 'company_name'
    }, inplace=True)

    df.fillna(0, inplace=True)

    numeric_cols = ['pct_unique', 'pct_ambulatory', 'pct_inpatient_without_obstetric',
                    'pct_inpatient_with_obstetric', 'contracts_qty', 'beneficiaries_qty']

    for col in numeric_cols:
        if df[col].dtype == 'object':
            df[col] = df[col].str.replace(',', '.')
        if col.startswith('pct_'):
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
        else:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)

    df.to_excel(output_file, index=False)

    print(f'Data cleaned and saved to {output_file}')

if __name__ == '__main__':
    clean_data()
