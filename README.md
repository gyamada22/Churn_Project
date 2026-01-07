# ☁️ Cloud Data Engineering — End-to-End ETL Pipeline
**Python • Apache Airflow • dbt • Snowflake • PostgreSQL • Docker • Power BI**

Este repositório apresenta a construção de um **pipeline de dados end-to-end em ambiente cloud**, cobrindo **ingestão, orquestração, transformação, modelagem analítica e qualidade de dados**, seguindo boas práticas modernas de **Data Engineering e Analytics Engineering**.

O projeto foi desenhado para simular um **cenário real de produção**, indo além de soluções totalmente gerenciadas, com foco em **infraestrutura, automação, versionamento e observabilidade**.

---

## 🎯 Objetivos do Projeto

- Construir um pipeline **completo**, desde dados brutos até camadas analíticas.
- Trabalhar com **dados externos** (API pública e dataset real).
- Implementar **orquestração automatizada** com dependências, retries e logs.
- Aplicar **Medallion Architecture (Bronze, Silver, Gold)** usando dbt.
- Garantir **qualidade de dados** via testes automatizados.
- Simular um ambiente próximo ao **dia a dia de um Data Engineer em cloud**.

---

## 🧱 Stack Tecnológica

### ☁️ Infraestrutura & DevOps
- **Cloud Provider:** DigitalOcean
- **Ambiente:** Linux VM (Droplet)
- **Containerização:** Docker & Docker Compose
- **CI:** GitHub Actions

> Escolha proposital para aprender conceitos reais de infraestrutura, deploy e isolamento de ambientes.

---

### 🗄️ Camada de Dados
- **PostgreSQL**
- **Snowflake** (Data Warehouse Analítico)

Utilização:
- **Bronze:** dados brutos ingeridos
- **Silver:** dados tratados e padronizados
- **Gold:** dados modelados para analytics e BI

---

### 🔌 Ingestão de Dados
- **Python**
  - `requests`
  - `pandas`
  - `SQLAlchemy`

**Responsabilidades:**
- Extração de dados (API pública / CSV real)
- Padronização técnica mínima de schema
- Persistência **sem regras de negócio** na camada Bronze

---

### 🔄 Orquestração
- **Apache Airflow**

**Funcionalidades implementadas:**
- DAGs end-to-end
- Controle de dependências
- Retries automáticos
- Scheduling e backfill
- Logs, Grid View e Gantt View para observabilidade

---

### 🧪 Transformação & Modelagem
- **dbt Core**

**Boas práticas aplicadas:**
- SQL versionado
- Modelagem incremental
- Medallion Architecture
- Separação entre lógica técnica e de negócio

**Camadas:**
- **Bronze:** espelhamento do raw
- **Silver:** limpeza, tipagem, deduplicação
- **Gold:** métricas e tabelas analíticas

**Qualidade de Dados:**
- `not_null`
- `unique`
- testes customizados via dbt

---

### 📊 Consumo Analítico
- **Power BI**

**KPIs e Análises:**
- Taxa de Churn (%)
- Segmentação geográfica
- Comportamento do cliente
- Uso de produtos e impacto na retenção

---

## 📅 Linha do Tempo do Projeto

### 🏗️ Fase 1 — Fundação e Infraestrutura
- Configuração do `docker-compose.yaml`
- Deploy do Apache Airflow
- Criação dos schemas `BRONZE`, `SILVER`, `GOLD`

---

### 📥 Fase 2 — Ingestão & Orquestração
- Desenvolvimento do script Python de ingestão
- Padronização técnica de colunas
- Carga automática na camada Bronze
- Criação da primeira DAG no Airflow

---

### 🧠 Fase 3 — Analytics Engineering
- Modelos dbt para Silver e Gold
- Implementação de regras de negócio
- Testes automatizados de qualidade
- Orquestração do `dbt run` via Airflow

---

### 📈 Fase 4 — Entrega de Valor
- Conexão do Power BI à camada Gold
- Construção de dashboards estratégicos
- Geração de insights para retenção de clientes

---

## 🏦 Caso de Uso: Churn Bancário

Pipeline focado em **retenção de clientes bancários**, transformando dados operacionais em inteligência estratégica.

**Principais análises:**
- Taxa geral de churn
- Churn por país (França, Alemanha, Espanha)
- Relação entre produtos, atividade do cliente e churn

---

## 🛠️ Skills Aplicadas

| Skill | Categoria |
|-----|---------|
| Apache Airflow | Orquestração |
| dbt (data build tool) | Transformação |
| SQL (PostgreSQL / Snowflake) | Data Warehouse |
| Python (ETL) | Engenharia de Dados |
| Docker & Docker Compose | Infraestrutura |
| Power BI | Visualização |
| Git & GitHub Actions | Versionamento & CI |

---

## 🚀 Como Executar o Projeto

```bash
# Subir o ambiente
docker-compose up -d
Acessar o Airflow em http://localhost:8080

Ativar a DAG pipeline_churn_bancario_end_to_end

Aguardar a execução completa

Consultar os dados nas camadas Silver e Gold

Abrir o arquivo .pbix no Power BI para visualizar os dashboards
```
