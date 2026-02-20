# ============================================================================
# CV ATS-Otimizado para Benevanio Santos
# Gera 8 PDFs: 4 especializações x 2 idiomas (PT-BR e EN-US)
# Otimizado para ATS (Greenhouse, Lever, Workday), com métricas, palavras-chave
# e formatação compatível com leitores automáticos.
# ============================================================================

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

styles = getSampleStyleSheet()

def build_cv(path, title, summary, experience_items, skills, projects, education, language_note):
    """
    Gera um currículo em PDF com formatação ATS-friendly.
    """
    doc = SimpleDocTemplate(path, pagesize=A4)
    story = []

    # Cabeçalho
    story.append(Paragraph("<font size=14><b>Benevanio Santos</b></font>", styles["Normal"]))
    story.append(Paragraph(f"<font size=12><b>{title}</b></font>", styles["Normal"]))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "Brasil | benevaniosantos930@gmail.com | WhatsApp: +55 19 99828-3835<br/>"
        "LinkedIn: linkedin.com/in/bene-tesla | GitHub: github.com/Benevanio<br/>"
        f"Portfólio: bene-tesla-dev.vercel.app | {language_note}",
        styles["Normal"]
    ))
    story.append(Spacer(1, 20))

    # Resumo Profissional / Professional Summary
    story.append(Paragraph("<b>Resumo Profissional</b>" if "Desenvolvedor" in title else "<b>Professional Summary</b>", styles["Heading3"]))
    story.append(Paragraph(summary, styles["Normal"]))
    story.append(Spacer(1, 12))

    # Experiência Profissional / Professional Experience
    story.append(Paragraph("<b>Experiência Profissional</b>" if "Desenvolvedor" in title else "<b>Professional Experience</b>", styles["Heading3"]))
    story.append(Paragraph("<b>SysMap Solutions – Desenvolvedor Back-End (Terceirizado Natura)</b><br/>Jun 2023 – Atual | Remoto", styles["Normal"]))
    story.append(ListFlowable(
        [ListItem(Paragraph(item, styles["Normal"])) for item in experience_items],
        bulletType='bullet',
        leftIndent=20
    ))
    story.append(Spacer(1, 12))

    # Habilidades Técnicas / Technical Skills
    story.append(Paragraph("<b>Habilidades Técnicas</b>" if "Desenvolvedor" in title else "<b>Technical Skills</b>", styles["Heading3"]))
    story.append(Paragraph(skills, styles["Normal"]))
    story.append(Spacer(1, 12))

    # Projetos Relevantes / Relevant Projects
    story.append(Paragraph("<b>Projetos Relevantes</b>" if "Desenvolvedor" in title else "<b>Relevant Projects</b>", styles["Heading3"]))
    for p in projects:
        story.append(Paragraph(p, styles["Normal"]))
        story.append(Spacer(1, 6))

    story.append(Spacer(1, 12))

    # Formação Acadêmica / Education
    story.append(Paragraph("<b>Formação Acadêmica</b>" if "Desenvolvedor" in title else "<b>Education</b>", styles["Heading3"]))
    story.append(Paragraph(education, styles["Normal"]))

    doc.build(story)

# ============================================================================
# DADOS DOS CURRÍCULOS (PT-BR e EN-US)
# ============================================================================

# Nota sobre idioma para o cabeçalho
language_note_pt = "Inglês: Iniciante (em estudo, leitura técnica)"
language_note_en = "English: Beginner (currently studying, technical reading)"

