# EveryMindDesafio
Esse repositório tem como objetivo armazenar os arquivos utilizados para realização do desafio EveryMind - Best Minds 2024.

Para o desenvolvimento do projeto, foi utilizando Python com o microframework Flask, integrado ao banco de dados PostgreSQL. O sistema permite ao usuário realizar operações descritas no enunciado (criar, eer, atualizar, deletar) em uma tabela de produtos, a qual contém campos com nome, código, descrição e preço do produto.

A interface do usuário foi construída de maneira simples, com o objetivo de cumpri o desafio, por meio de HTML e Flask. Para cada produto, foi desenvolvida a funcionalidade de exibição, onde todas as informações do produto são apresentadas, mas sem a opção de edição, conforme meu entendimento do enunciado.

Optei por estruturar o projeto da maneira mais modular possível, dividindo entre a definição do modelo de dados (models.py), a logica de aplicação (app.py) e os templates de interface do usuário (arquivos HTML do diretório templates/). Por fim, a configuração do banco de dados foi realizada utilizando o PostgreSQL.

Por fim, o diretório “exibir” apresenta alguns prints, documentando o teste de funcionamento de todas as operações descritas no enunciado.
