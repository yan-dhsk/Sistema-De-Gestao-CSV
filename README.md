SOBRE O SISTEMA

Este projeto é um sistema de gestão empresarial completo, desenvolvido como meu primeiro grande projeto durante o 2º período da minha graduação em Sistemas de Informação. A aplicação, feita em Python, foi planejada para ser modular e escalável. Atualmente, seu módulo principal de controle de produtos está totalmente funcional, utilizando um arquivo CSV como base de dados leve e portátil.

OBJETIVO

O objetivo foi planejar a arquitetura de um sistema de gestão abrangente e implementar seu módulo central de produtos como prova de conceito. O desenvolvimento buscou aplicar e consolidar conhecimentos essenciais de programação, como a arquitetura de software baseada em um diagrama de classes previamente feito, a programação modularizada para separar as camadas de lógica e apresentação, a persistência de dados em arquivos CSV, a implementação da lógica de negócio para operações CRUD e a criação de uma interface de usuário interativa via linha de comando.

TECNOLOGIAS UTILIZADAS

    Python 3
    Módulo nativo 'csv'
    Git e GitHub

ESTRUTURA DO PROJETO

/
|-- Main.py (Camada de Apresentação e interação com o usuário).
|-- CRUD_produto.py (Camada de Dados para o módulo de produtos).
|-- listaProdutos.csv (Base de dados do módulo de produtos).
|-- .gitignore (Arquivo para ignorar arquivos de cache).
|-- README.md (Documentação do projeto).

COMO EXECUTAR

    Clone o repositório:
    git clone https://github.com/yan-dhsk/Sistema-De-Gestao-CSV.git
    Navegue até o diretório do projeto:
    cd Sistema-De-Gestao-CSV
    Execute o script principal:
    python Main.py
    Siga as instruções do menu para interagir com o módulo de produtos.

AUTOR

Desenvolvido por Yan Neves.
Perfil no GitHub: https://github.com/yan-dhsk
