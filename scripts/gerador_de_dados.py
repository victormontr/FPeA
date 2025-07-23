import pandas as pd
import numpy as np
import os
from datetime import datetime

def gerar_dados_orcamento() -> str:
    """
    Gera dados simulados de orçamento (Orçado, Realizado, Forecast) por departamento e mês,
    salvando-os em um arquivo CSV com configurações internas e datas genéricas (Dia-Mês).
    Ideal para projetos estáticos onde os parâmetros são fixos no código.

    Returns:
        str: Uma mensagem confirmando o salvamento e o caminho do arquivo.
    """
    # --- Parâmetros de Configuração Interna ---
    # Estes parâmetros são fixos para este projeto estático.
    departamentos = ['Financeiro', 'Marketing', 'RH', 'Operações', 'TI']
    meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
    
    # Faixa de valores para a base orçamentária inicial de cada departamento
    min_base_orcamento = 15000
    max_base_orcamento = 25000
    
    # Faixa de crescimento mensal para o orçamento
    min_crescimento_mensal = 0.01
    max_crescimento_mensal = 0.03
    
    # Desvio padrão para a variação de Realizado e Forecast
    desvio_padrao_realizado = 3000
    desvio_padrao_forecast = 2000
    
    # Caminho onde o arquivo CSV será salvo
    caminho_saida = "dados/orcamento_empresa.csv"
    
    # Semente para reprodutibilidade dos dados
    seed = 2002
    # --- Fim dos Parâmetros ---

    # Configurar a semente para reprodutibilidade
    np.random.seed(seed)

    dados = []
    for dept in departamentos:
        # Gerar valores base e de crescimento para cada departamento
        # O +1 em max_base_orcamento garante que o valor máximo seja inclusivo
        base_orcamento_inicial = np.random.randint(min_base_orcamento, max_base_orcamento + 1)
        crescimento_mensal_dept = np.random.uniform(min_crescimento_mensal, max_crescimento_mensal)

        for i, mes in enumerate(meses):
            # Calcular o valor orçado com base no crescimento mensal (exponencial)
            orcado = base_orcamento_inicial * (1 + crescimento_mensal_dept) ** i

            # Calcular valores realizado e forecast com base no orçado e desvios aleatórios
            # np.random.normal(média, desvio_padrão) gera um número aleatório seguindo uma distribuição normal
            realizado = orcado + np.random.normal(0, desvio_padrao_realizado)
            forecast = orcado + np.random.normal(0, desvio_padrao_forecast)

            # Criar a data no formato "DD-Mon", ignorando o ano.
            # Foi usado um ano fictício (ex: 2024) apenas para criar o objeto datetime.
            data_str = datetime(2024, i + 1, 1).strftime("%d-%b") # Ex: 01-Jan

            dados.append([
                data_str,
                dept,
                round(orcado, 2),    # Arredonda para 2 casas decimais
                round(realizado, 2), 
                round(forecast, 2)   
            ])

    # Criar DataFrame com as colunas especificadas
    colunas = ["Data", "Departamento", "Orcado", "Realizado", "Forecast"]
    df = pd.DataFrame(dados, columns=colunas)

    # Criar o diretório de saída se ele não existir
    diretorio_saida = os.path.dirname(caminho_saida)
    if diretorio_saida and not os.path.exists(diretorio_saida):
        os.makedirs(diretorio_saida, exist_ok=True)

    # Salvar o DataFrame em um arquivo CSV
    df.to_csv(caminho_saida, index=False, encoding="utf-8-sig")

    return f"✅ Base orçamentária genérica e estática salva em: {caminho_saida}"

print("Gerando dados de orçamento para o projeto estático...")
mensagem = gerar_dados_orcamento()
print(mensagem)