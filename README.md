# Sistema de Gestão SST  
**Medicina Ocupacional • PGR • PCMSO • ASO**

Sistema profissional de gestão em Segurança e Saúde do Trabalho, focado em:

- Geração automática de **PGR** (NR-01 + NR-09)
- Geração automática de **PCMSO** (NR-07) a partir dos riscos do PGR
- Cadastro de colaboradores, clínicas e fluxo completo de exames
- Formulário de **ASO** + Checklist de Avaliação Psicossocial
- Upload de ASO pela clínica com acesso da empresa solicitante
- Documentos prontos para **imprimir** ou **enviar**

---

## Estrutura do Projeto

```
Sistema_SST/
├── docs/
│   └── Especificacao_Tecnica_Sistema_SST.docx   # Especificação técnica completa
├── modelos_dados/
│   └── Modelo_Dados_Sistema_SST.xlsx            # Modelo de dados (tabelas e relacionamentos)
├── templates/
│   ├── Template_PGR_NR01_NR09.docx              # Template oficial do PGR
│   └── Template_PCMSO_NR07.docx                 # Template oficial do PCMSO
├── formularios/
│   ├── Formulario_ASO_e_Checklist_Psicossocial.html      # ASO + Checklist (CEP, CNPJ, múltiplos riscos)
│   └── Formulario_Cadastro_Empresa_e_Riscos.html         # Cadastro empresa + inventário de riscos
├── prototipo/
│   └── index.html                               # Dashboard / protótipo responsivo
└── README.md
```

---

## Principais Funcionalidades

### 1. PGR (Programa de Gerenciamento de Riscos)
- Inventário de riscos ocupacionais (físicos, químicos, biológicos, ergonômicos, acidentes e psicossociais)
- Critérios de avaliação (Probabilidade × Severidade)
- Plano de Ação com hierarquia de controles
- Documento completo gerado automaticamente

### 2. PCMSO (Programa de Controle Médico de Saúde Ocupacional)
- Matriz de exames por função / risco (vinculada ao PGR)
- Tipos de exame: Admissional, Periódico, Retorno, Mudança de Riscos e Demissional
- Estrutura de Relatório Analítico Anual
- Documento-base pronto para validação do médico coordenador

### 3. Fluxo Completo de ASO
1. Empresa solicita exame do colaborador  
2. Sistema gera Pedido + Formulário ASO + Checklist Psicossocial  
3. Clínica recebe e agenda  
4. Colaborador preenche o checklist psicossocial  
5. Médico edita o ASO, conclui (Apto/Inapto) e imprime  
6. Clínica faz upload do ASO → empresa tem acesso imediato  

### 4. Características Técnicas
- Interface **responsiva** (celular e desktop)
- Campos obrigatórios conforme NR-07 item 7.5.19.1
- Documentos prontos para impressão e envio
- Modelo de dados estruturado para evolução para sistema completo (web + banco de dados)

---

## Conformidade Legal

| Norma | Aplicação no Sistema |
|-------|----------------------|
| **NR-01** | Gerenciamento de Riscos Ocupacionais (GRO) e estrutura mínima do PGR |
| **NR-07** | PCMSO, ASO e relatório analítico |
| **NR-09** | Avaliação e controle de agentes físicos, químicos e biológicos |

---

## Como usar (versão atual)

1. Abra o **protótipo** (`prototipo/index.html`) no navegador para visualizar o fluxo.
2. Use o **Formulário ASO** (`formularios/Formulario_ASO_e_Checklist_Psicossocial.html`) para preencher, imprimir ou simular o envio.
3. Utilize os **templates** de PGR e PCMSO como base para geração dos documentos oficiais.
4. Consulte a **Especificação Técnica** e o **Modelo de Dados** para desenvolvimento do sistema completo.

---

## Próximos Passos (evolução)

- [ ] Formulário de inventário de riscos (alimentação do PGR)
- [ ] Geração automática de documentos preenchidos (PDF/DOCX)
- [ ] Backend + banco de dados
- [ ] Controle de acesso (empresa / clínica / médico)
- [ ] Dashboard de vencimentos e conformidade
- [ ] Assinatura digital (ICP-Brasil) no ASO

---

## Autor / Responsável

Projeto desenvolvido para gestão profissional de SST, com foco em usabilidade, conformidade normativa e geração automática de documentação.

---

**Versão:** 1.0  
**Data:** Setembro 2026  
**Base normativa:** NR-01, NR-07 e NR-09 – Ministério do Trabalho e Emprego (MTE)
