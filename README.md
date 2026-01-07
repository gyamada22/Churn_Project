# 🏦 Churn Bancário — Pipeline de Dados & Insights Estratégicos

## 🎯 Contexto do Problema
Este projeto analisa dados de clientes bancários com o objetivo de identificar
os principais fatores que influenciam o **churn** e apoiar **decisões estratégicas
de retenção**, utilizando um pipeline de dados completo e automatizado.

O foco não é apenas o dashboard final, mas todo o processo de **engenharia,
transformação e análise de dados**, simulando um cenário real de Data Engineering
e Analytics.

---

## ⚙️ Stack & Fluxo de Dados

**Stack:** Python • SQL • dbt • Apache Airflow • PostgreSQL / Snowflake • Power BI • Docker

- **Fonte de Dados:**  
  Dataset público de Churn Bancário (Kaggle), representando dados operacionais de clientes financeiros.

- **Ingestão de Dados:**  
  - **Python** para extração, padronização técnica e carga dos dados brutos  
  - Uso de **Pandas** e **SQLAlchemy** para persistência eficiente  

- **Armazenamento & Camadas de Dados:**  
  - **PostgreSQL / Snowflake** como base central  
  - Arquitetura em camadas (**Bronze, Silver e Gold**)  

- **Transformação & Modelagem:**  
  - **dbt** para transformações SQL versionadas  
  - Regras de negócio, tipagem, deduplicação e métricas analíticas  
  - Testes automatizados de qualidade de dados  

- **Orquestração:**  
  - **Apache Airflow** para execução end-to-end do pipeline  
  - Controle de dependências, retries, logs e agendamento  

- **Visualização & Analytics:**  
  - **Power BI** conectado à camada **Gold**  
  - Dashboards focados em churn, retenção e comportamento do cliente  

- **Infraestrutura & DataOps:**  
  - **Docker & Docker Compose** para padronização do ambiente  
  - **Git & GitHub** para versionamento do código e do pipeline  

---

## ❓ Perguntas de Negócio Respondidas
- Quais perfis de clientes apresentam maior risco de churn?
- O uso de múltiplos produtos reduz a evasão?
- Qual é o impacto financeiro do churn?
- Em que momento do relacionamento o cliente tende a sair?

---

## 📌 KPIs-Chave
- **Taxa de Churn (%)**
- **Saldo Perdido (€)**
- **Clientes Ativos vs Inativos**
- **Churn por Quantidade de Produtos**
- **Churn por Tempo de Relacionamento (Tenure)**

---

## 📊 Insights Estratégicos

- **Alta Renda em Risco**  
  **Insight:** Clientes com saldo entre **100k–150k** concentram a maior parte do **saldo perdido (€185,6 Mi)**.  
  **Ação:** Criar programas de retenção dedicados para clientes de alto valor.

- **Segundo Produto = Fidelização**  
  **Insight:** Clientes com **2 produtos** apresentam a **menor taxa de churn (7,58%)**.  
  **Ação:** Estratégia de cross-sell para levar rapidamente o cliente do 1º para o 2º produto.

- **Churn Concentrado em 1 Produto**  
  **Insight:** Clientes com apenas **1 produto** geram o maior volume absoluto de churn (**1.409 cancelamentos**).  
  **Ação:** Incentivos e ofertas nos primeiros meses de relacionamento.

- **Falha no Onboarding**  
  **Insight:** O churn atinge cerca de **23% no primeiro ano** de relacionamento.  
  **Ação:** Melhorar o onboarding e a entrega de valor nos primeiros 90 dias.

- **Público Maduro em Risco**  
  **Insight:** Clientes entre **50–59 anos** apresentam churn de **56,04%**.  
  **Ação:** Desenvolver produtos de investimento, previdência e atendimento premium.

---

## 💼 Impacto para o Negócio
Os resultados permitem:
- Priorizar a retenção de clientes de **alta renda**
- Reduzir churn nos **primeiros meses de relacionamento**
- Aumentar a fidelização por meio de **cross-sell**
- Apoiar decisões estratégicas com base em dados confiáveis e automatizados
