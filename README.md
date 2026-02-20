# 📄 Gerador Automático de Currículos - CV ATS Otimizado

Um projeto Python que gera automaticamente currículos personalizados em PDF e Word, otimizados para sistemas ATS (Applicant Tracking System) como Greenhouse, Lever e Workday.

## 🎯 Sobre o Projeto

Este projeto foi desenvolvido para automatizar a criação de currículos personalizados para diferentes stacks tecnológicos e idiomas. Ele gera múltiplas versões otimizadas para vagas específicas, aumentando as chances de aprovação em sistemas de triagem automática.

## ✨ Funcionalidades

### 📊 Geração de PDFs (index.py)
  - **4 especializações técnicas:**
    - Full Stack MERN (MongoDB, Express, React, Node.js)
    - Back-End Node.js & TypeScript
    - Back-End Java & Spring Boot
    - Integrações MuleSoft & API-Led Connectivity
  - **2 idiomas:** Português (PT-BR) e Inglês (EN-US)

### 📝 Geração de Word (doc.py)
- Currículo específico para vagas **Java Pleno**
- Formato idêntico ao PDF, adaptado para Word
- Inclui informações específicas para RH

### 🔧 Otimizações ATS
- Formatação compatível com leitores automáticos
- Palavras-chave estratégicas por stack
- Métricas quantificáveis de performance
- Estrutura padronizada e limpa

## 🚀 Como Usar

### Pré-requisitos

```bash
# Instalar dependências Python
pip install reportlab python-docx
```

### Executando o Gerador

#### 1. Gerar todos os CVs em PDF:
```bash
python index.py
```

**Saída esperada:**
```
Gerado: Benevanio_CV_MERN_FullStack_PT.pdf
Gerado: Benevanio_CV_MERN_FullStack_EN.pdf
Gerado: Benevanio_CV_Node_Backend_PT.pdf
Gerado: Benevanio_CV_Node_Backend_EN.pdf
Gerado: Benevanio_CV_Java_Backend_PT.pdf
Gerado: Benevanio_CV_Java_Backend_EN.pdf
Gerado: Benevanio_CV_MuleSoft_Integrations_PT.pdf
Gerado: Benevanio_CV_MuleSoft_Integrations_EN.pdf
Gerado: Benevanio_CV_Hybrid_Systems_PT.pdf

✅ Todos os currículos foram gerados com sucesso!
```

#### 2. Gerar CV Java em Word:
```bash
python doc.py
```

### 📁 Estrutura de Arquivos Gerados

```
/projeto
├── index.py                                    # Gerador de PDFs
├── doc.py                                     # Gerador de Word
├── README.md                                  # Este arquivo
└── [CVs Gerados]
    ├── Benevanio_CV_MERN_FullStack_PT.pdf
    ├── Benevanio_CV_MERN_FullStack_EN.pdf
    ├── Benevanio_CV_Node_Backend_PT.pdf
    ├── Benevanio_CV_Node_Backend_EN.pdf
    ├── Benevanio_CV_Java_Backend_PT.pdf
    ├── Benevanio_CV_Java_Backend_EN.pdf
    ├── Benevanio_CV_MuleSoft_Integrations_PT.pdf
    ├── Benevanio_CV_MuleSoft_Integrations_EN.pdf
    ├── Benevanio_CV_Hybrid_Systems_PT.pdf
    └── Curriculo_Java_Pleno_Identico_PDF.docx
```

## 🛠️ Personalização

### Modificar Dados Pessoais

Para personalizar o currículo com seus dados, edite as seguintes seções no [index.py](index.py):

```python
# Cabeçalho - Linha ~17
story.append(Paragraph("<font size=14><b>SEU NOME</b></font>", styles["Normal"]))

# Contatos - Linha ~20-24  
story.append(Paragraph(
    "Sua Cidade, Estado | seuemail@gmail.com | Telefone: +55 XX XXXXX-XXXX<br/>"
    "LinkedIn: linkedin.com/in/seulinkedin | GitHub: github.com/seugithub<br/>"
    f"Portfólio: seuportfolio.com | {language_note}",
    styles["Normal"]
))
```

### Adicionar Nova Especialização

1. **Criar novo dicionário de dados:**

```python
cv_nova_stack_pt = {
    "title": "Seu Título Profissional | Tecnologias Principais",
    "summary": "Seu resumo profissional personalizado...",
    "experience_items": [
        "Sua experiência 1 com métricas quantificáveis...",
        "Sua experiência 2 com resultados mensuráveis...",
        # ... mais experiências
    ],
    "skills": "Suas habilidades organizadas por categorias...",
    "projects": [
        "Projeto 1 com descrição técnica...",
        "Projeto 2 com tecnologias utilizadas..."
    ],
    "education": "Sua formação acadêmica...",
    "language_note": language_note_pt
}
```

2. **Adicionar à lista de geração:**

```python
all_cvs = [
    # ... CVs existentes
    (cv_nova_stack_pt, "Seu_CV_NovaStack_PT.pdf"),
    (cv_nova_stack_en, "Seu_CV_NovaStack_EN.pdf")
]
```

### Modificar Experiências e Projetos

Todas as experiências incluem **métricas quantificáveis** para maior impacto:

```python
"experience_items": [
    "Desenvolvi X funcionalidade resultando em Y% de melhoria em Z métrica",
    "Otimizei processo ABC reduzindo tempo de resposta em X% e aumentando throughput em Y%",
    "Implementei sistema XYZ que aumentou eficiência em Z% e reduziu custos em $X"
]
```

## 🎯 Estratégia ATS

### Palavras-chave por Stack:

- **MERN:** React.js, Node.js, MongoDB, Express.js, JavaScript, TypeScript
- **Node.js:** Node.js, TypeScript, Express, NestJS, RESTful APIs, Microservices  
- **Java:** Spring Boot, Hibernate, JPA, Maven, JUnit, Microservices
- **MuleSoft:** API-Led Connectivity, DataWeave, Anypoint Platform, Integration

### Métricas Incluídas:
- ✅ Percentuais de melhoria de performance
- ✅ Redução de tempo de resposta/deploy
- ✅ Aumento de disponibilidade/throughput
- ✅ Cobertura de testes e qualidade
- ✅ Economia de custos operacionais

## 🔄 Versionamento de CVs

Recomenda-se versionar os CVs gerados por data:

```bash
# Criar pasta com data atual
mkdir cvs_$(date +%Y%m%d)
python index.py
mv *.pdf cvs_$(date +%Y%m%d)/
```

## 📋 Checklist de Uso

Antes de enviar seus CVs:

- [ ] ✅ Todos os PDFs foram gerados sem erros
- [ ] 📝 Dados pessoais estão atualizados  
- [ ] 🎯 Stack escolhido é compatível com a vaga
- [ ] 🌐 Idioma correto (PT-BR para vagas nacionais, EN-US para internacionais)
- [ ] 📊 Métricas estão atualizadas e realistas
- [ ] 🔍 Palavras-chave da vaga estão presentes no CV

## 💡 Dicas de Uso

1. **Escolha o CV certo:** Use o CV específico para a stack da vaga
2. **Versão em inglês:** Para vagas internacionais ou empresas multinacionais
3. **Personalização:** Ajuste palavras-chave específicas da vaga antes de enviar
4. **Métricas:** Mantenha métricas realistas e verificáveis
5. **Atualização:** Regenere os CVs periodicamente com novas experiências

## 📞 Suporte

Para dúvidas ou melhorias neste projeto, abra uma issue ou entre em contato.

---

**Desenvolvido para otimizar o processo de candidatura a vagas tech** 🚀