# ----------------------------------------------------------------------------
# 1. FULL STACK MERN (PT-BR e EN-US)
# ----------------------------------------------------------------------------
cv_mern_pt = {
    "title": "Desenvolvedor Full Stack | Stack MERN & Arquitetura de APIs",
    "summary": "Desenvolvedor Full Stack com experiência sólida no desenvolvimento de aplicações escaláveis utilizando a stack MERN completa (MongoDB, Express.js, React.js, Node.js). Expertise em construir APIs RESTful performáticas e interfaces de usuário modernas com React (Hooks, Context API). Foco em qualidade de código, testes automatizados, boas práticas de arquitetura (Clean Code, SOLID) e observabilidade. Experiência em projetos reais com impacto mensurável em performance e rastreabilidade.",
    "experience_items": [
        "Desenvolvimento end-to-end de uma aplicação web com stack MERN, aumentando a satisfação do usuário em 25% através de melhorias na performance e usabilidade.",
        "Construção de APIs RESTful robustas com Node.js e Express.js, implementando autenticação JWT, validações e tratamento de erros, reduzindo o tempo de resposta médio em 30%.",
        "Desenvolvimento de interfaces responsivas e dinâmicas com React.js, utilizando Hooks, Context API e Styled Components, melhorando o tempo de carregamento em 40% com code splitting e lazy loading.",
        "Modelagem de dados e otimização de desempenho em MongoDB, criando índices estratégicos e schemas eficientes, resultando em uma redução de 35% no tempo de consulta.",
        "Implementação de logging estruturado e dashboards de monitoramento com Kibana, aumentando a rastreabilidade do sistema em 40%.",
        "Containerização de aplicações com Docker e deploy em ambiente AWS (EC2, S3, Lambda), reduzindo o tempo de deploy em 50%.",
        "Participação ativa em ceremonies ágeis (Scrum), code reviews e aplicação de boas práticas (TDD, Clean Architecture), aumentando a cobertura de testes em 50%."
    ],
    "skills": "<b>Front-End:</b> React.js, Next.js, Hooks, Context API, Styled-Components, HTML5, CSS3, Bootstrap<br/>"
              "<b>Back-End & APIs:</b> Node.js, Express.js, RESTful APIs, JWT, Autenticação/OAuth<br/>"
              "<b>Banco de Dados:</b> MongoDB, Mongoose, Design de Schemas, Indexação, Redis (cache)<br/>"
              "<b>Linguagens:</b> JavaScript (ES6+), TypeScript<br/>"
              "<b>Ferramentas & DevOps:</b> Git, Docker, Kubernetes (conceitos), Terraform (conceitos), Jenkins, AWS (EC2, S3, Lambda), Postman, Kibana<br/>"
              "<b>Metodologias & Soft Skills:</b> Scrum, TDD, Clean Code, SOLID, Clean Architecture, Comunicação, Trabalho em Equipe, Resolução de Problemas",
    "projects": [
        "<b>SocialMedia API (Full Stack):</b> Desenvolvi uma API RESTful completa para uma rede social utilizando Node.js, Express e MongoDB. Implementei autenticação JWT, upload de imagens e um front-end responsivo com React.js.",
        "<b>AuthKnex:</b> Sistema de autenticação robusto com Node.js, JWT, PostgreSQL, incluindo roles, refresh token e fluxos de segurança."
    ],
    "education": "<b>PUC Minas</b> – Pós-Graduação em Arquitetura de Software Distribuído (2025 – 2027, em andamento)<br/>"
                 "<b>Anhanguera Educacional</b> – Bacharelado em Engenharia de Software (2021 – 2025)",
    "language_note": language_note_pt
}

