## 🧾 Projeto: Análise Orçamentária e Forecast — FP&A

Este repositório tem como objetivo apresentar de forma prática e aplicada as principais atividades de um analista de FP&A (Financial Planning & Analysis), por meio de um projeto fictício com dados simulados e técnicas reais de análise orçamentária, previsão e controle de desempenho.

A estrutura modular do repositório inclui códigos em Python, dashboards em Excel e Power BI, além de consultas em SQL, permitindo uma demonstração completa e integrada de habilidades técnicas e analíticas voltadas à área de finanças corporativas.

### 🐍 Módulo Python — Análise FP&A com Dados Fictícios

A parte em Python contém:

📁 scripts/: geração automatizada de dados orçamentários com orçado, realizado e forecast por mês e departamento.

📁 dados/: arquivos .csv gerados, representando a base da análise (Comum para outras partes do repositório).

📁 notebooks/: notebook interativo com a análise orçamentária.

Principais análises realizadas:

- Comparação Orçado vs Realizado vs Forecast ao longo dos meses;

- Cálculo de desvios absolutos e percentuais;

- Identificação de áreas com maior variação orçamentária;

- Visualização com gráficos e heatmap.

Os notebooks utilizam pandas, matplotlib, seaborn e seguem boas práticas de estrutura, formatação e reprodutibilidade com ambiente virtual Python (venv).

### 📊 Módulo Excel — Análise Orçamentária com Recursos Nativos

Este módulo reproduz a análise orçamentária utilizando recursos nativos do Microsoft Excel, simulando o trabalho cotidiano de um analista de FP&A com ferramentas amplamente adotadas no ambiente corporativo.

📁 excel/: contém a analise_orcamentaria.xlsx, estruturada com as seguintes funcionalidades:

- Importação automatizada via Power Query dos dados simulados (CSV);

- Criação de colunas auxiliares com fórmulas financeiras (Desvios, Execução %, Gap Forecast);

- Uso de Tabelas Dinâmicas (Pivot Tables) para consolidação e análise dos dados por mês e por departamento;

- Visualizações com gráficos nativos do Excel:

    - Barras agrupadas: Orçado vs Realizado por Departamento;

    - Linhas: Evolução mensal das métricas;

    - Destaque de desvios através do heatmap.

A planilha simula o ambiente real de análise orçamentária, com foco em clareza visual, interatividade e aplicação de boas práticas de estruturação e visualização em Excel.