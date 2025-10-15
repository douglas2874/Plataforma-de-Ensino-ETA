# 🚀 **ETA - Ensino Tecnológico Avançado**

## Sistema de Gestão Educacional para Escolas de Tecnologia

> Breve descrição de alto nível: A **ETA - Ensino Tecnológico Avançado** é uma solução robusta e moderna, focada em otimizar a gestão acadêmica e pedagógica em escolas de ensino de tecnologia. Ele fornece ferramentas essenciais para **professores** e **coordenadores** gerenciarem turmas, alunos, atividades e promoverem a colaboração.

-----

## ✨ Funcionalidades Principais

O sistema foi desenhado para ser o centro de operações para a equipe pedagógica, com um acesso simplificado para os alunos.

### Para Professores e Coordenadores (Back-office)

| Código | Requisito Funcional | Descrição |
| :---: | :--- | :--- |
| **RF01** | **Gestão de Cadastro** | Cadastro, atualização e consulta de **Turmas** e **Alunos(as)** de forma eficiente. |
| **RF02** | **Diário Eletrônico** | Registro detalhado de **Aulas**, controle de **Frequência** e **Observações** pedagógicas por aluno(a). |
| **RF03** | **Gestão de Atividades** | **Upload** de materiais e atividades, acompanhamento de **Status** de envio e visualização por parte dos alunos. |
| **RF05** | **Relatórios e Busca** | Geração de **Relatórios** completos sobre turmas, desempenho e atividades. Ferramentas avançadas de **Busca e Ordenação**. |
| **RF04** | **Fórum e Colaboração** | Ferramenta de **Interação** (Fórum) para comunicação, comentários em atividades e compartilhamento de informações entre todos os usuários. |

### Para Alunos(as) (Front-office)

  * **Acesso a Conteúdo:** Visualização de aulas gravadas e materiais postados.
  * **Envio de Atividades:** Possibilidade de visualizar, responder e enviar as atividades propostas pelos professores.
  * **Interação:** Participação no fórum de discussão com colegas e professores.

-----

## 🛠️ Tecnologias e Arquitetura

Este projeto adota uma abordagem moderna e especializada, combinando a versatilidade de linguagens de alto nível com a eficiência de baixo nível para módulos críticos. A arquitetura contempla também uma camada de apresentação robusta e responsiva, construída com tecnologias web amplamente consolidadas.

### Linguagens e Ferramentas (RNF02)

- **Python**: Utilizado para a maior parte dos algoritmos de gerenciamento de dados, estruturas complexas e lógica de negócio.
- **C Estruturado**: Empregado em módulos críticos próximos ao hardware ou que exigem alta performance e manipulação de baixo nível.
- **HTML, CSS e JavaScript**: Aplicados na construção da interface do usuário, garantindo uma experiência interativa, responsiva e compatível com múltiplos dispositivos e navegadores.

### Arquitetura (RNF04)

  * **Modelo Cliente-Servidor:** O sistema funciona em uma **rede local**, garantindo performance e segurança de acesso.
  * **Acesso Distribuído (RF06):** Suporte nativo para **múltiplos usuários simultâneos**, com arquitetura distribuída para garantir a **consistência** e **integridade dos dados**.
  * **Acesso Remoto:** Previsão de mecanismos de **acesso remoto seguro** para coordenadores ou gestores.

### Inovação e Diferenciais

  * **Inteligência Artificial (RNF03):** Exploração de recursos de **IA** para aprimorar o gerenciamento acadêmico, como **sugestões automáticas de relatórios** e **análise preditiva de dados** de desempenho.
  * **Sustentabilidade (RNF06):** Foco na **digitalização** (*paperless*), substituindo relatórios em papel por versões digitais, e inclusão de **métricas de sustentabilidade** no escopo de desenvolvimento.

-----

## 📜 Desenvolvimento e Qualidade

O processo de desenvolvimento é guiado por práticas que garantem a qualidade e a rastreabilidade do projeto.

### Metodologia e Gerenciamento

  * **Metodologia Ágil (RNF01):** O projeto é desenvolvido utilizando práticas de engenharia de *software* ágil, com organização de **sprints**, gerenciamento de **backlog** e acompanhamento contínuo do progresso.

### Documentação e Qualidade (RNF05)

  * **Código Comentado:** Priorizamos um código-fonte funcional e devidamente comentado.
  * **Modelagem UML:** O projeto inclui diagramas **UML** (Casos de Uso, Classes e Sequência) para visualização clara da arquitetura e interações do sistema.
  * **Testes e Homologação:** Será fornecido um plano detalhado de **homologação e testes** para garantir a robustez do sistema.
  * **Manual de Uso:** Criação de um **manual** claro e completo para facilitar a adoção pelos usuários finais (professores e coordenadores).

-----

## 💻 Como Executar o Projeto Localmente

**(Instruções detalhadas serão adicionadas aqui após a definição da arquitetura de *deploy* - Ex: *docker-compose*, compilação dos módulos C, ambiente Python, etc.)**

1.  **Pré-requisitos:**
      * Python [Versão]
      * Compilador C ([Nome do Compilador])
      * [Outros softwares necessários]
2.  **Clone o repositório:**
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```
3.  **Configuração do Ambiente Python:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Compilação dos Módulos em C:**
    ```bash
    # Exemplo de comando de compilação
    gcc -o modulo_critico src/modulo_critico.c
    ```
5.  **Execução do Servidor:**
    ```bash
    python main.py
    ```

-----

## 🤝 Contribuição

Contribuições são bem-vindas\! Se você tiver sugestões ou quiser contribuir com o código, por favor, abra uma *Issue* ou um *Pull Request*.

-----

## 👤 Autor

  * **[Douglas Borges e João Victor Lírio ]** 