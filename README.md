# IR2PC

[![GitHub license](https://img.shields.io/github/license/vitorugz/IR2PC)](./LICENSE)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue?logo=python)](https://www.python.org/)
[![Made with Arduino](https://img.shields.io/badge/Made%20with-Arduino-00979D?logo=arduino)](https://www.arduino.cc/)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)](https://github.com/seu-usuario-aqui/IR2PC)

**Controle seu computador com um controle remoto de TV!**  
**IR2PC** é um projeto que une **Arduino**, **C++** e **Python** para permitir a automação de ações no PC utilizando comandos enviados por um controle remoto infravermelho. O infravermelho usado foi reaproveitado de uma fita de led RGB antiga que eu tinha, removi o sensor e reaproveitei.

---

## 💡 Como funciona?

O projeto é dividido em duas partes principais:

### 🔧 Arduino (C++)

- Utiliza um receptor infravermelho com a biblioteca `IRremote`.
- Capta sinais do controle remoto **CR2FP**.
- Interpreta o sinal e envia um código para o **monitor serial** via USB.
- Utiliza uma placa **Arduino Uno**.

### 🐍 Python

- Um script Python lê continuamente a porta serial.
- Ao receber um código, ele:
  - Valida o comando.
  - Executa a ação correspondente no computador:
    - mover o mouse, pressionar teclas, aumentar/diminuir volume etc.
- Uma interface gráfica exibe:
  - 🔁 Modo atual (Mouse ou Teclado)
  - 🔘 Último comando recebido
  - ⚙️ Última ação executada

---

## 🖥️ Funcionalidades

- Alternar entre modo:
    - **Mouse**: Para controlar o cursor do mouse com as setas do controle
    - **Teclado**: Para controlar as setas do teclado com as setas do controle
- Aumentar, diminuir e mutar o volume
- Executar atalhos como:
    - Pressionar o botão do windows
    - Desligar o computador
    - Abrir o Explorador de arquivos
    - Abrir o YouTube no navegador Opera
    - Abrir o VSCode
- Utilizar qualquer botão do controle remoto para ações específicas

---

## ⚙️ Tecnologias usadas

| Tecnologia | Função |
|------------|--------|
| **C++** (Arduino) | Leitura de sinais infravermelho |
| **IRremote** | Biblioteca para interpretar comandos IR |
| **Python 3.x** | Script principal de controle |
| `pyserial` | Comunicação serial entre Arduino e Python |
| `pyautogui` | Ações de mouse e teclado no computador |
| `tkinter` | Interface gráfica simples (GUI) |

---

## 🧰 Requisitos

- **Placa**: Arduino Uno
- **Sensor**: VS1838B (ou compatível)
- **Controle remoto**: CR2FP (ou qualquer outro com protocolo compatível)
- **Python 3.x** instalado
- **Dependências Python**:
  ```bash
  pip install pyserial pyautogui keyboard

## 🚀 Como usar

1. Conecte o sensor IR ao Arduino Uno
   - Pino VCC  na porta 5V do Arduino
   - GND       na porta GND do Arduino
   - OUT       na porta 8 do Arduino
2. Envie o código C++ para o Arduino utilizando a IDE do Arduino
3. Conecte o Arduino via USB
4. Clone este repositório:
  ```bash
  git clone https://github.com/seu-usuario-aqui/IR2PC.git
  cd IR2PC
  ```
5. Instale as dependências Python:
   ```bash
    pip install pyserial pyautogui keyboard
   ```
6. Execute o script principal:
   ```bash
    python main.py
   ```
7. Aponte o controle para o sensor e divirta-se

## 📸 Imagens
![Imagem do WhatsApp de 2025-04-20 à(s) 21 22 18_70909d49](https://github.com/user-attachments/assets/be195354-7fd1-4af4-95ac-949257648cd3)

## 👨‍💻 Autor
**Desenvolvido** por Vitor
Desenvolvedor Back-end Python | Amante de automações, hardware e projetos criativos 🚀