cv_mern_en = {
    "title": "Full Stack Developer | MERN Stack & API Architecture",
    "summary": "Full Stack Developer with solid experience in building scalable applications using the full MERN stack (MongoDB, Express.js, React.js, Node.js). Expertise in building high-performance RESTful APIs and modern user interfaces with React (Hooks, Context API). Focus on code quality, automated testing, architecture best practices (Clean Code, SOLID), and observability. Experience in real projects with measurable impact on performance and traceability.",
    "experience_items": [
        "End-to-end development of a web application using the MERN stack, increasing user satisfaction by 25% through performance and usability improvements.",
        "Built robust RESTful APIs with Node.js and Express.js, implementing JWT authentication, validations, and error handling, reducing average response time by 30%.",
        "Developed responsive and dynamic interfaces with React.js, using Hooks, Context API, and Styled Components, improving load time by 40% through code splitting and lazy loading.",
        "Data modeling and performance optimization in MongoDB, creating strategic indexes and efficient schemas, resulting in a 35% reduction in query time.",
        "Implemented structured logging and monitoring dashboards with Kibana, increasing system traceability by 40%.",
        "Containerized applications with Docker and deployed on AWS environment (EC2, S3, Lambda), reducing deployment time by 50%.",
        "Active participation in agile ceremonies (Scrum), code reviews, and application of best practices (TDD, Clean Architecture), increasing test coverage by 50%."
    ],
    "skills": "<b>Front-End:</b> React.js, Next.js, Hooks, Context API, Styled-Components, HTML5, CSS3, Bootstrap<br/>"
              "<b>Back-End & APIs:</b> Node.js, Express.js, RESTful APIs, JWT, Authentication/OAuth<br/>"
              "<b>Databases:</b> MongoDB, Mongoose, Schema Design, Indexing, Redis (caching)<br/>"
              "<b>Languages:</b> JavaScript (ES6+), TypeScript<br/>"
              "<b>Tools & DevOps:</b> Git, Docker, Kubernetes (concepts), Terraform (concepts), Jenkins, AWS (EC2, S3, Lambda), Postman, Kibana<br/>"
              "<b>Methodologies & Soft Skills:</b> Scrum, TDD, Clean Code, SOLID, Clean Architecture, Communication, Teamwork, Problem Solving",
    "projects": [
        "<b>SocialMedia API (Full Stack):</b> Developed a complete RESTful API for a social network using Node.js, Express, and MongoDB. Implemented JWT authentication, image upload, and a responsive front-end with React.js.",
        "<b>AuthKnex:</b> Robust authentication system with Node.js, JWT, PostgreSQL, including roles, refresh token, and security flows."
    ],
    "education": "<b>PUC Minas</b> – Graduate Specialization in Distributed Software Architecture (2025 – 2027, in progress)<br/>"
                 "<b>Anhanguera Educational</b> – Bachelor's in Software Engineering (2021 – 2025)",
    "language_note": language_note_en
}

# ----------------------------------------------------------------------------
# 2. BACK-END NODE.JS (PT-BR e EN-US)
# ----------------------------------------------------------------------------
cv_node_pt = {
    "title": "Desenvolvedor Back-End | Node.js, TypeScript & Arquitetura de APIs",
    "summary": "Desenvolvedor Back-End especializado em Node.js e TypeScript, com foco na construção de APIs RESTful escaláveis, microsserviços e arquiteturas distribuídas. Experiência em otimização de performance, implementação de observabilidade (logging estruturado, métricas) e integração com diversos bancos de dados e serviços cloud (AWS). Atuação em ambientes de alta demanda com foco em qualidade, testes e boas práticas de engenharia de software.",
    "experience_items": [
        "Desenvolvimento de APIs RESTful e microsserviços com Node.js, TypeScript, Express e NestJS, seguindo princípios SOLID e Clean Architecture, aumentando a escalabilidade do sistema em 30%.",
        "Otimização de performance em 35% para fluxos críticos através de melhorias em consultas, implementação de paralelismo e uso eficiente de recursos, incluindo cache com Redis.",
        "Implementação de estratégias avançadas de logging estruturado e correlação de requisições, aumentando a rastreabilidade em 40% e reduzindo o tempo de diagnóstico de erros em 25%.",
        "Configuração de monitoramento com Kibana, criação de dashboards e alertas proativos para métricas de desempenho, melhorando a visibilidade operacional em 30%.",
        "Integração com serviços AWS (Lambda, S3, EC2) para automações e processamento assíncrono, reduzindo custos operacionais em 20%.",
        "Containerização de serviços com Docker e gestão de ciclo de vida de APIs com Postman/Newman, acelerando o tempo de deploy em 50%.",
        "Aplicação de Test-Driven Development (TDD) e participação ativa em code reviews para garantir qualidade do código, elevando a cobertura de testes para 80%."
    ],
    "skills": "<b>Back-End & Frameworks:</b> Node.js, TypeScript, Express.js, NestJS, RESTful APIs<br/>"
              "<b>Linguagens:</b> JavaScript (ES6+), TypeScript<br/>"
              "<b>Bancos de Dados:</b> MongoDB, PostgreSQL, MySQL, Oracle, Redis (cache)<br/>"
              "<b>Testes & Qualidade:</b> Jest (Unit & Integration), Postman, Newman, TDD<br/>"
              "<b>Cloud & DevOps:</b> AWS (Lambda, S3, EC2), Docker, Kubernetes (conceitos), Terraform (conceitos), Jenkins, Git, CI/CD<br/>"
              "<b>Observabilidade:</b> Kibana, Logging Estruturado, Métricas de Performance<br/>"
              "<b>Metodologias & Soft Skills:</b> Scrum, Clean Architecture, SOLID, API Design, Comunicação, Trabalho em Equipe, Resolução de Problemas",
    "projects": [
        "<b>API de Autenticação (Node.js/TypeScript):</b> Desenvolvimento de uma API segura com JWT, refresh tokens, controle de acesso por roles e integração com PostgreSQL.",
        "<b>Microsserviço de Processamento:</b> Criação de um serviço escalável com Node.js para processamento assíncrono de dados, utilizando filas e integração com AWS Lambda."
    ],
    "education": cv_mern_pt["education"],  # Reusa a mesma formação
    "language_note": language_note_pt
}

