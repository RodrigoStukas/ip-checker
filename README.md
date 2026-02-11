# 📡 IP Checker

Um utilitário simples em Python que exibe um \*\*widget flutuante\*\* mostrando o \*\*IP corporativo\*\* da máquina.

Caso nenhum IP corporativo seja detectado, o sistema exibe um alerta solicitando a ativação da \*\*VPN\*\*.

---

## 🚀 Funcionalidades

- Detecta e exibe o \*\*IP corporativo\*\* em tempo real

- Widget flutuante em formato de \*\*bolinha\*\*

- Widget \*\*arrastável\*\* pela tela

- Clique para abrir uma janela com:

- Hostname da máquina

- IP corporativo detectado

- Botão para \*\*copiar o IP\*\* para a área de transferência

- Alerta automático quando não estiver conectado à rede corporativa

---

## 📦 Requisitos

- \*\*Python 3.10 ou superior\*\*

### Bibliotecas externas

- `psutil` — coleta informações de rede

- `Pillow` — manipulação de imagens

### Bibliotecas padrão do Python

- `tkinter`

> Em algumas distribuições Linux pode ser necessário instalar manualmente:

`sudo apt-get install python3-tk`

- `socket`

- `os`

- `unittest`

---

## 🔧 Instalação

### 1️⃣ Clone o repositório

```bash

git clone https://github.com/seuusuario/ip-checker.git

cd ip-checker

2️⃣ Instale as dependências

pip install -r requirements.txt

Ou instale manualmente:

pip install psutil Pillow

▶️ Executar o Projeto

Com o terminal aberto na raiz do projeto, execute:

python -m src.main


🧪 Testes

Para executar os testes unitários:

python -m unittest discover -s tests


📂 Estrutura do Projeto

ip-checker/

│

├── assets/ # Ícones e imagens

├── src/

│ ├── network/

│ │ └── ip\_checker.py # Funções de rede (hostname, IP corporativo, etc.)

│ ├── ui/

│ │ └── popup.py # Interface gráfica (widget flutuante)

│ └── main.py # Ponto de entrada do programa

│

├── tests/

│ └── test\_ip\_checker.py # Testes unitários

│

├── requirements.txt # Dependências do projeto

└── README.md # Documentação


📌 Observações

O sistema considera IP corporativo os endereços que começam com:

10.

172.21.

Caso nenhum IP válido seja encontrado, um aviso para ligar a VPN será exibido

O widget é transparente, leve e pode ser movido livremente pela tela


🖼️ Exemplo de Uso

Ao executar o programa, um ícone flutuante aparecerá na tela

Clique para abrir a janela de informações

Botão para copiar o IP

Menu com opções Abrir e Sair


📄 Licença

Este projeto está sob a licença MIT.

Consulte o arquivo LICENSE para mais detalhes.