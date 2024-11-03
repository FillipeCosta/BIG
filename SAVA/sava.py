import pandas as pd

# Carrega o arquivo .xlsx
file_path = 'date.xlsx'  # Substitua pelo caminho do seu arquivo
data = pd.read_excel(file_path)

# Converte o DataFrame para JSON e salva em um arquivo
output_json_path = 'arquivo_convertido.json'  # Nome do arquivo JSON de saída
data.to_json(output_json_path, orient="records", indent=4)

print(f"Arquivo JSON salvo como {output_json_path}")