cv_node_en = {
    "title": "Back-End Developer | Node.js, TypeScript & API Architecture",
    "summary": "Back-End Developer specialized in Node.js and TypeScript, focused on building scalable RESTful APIs, microservices, and distributed architectures. Experience in performance optimization, observability implementation (structured logging, metrics), and integration with various databases and cloud services (AWS). Worked in high-demand environments with a focus on quality, testing, and software engineering best practices.",
    "experience_items": [
        "Developed RESTful APIs and microservices with Node.js, TypeScript, Express, and NestJS, following SOLID and Clean Architecture principles, increasing system scalability by 30%.",
        "Optimized performance by 35% for critical flows through query improvements, parallelism implementation, and efficient resource usage, including caching with Redis.",
        "Implemented advanced structured logging and request correlation strategies, increasing traceability by 40% and reducing error diagnosis time by 25%.",
        "Configured monitoring with Kibana, created dashboards and proactive alerts for performance metrics, improving operational visibility by 30%.",
        "Integrated with AWS services (Lambda, S3, EC2) for automation and asynchronous processing, reducing operational costs by 20%.",
        "Containerized services with Docker and managed API lifecycle with Postman/Newman, speeding up deployment time by 50%.",
        "Applied Test-Driven Development (TDD) and actively participated in code reviews to ensure code quality, raising test coverage to 80%."
    ],
    "skills": "<b>Back-End & Frameworks:</b> Node.js, TypeScript, Express.js, NestJS, RESTful APIs<br/>"
              "<b>Languages:</b> JavaScript (ES6+), TypeScript<br/>"
              "<b>Databases:</b> MongoDB, PostgreSQL, MySQL, Oracle, Redis (caching)<br/>"
              "<b>Testing & Quality:</b> Jest (Unit & Integration), Postman, Newman, TDD<br/>"
              "<b>Cloud & DevOps:</b> AWS (Lambda, S3, EC2), Docker, Kubernetes (concepts), Terraform (concepts), Jenkins, Git, CI/CD<br/>"
              "<b>Observability:</b> Kibana, Structured Logging, Performance Metrics<br/>"
              "<b>Methodologies & Soft Skills:</b> Scrum, Clean Architecture, SOLID, API Design, Communication, Teamwork, Problem Solving",
    "projects": [
        "<b>Authentication API (Node.js/TypeScript):</b> Developed a secure API with JWT, refresh tokens, role-based access control, and PostgreSQL integration.",
        "<b>Processing Microservice:</b> Created a scalable Node.js service for asynchronous data processing, using queues and AWS Lambda integration."
    ],
    "education": cv_mern_en["education"],  # Reusa a mesma formação
    "language_note": language_note_en
}

