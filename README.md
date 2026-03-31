# 🏦 Projeto Banco em Python (Em Desenvolvimento)

## 📌 Descrição

Este projeto é uma simulação de um sistema bancário simples desenvolvido em Python. Ele permite realizar operações básicas como depósito, saque, criação de usuários e contas, além de exibir extratos.

O objetivo principal é praticar conceitos de programação como:

* Programação orientada a objetos (POO)
* Modularização de código
* Manipulação de dados
* Regras de negócio simples

---

## ⚙️ Funcionalidades
(Em desenvolvimento)

---

## 🧠 Regras de Negócio

* O usuário é identificado pelo CPF
* Não é permitido cadastrar dois usuários com o mesmo CPF
* O saque possui:

  * Limite de valor por operação
  * Limite de número de saques diários
* Não é possível sacar valores maiores que o saldo disponível

---

## 🗂️ Estrutura do Projeto

```
Projeto_BancoPython-main/
│
├── desafio.py                # Arquivo principal (menu e fluxo do sistema)
│
├── Cliente/
│   └── Cliente.py
│
├── Conta/
│   └── Conta.py
│
├── ContaCorrente/
│   └── ContaCorrente.py
│
├── Historico/
│   └── Historico.py
│
├── PessoaFisica/
│   └── PessoaFisica.py
│
├── Transacao/
│   ├── Transacao.py
│   ├── Deposito.py
│   └── Saque.py
│
└── LICENSE
```

---

## ▶️ Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/Williansilva2207/Projeto_BancoPython.git
```

### 2. Acesse a pasta do projeto

```bash
cd Projeto_BancoPython-main
```

### 3. Execute o programa

```bash
python desafio.py
```

---

## 💻 Exemplo de Uso

Ao rodar o sistema, você verá um menu como este:

```
[d] Depositar
[s] Sacar
[e] Extrato
[nc] Nova conta
[lc] Listar contas
[nu] Novo usuário
[q] Sair
```

Basta digitar a opção desejada e seguir as instruções.

---

## 🧩 Tecnologias Utilizadas

* Python 3.13

---

## 📚 Aprendizados

Este projeto ajuda a entender:

* Estruturação de projetos em Python
* Separação de responsabilidades (classes e módulos)
* Criação de sistemas baseados em regras

---

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

---

## 🚀 Melhorias Futuras

* Interface gráfica
* Persistência de dados (banco de dados)
* Sistema de autenticação
* API REST

---

## 👨‍💻 Autor
Willian Rodrigues Lima Silva
Desenvolvido como projeto de estudo.
