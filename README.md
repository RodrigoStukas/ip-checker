# 📡 IP Checker

Um utilitário simples em Python que exibe um **widget flutuante** mostrando o **IP corporativo** da máquina.  
Caso nenhum IP corporativo seja detectado, o sistema exibe um alerta solicitando a ativação da **VPN**.

---

## 🚀 Funcionalidades

- Detecta e exibe o **IP corporativo** em tempo real
- Widget flutuante em formato de **bolinha**
- Widget **arrastável** pela tela
- Clique para abrir uma janela com:
  - Hostname da máquina
  - IP corporativo detectado
- Botão para **copiar o IP** para a área de transferência
- Alerta automático quando não estiver conectado à rede corporativa

---

## 📦 Requisitos

- **Python 3.10 ou superior**

### Bibliotecas externas
- `psutil` — coleta informações de rede
- `Pillow` — manipulação de imagens

### Bibliotecas padrão do Python

- `tkinter`  
  > Em algumas distribuições Linux pode ser necessário instalar manualmente:
  
  
  ```bash 
   ```sudo apt-get install python3-tk

---
- socket

- os

- unittest

---

### 📄 requirements.txt

Conteúdo do arquivo requirements.txt:

psutil
Pillow

---

## 🔧 Instalação

### 1️⃣ Clonar o repositório

git clone https://github.com/RodrigoStukas/ip-checker

#### Abrir no terminal:
cd ip-checker

---

### 2️⃣ Instalar dependências

pip install -r requirements.txt
Ou manualmente:
pip install psutil Pillow

---

## ▶️ Executar o projeto
Com o terminal aberto na raiz do projeto:

python -m src.main

---

## 🧪 Testes
Para executar os testes unitários:

python -m unittest discover -s tests

---

## 📌 Observações

São considerados IPs corporativos:

Endereços iniciados com 10.

Endereços iniciados com 172.21.

Caso nenhum IP válido seja encontrado, o sistema exibirá um aviso para ligar a VPN

O widget é transparente, leve e pode ser movido livremente pela tela

---

## 🖼️ Exemplo de Uso

Ao executar o programa, um ícone flutuante aparece na tela

Clique para abrir a janela de informações

Botão para copiar o IP

Opções de Abrir e Sair

---

## 🛠️ Contribuição

Contribuições são bem-vindas!
Sinta-se à vontade para abrir issues ou enviar pull requests.

---

## 📄 Licença

Este projeto está sob a licença MIT.
Consulte o arquivo LICENSE para mais detalhes.

---