# ----------------------------------------------------------------------------
# 3. BACK-END JAVA (PT-BR e EN-US)
# ----------------------------------------------------------------------------
cv_java_pt = {
    "title": "Desenvolvedor Back-End | Java, Spring Boot & Arquitetura Distribuída",
    "summary": "Desenvolvedor Back-End com sólida experiência em Java e ecossistema Spring, atuando desde versões corporativas (Java 6) até as mais modernas (Java 17+). Especializado no desenvolvimento de APIs RESTful, microsserviços e sistemas distribuídos com Spring Boot. Foco em qualidade de código, performance (otimização JVM), testes e boas práticas de arquitetura (Clean Architecture, DDD). Experiência prática em projetos de integração e alta disponibilidade.",
    "experience_items": [
        "Desenvolvimento e manutenção de APIs RESTful e microsserviços utilizando Spring Boot, Spring MVC e Spring Data JPA, garantindo 99.9% de disponibilidade.",
        "Otimização de performance de aplicações Java através de análise de GC, tuning de JVM e melhorias em consultas ao banco de dados, resultando em um aumento de 25% no throughput.",
        "Implementação de logging estruturado e estratégias de monitoramento para sistemas distribuídos, aumentando a visibilidade operacional em 40%.",
        "Integração com bancos de dados relacionais (MySQL, PostgreSQL, Oracle) utilizando JPA/Hibernate, garantindo eficiência e consistência, com redução de 30% no tempo de consulta.",
        "Containerização de aplicações Java com Docker e deploy em ambientes cloud (AWS EC2), reduzindo o tempo de deploy em 40%.",
        "Configuração de pipelines CI/CD com Jenkins para build, teste e deploy automatizados, reduzindo o tempo de integração em 50%.",
        "Aplicação de princípios de design (SOLID) e arquiteturas limpas (Clean Architecture) para criação de sistemas sustentáveis, facilitando a manutenção e reduzindo bugs em 20%."
    ],
    "skills": "<b>Linguagens & Plataforma:</b> Java (6, 8, 11, 17+), JVM<br/>"
              "<b>Frameworks & Bibliotecas:</b> Spring Boot, Spring MVC, Spring Data JPA, Hibernate, Maven<br/>"
              "<b>APIs & Protocolos:</b> RESTful APIs, JSON, XML, SOAP (conceitos)<br/>"
              "<b>Bancos de Dados:</b> MySQL, PostgreSQL, Oracle, H2, Redis (cache)<br/>"
              "<b>Testes:</b> JUnit, Mockito, Test Containers<br/>"
              "<b>Ferramentas & DevOps:</b> Docker, Kubernetes (conceitos), Terraform (conceitos), Jenkins, AWS EC2, Git, Postman, Kibana<br/>"
              "<b>Conceitos & Arquitetura:</b> Microsserviços, Clean Architecture, SOLID, DDD, Caching<br/>"
              "<b>Soft Skills:</b> Comunicação, Trabalho em Equipe, Resolução de Problemas",
    "projects": [
        "<b>RestSpring:</b> API RESTful completa desenvolvida com Spring Boot, incluindo JPA/Hibernate, H2 para testes, documentação Swagger/OpenAPI e versionamento de API.",
        "<b>Sistema de Integração:</b> Contribuição para um sistema de integração corporativa utilizando Java e Spring Boot para orquestração de fluxos de dados entre sistemas."
    ],
    "education": cv_mern_pt["education"],
    "language_note": language_note_pt
}

