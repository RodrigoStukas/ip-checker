# IP Checker

Um utilitário simples em Python que exibe um **popup flutuante** mostrando o **IP corporativo** da máquina.  
Se não houver IP da rede corporativa, o programa alerta para ligar a VPN.

---

## 🚀 Funcionalidades
- Mostra o **IP corporativo** em tempo real.
- Exibe um **widget flutuante** em forma de bolinha roxa com "IP".
- Permite **arrastar** a bolinha pela tela.
- Ao **clicar**, abre uma janela com informações detalhadas:
  - Hostname da máquina
  - IP corporativo detectado
- Botão para **copiar IP** para a área de transferência.

---

## 📦 Requisitos
- Python **3.10+**
- Dependências:
  - `psutil`
  - `Pillow`

---

## 🔧 Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/seuusuario/ip-checker.git
cd ip-checker
