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

### 📈 Módulo Power BI — Dashboard Orçamentário Interativo
O arquivo dashboard_orcamentario.pbix apresenta um painel dinâmico e executivo para análise orçamentária anual, com base em dados estruturados no banco de dados SQL Server.

As visualizações são alimentadas diretamente da tabela Orcamento, populada via script Python a partir do arquivo CSV fonte utilizado em outras etapas. O código python utilizado não será disponibilizado.

🔍 O dashboard inclui:

- Comparação entre Orçado, Realizado e Forecast por departamento;
- Evolução mensal das métricas por área (gráficos de linha);
- Indicadores consolidados por categoria;
- Segmentações por departamento e mês para análise interativa.

Essa estrutura demonstra a integração entre SQL Server e Power BI para análise de dados financeiros no contexto de FP&A.

Este projeto foi desenvolvido com o objetivo de integrar e aplicar, de forma prática, os principais conhecimentos exigidos na área de FP&A — combinando ferramentas técnicas como Python, Excel, SQL Server e Power BI em um fluxo de trabalho completo de análise orçamentária.

Ao utilizar dados simulados e focar em clareza visual, automação e análise crítica, o repositório serve como uma vitrine das competências essenciais para a função de analista financeiro com perfil técnico.

### 👤 Autor

- Victor Monteiro
- Estudante de Controladoria e Finanças na UFMG.
- 💼 LinkedIn: linkedin.com/in/victormontr
- 📂 Projeto pessoal para fins de aprendizado e portfólio.