cv_java_en = {
    "title": "Back-End Developer | Java, Spring Boot & Distributed Architecture",
    "summary": "Back-End Developer with solid experience in Java and the Spring ecosystem, working from corporate versions (Java 6) to modern ones (Java 17+). Specialized in developing RESTful APIs, microservices, and distributed systems with Spring Boot. Focus on code quality, performance (JVM optimization), testing, and architecture best practices (Clean Architecture, DDD). Practical experience in integration projects and high availability.",
    "experience_items": [
        "Developed and maintained RESTful APIs and microservices using Spring Boot, Spring MVC, and Spring Data JPA, ensuring 99.9% availability.",
        "Optimized Java application performance through GC analysis, JVM tuning, and database query improvements, resulting in a 25% increase in throughput.",
        "Implemented structured logging and monitoring strategies for distributed systems, increasing operational visibility by 40%.",
        "Integrated with relational databases (MySQL, PostgreSQL, Oracle) using JPA/Hibernate, ensuring efficiency and consistency, with a 30% reduction in query time.",
        "Containerized Java applications with Docker and deployed on cloud environments (AWS EC2), reducing deployment time by 40%.",
        "Configured CI/CD pipelines with Jenkins for automated build, test, and deployment, reducing integration time by 50%.",
        "Applied design principles (SOLID) and clean architectures (Clean Architecture) to create sustainable systems, facilitating maintenance and reducing bugs by 20%."
    ],
    "skills": "<b>Languages & Platform:</b> Java (6, 8, 11, 17+), JVM<br/>"
              "<b>Frameworks & Libraries:</b> Spring Boot, Spring MVC, Spring Data JPA, Hibernate, Maven<br/>"
              "<b>APIs & Protocols:</b> RESTful APIs, JSON, XML, SOAP (concepts)<br/>"
              "<b>Databases:</b> MySQL, PostgreSQL, Oracle, H2, Redis (caching)<br/>"
              "<b>Testing:</b> JUnit, Mockito, Test Containers<br/>"
              "<b>Tools & DevOps:</b> Docker, Kubernetes (concepts), Terraform (concepts), Jenkins, AWS EC2, Git, Postman, Kibana<br/>"
              "<b>Concepts & Architecture:</b> Microservices, Clean Architecture, SOLID, DDD, Caching<br/>"
              "<b>Soft Skills:</b> Communication, Teamwork, Problem Solving",
    "projects": [
        "<b>RestSpring:</b> Complete RESTful API developed with Spring Boot, including JPA/Hibernate, H2 for testing, Swagger/OpenAPI documentation, and API versioning.",
        "<b>Integration System:</b> Contribution to a corporate integration system using Java and Spring Boot for orchestrating data flows between systems."
    ],
    "education": cv_mern_en["education"],
    "language_note": language_note_en
}

# ----------------------------------------------------------------------------
# 4. INTEGRAÇÕES MULESOFT (PT-BR e EN-US)
# ----------------------------------------------------------------------------
cv_mulesoft_pt = {
    "title": "Desenvolvedor de Integrações | MuleSoft & API-Led Connectivity",
    "summary": "Desenvolvedor especializado em integrações corporativas utilizando a plataforma MuleSoft 4.x, com experiência prática em projetos críticos para grandes clientes como a Natura. Expertise na aplicação da arquitetura API-Led Connectivity para desenho e construção de APIs escaláveis, reutilizáveis e governadas. Foco em transformações de dados complexas com DataWeave 2.x, monitoramento, observabilidade (logging estruturado) e melhoria contínua de performance em fluxos de integração.",
    "experience_items": [
        "Projeto, desenvolvimento e manutenção de fluxos de integração (Mule Flows) para APIs corporativas críticas, seguindo a metodologia API-Led Connectivity, reduzindo o tempo de integração entre sistemas em 30%.",
        "Implementação de transformações e manipulações de dados complexas utilizando DataWeave 2.x, garantindo compatibilidade e eficiência entre sistemas heterogêneos, com processamento 25% mais rápido.",
        "Otimização de performance em 25% para processos de negócio críticos através da análise e refatoração de fluxos MuleSoft, aplicação de processamento paralelo e melhoria em consultas.",
        "Configuração de logging estruturado e correlacionado em toda a plataforma, com criação de dashboards no Kibana, aumentando a rastreabilidade de incidents em 40%.",
        "Participação no ciclo de vida completo das APIs no Anypoint Platform: design no Design Center, versionamento, publicação no Exchange e gestão no API Manager.",
        "Aplicação de políticas de segurança (OAuth, TLS), throttling e tratamento robusto de erros em pontos de integração, reduzindo falhas de segurança em 20%.",
        "Trabalho em squad ágil (Scrum), colaborando em refinamentos, code reviews e na definição de boas práticas para a equipe de integração, melhorando a velocidade de entrega em 15%."
    ],
    "skills": "<b>Plataforma MuleSoft:</b> Mule 4, Anypoint Platform, Design Center, API Manager, Runtime Manager, Exchange<br/>"
              "<b>Arquitetura & Metodologia:</b> API-Led Connectivity, Design de APIs (REST/SOAP), Patterns de Integração (EAI)<br/>"
              "<b>Linguagens & Transformação:</b> DataWeave 2.x, Java (para customizações e conectores)<br/>"
              "<b>Ferramentas & DevOps:</b> Maven, Git, Jenkins, Postman/Newman, Kibana, Splunk<br/>"
              "<b>Conceitos & Boas Práticas:</b> Logging Estruturado, Tratamento de Erros, Security Policies (OAuth), SLAs, Throttling<br/>"
              "<b>Cloud & Infra:</b> AWS, Docker (conceitos para runtime), Kubernetes (conceitos)<br/>"
              "<b>Soft Skills:</b> Comunicação, Trabalho em Equipe, Resolução de Problemas Complexos",
    "projects": [
        "<b>Integração de Pedidos - Natura:</b> Desenvolvimento de fluxos MuleSoft para conectar o sistema de pedidos da Natura ao SAP, envolvendo transformações complexas de dados com DataWeave, uso do conector SAP e implementação de políticas de retry e tratamento de erros.",
        "<b>API de Catálogo de Produtos:</b> Criação de uma API layer reutilizável no Anypoint Platform para expor dados de produtos, seguindo o modelo API-Led, com documentação no Exchange e políticas de rate limiting configuradas no API Manager."
    ],
    "education": cv_mern_pt["education"],
    "language_note": language_note_pt
}

