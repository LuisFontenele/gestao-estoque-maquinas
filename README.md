# 💻 Sistema de Gestão de Estoque de Notebooks

Uma aplicação web completa desenvolvida para automatizar e centralizar o controle de ativos de TI (notebooks), realizando a migração de dados legados em planilhas Excel para um banco de dados relacional.

---

## 🚀 Tecnologias Utilizadas

- **Backend:** Python, FastAPI, Uvicorn
- **Banco de Dados & ORM:** PostgreSQL, SQLAlchemy
- **Manipulação de Dados:** Pandas, OpenPyXL
- **Frontend:** Jinja2 (Templates), Bootstrap 5 (CSS/JS)

---

## 📌 Funcionalidades

- **Importação de Dados Legados:** Script em Python/Pandas para leitura, tratamento de dados nulos/vazios e ingestão automática do arquivo Excel para o PostgreSQL.
- **Dashboard Interativo:** Visualização de indicadores em tempo real (Total de máquinas, Disponíveis, Em uso e Em manutenção).
- **Busca e Filtros Dinâmicos:** Pesquisa por código da máquina, modelo ou localidade, além de filtragem avançada por status.
- **Cadastro via Modal:** Interface intuitiva com janela modal para inclusão de novos equipamentos diretamente pela web sem necessidade de recarregar a página.

---

## 📂 Estrutura do Projeto

```text
project-estoque-de-maquinas/
│
├── app/
│   ├── templates/
│   │   ├── base.html          # Layout base com dependências do Bootstrap
│   │   └── dashboard.html     # Painel principal com tabela, cards e modal
│   ├── database.py            # Configuração do SQLAlchemy e sessão do banco
│   ├── main.py                # Rotas da API FastAPI e regras de negócio
│   └── models.py              # Modelo/Tabela SQLAlchemy (Machine)
│
├── .env.example               # Exemplo de configuração de variáveis de ambiente
├── .gitignore                 # Arquivos ignorados pelo Git
├── Estoque do notebook.xlsx   # Planilha legada para importação inicial
├── importar.py                # Script de ingestão de dados com Pandas
└── requirements.txt           # Dependências do projeto
```
