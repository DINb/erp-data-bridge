# 🚀 ERP Data Bridge - Invoice Validator (AP Module)

[PT-BR] Este projeto demonstra a união entre conhecimento Funcional e Tecnologia para garantir a integridade de dados em integrações ERP.

## 🇺🇸 English Version

### 💡 Business Context
In Oracle Cloud ERP projects, Data migration or integration often fails due to inconsistent records. This project acts as a **Middleware**, validating business rules before data reaches the **Oracle Integration Cloud (OIC)**.

### 🛠️ Key Features
- **Amount Validation:** Blocks negative or zero values for Invoices.
- **Date Formatting:** Ensures the ISO (YYYY-MM-DD) standard required by Oracle Cloud.
- **Vendor Integrity:** Simulates a master data check for valid Vendor IDs.

### ⚙️ Tech Stack
- **Python / FastAPI**
- **Pydantic** (Data Validation)
- **Thunder Client** (API Testing)

---

## 🇧🇷 Versão em Português

### 💡 Contexto de Negócio
Em projetos de Oracle Cloud ERP, integrações costumam falhar por dados inconsistentes. Este projeto atua como um **Middleware**, validando regras de negócio antes que o dado chegue ao **OIC**.

### 🛠️ Funcionalidades
- **Validação de Valor:** Bloqueia valores negativos ou zerados em Notas Fiscais.
- **Formatação de Data:** Garante o padrão ISO (AAAA-MM-DD) exigido pelo Oracle Cloud.
- **Integridade de Fornecedor:** Simula uma checagem no mestre de fornecedores para IDs válidos.

---

## 📸 Proof of Concept(Evidence)
![Sucesso na Integração](./assets/sucesso.jpg)
![Erro de Validação](./assets/erro.jpg)