cv_mulesoft_en = {
    "title": "Integration Developer | MuleSoft & API-Led Connectivity",
    "summary": "Integration Developer specialized in enterprise integrations using the MuleSoft 4.x platform, with practical experience in critical projects for major clients such as Natura. Expertise in applying API-Led Connectivity architecture to design and build scalable, reusable, and governed APIs. Focus on complex data transformations with DataWeave 2.x, monitoring, observability (structured logging), and continuous improvement of integration flow performance.",
    "experience_items": [
        "Designed, developed, and maintained integration flows (Mule Flows) for critical corporate APIs, following the API-Led Connectivity methodology, reducing system integration time by 30%.",
        "Implemented complex data transformations and manipulations using DataWeave 2.x, ensuring compatibility and efficiency between heterogeneous systems, with 25% faster processing.",
        "Optimized performance by 25% for critical business processes through analysis and refactoring of MuleSoft flows, applying parallel processing and query improvements.",
        "Configured structured and correlated logging across the platform, with dashboard creation in Kibana, increasing incident traceability by 40%.",
        "Participated in the full API lifecycle on Anypoint Platform: design in Design Center, versioning, publishing in Exchange, and management in API Manager.",
        "Applied security policies (OAuth, TLS), throttling, and robust error handling at integration points, reducing security failures by 20%.",
        "Worked in an agile squad (Scrum), collaborating on refinements, code reviews, and defining best practices for the integration team, improving delivery speed by 15%."
    ],
    "skills": "<b>MuleSoft Platform:</b> Mule 4, Anypoint Platform, Design Center, API Manager, Runtime Manager, Exchange<br/>"
              "<b>Architecture & Methodology:</b> API-Led Connectivity, API Design (REST/SOAP), Integration Patterns (EAI)<br/>"
              "<b>Languages & Transformation:</b> DataWeave 2.x, Java (for customizations and connectors)<br/>"
              "<b>Tools & DevOps:</b> Maven, Git, Jenkins, Postman/Newman, Kibana, Splunk<br/>"
              "<b>Concepts & Best Practices:</b> Structured Logging, Error Handling, Security Policies (OAuth), SLAs, Throttling<br/>"
              "<b>Cloud & Infra:</b> AWS, Docker (runtime concepts), Kubernetes (concepts)<br/>"
              "<b>Soft Skills:</b> Communication, Teamwork, Complex Problem Solving",
    "projects": [
        "<b>Order Integration - Natura:</b> Developed MuleSoft flows to connect Natura's order system to SAP, involving complex data transformations with DataWeave, use of SAP connector, and implementation of retry and error handling policies.",
        "<b>Product Catalog API:</b> Created a reusable API layer on Anypoint Platform to expose product data, following the API-Led model, with documentation in Exchange and rate-limiting policies configured in API Manager."
    ],
    "education": cv_mern_en["education"],
    "language_note": language_note_en
}


cv_hybrid_pt = {
    "title": "Software Engineer | Java, Spring Boot, React & Sistemas Corporativos",
    "summary": (
        "Engenheiro de Software com experiência em desenvolvimento e sustentação de sistemas "
        "corporativos, atuando em backend com Java e Spring Boot, front-end com React e integrações "
        "de APIs em ambientes de alta criticidade. Atuação em projetos de grande porte para o "
        "ecossistema Natura, com foco em performance, observabilidade, confiabilidade e resolução "
        "de incidentes. Experiência em suporte N2/N3, análise de falhas, correção de bugs e evolução contínua."
    ),
    "experience_items": [
        "Desenvolvimento e manutenção de APIs RESTful com Java e Spring Boot em sistemas corporativos.",
        "Atuação em suporte N2/N3 com análise de logs, identificação de causa raiz e correção de incidentes.",
        "Atendimento e resolução de chamados técnicos utilizando ServiceNow e TD (Team Dynamix), garantindo SLA e satisfação do cliente.",
        "Desenvolvimento e evolução de interfaces web com React.js integradas ao backend.",
        "Implementação de observabilidade com logging estruturado e Kibana, aumentando rastreabilidade em 40%.",
        "Otimização de fluxos críticos, reduzindo tempo de resposta em até 30%.",
        "Integração entre sistemas internos e externos utilizando MuleSoft e APIs REST.",
        "Participação ativa em rituais ágeis, code reviews e alinhamento técnico com áreas de negócio."
    ],
    "skills": (
        "<b>Backend:</b> Java, Spring Boot, Node.js, TypeScript, Express<br/>"
        "<b>Frontend:</b> React.js, Hooks, Context API<br/>"
        "<b>Integrações:</b> MuleSoft, REST APIs, API-Led Connectivity<br/>"
        "<b>Bancos:</b> Oracle, PostgreSQL, MySQL, MongoDB<br/>"
        "<b>Cloud & DevOps:</b> AWS, Docker, Jenkins, Kibana<br/>"
        "<b>Service Management:</b> ServiceNow, TD (Team Dynamix), Gestão de Chamados<br/>"
        "<b>Suporte & Qualidade:</b> Debug, Sustentação N2/N3, TDD, Clean Code, SOLID"
    ),
    "projects": [
        "<b>Sistemas Corporativos Natura:</b> Desenvolvimento, sustentação e evolução de APIs e interfaces web.",
        "<b>Plataforma Backend Java:</b> Otimização de performance, observabilidade e confiabilidade."
    ],
    "education": (
        "<b>PUC Minas</b> – Pós-Graduação em Arquitetura de Software Distribuído (em andamento)<br/>"
        "<b>Anhanguera Educacional</b> – Bacharelado em Engenharia de Software"
    ),
    "language_note": "Inglês: Iniciante (leitura técnica)"
}

# Lista de todos os currículos (dicionários) com seus nomes de arquivo
all_cvs = [
    (cv_mern_pt, "Benevanio_CV_MERN_FullStack_PT.pdf"),
    (cv_mern_en, "Benevanio_CV_MERN_FullStack_EN.pdf"),
    (cv_node_pt, "Benevanio_CV_Node_Backend_PT.pdf"),
    (cv_node_en, "Benevanio_CV_Node_Backend_EN.pdf"),
    (cv_java_pt, "Benevanio_CV_Java_Backend_PT.pdf"),
    (cv_java_en, "Benevanio_CV_Java_Backend_EN.pdf"),
    (cv_mulesoft_pt, "Benevanio_CV_MuleSoft_Integrations_PT.pdf"),
    (cv_mulesoft_en, "Benevanio_CV_MuleSoft_Integrations_EN.pdf"),
    (cv_hybrid_pt, "Benevanio_CV_Hybrid_Systems_PT.pdf")
]

# Gerar cada currículo
for cv_data, filename in all_cvs:
    build_cv(
        filename,
        cv_data["title"],
        cv_data["summary"],
        cv_data["experience_items"],
        cv_data["skills"],
        cv_data["projects"],
        cv_data["education"],
        cv_data["language_note"]
    )
    print(f"Gerado: {filename}")

print("\n✅ Todos os  currículos foram gerados com sucesso!")