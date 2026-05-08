# 🤖 Python Game Automation Bot
<div align="center">
  <img width="478" height="286" alt="image" src="https://github.com/user-attachments/assets/ef4e4de9-39b4-4d4f-9bd9-7054010fe7f7" />
</div>

> 🇧🇷 [Português](#português) | 🇺🇸 [English](#english)

---

## English

A Python automation tool with real-time screen capture and image recognition that detects visual cues on screen and executes timed input sequences automatically.

Two versions available depending on server latency:
- `slow_auto.py` — for high latency servers
- `fast_auto.py` — for low latency servers

### Technical Highlights
- **Real-time screen capture** — captures specific screen regions using `mss` for efficient pixel-level analysis
- **Image recognition** — detects target images on screen using `pyautogui.locate` with configurable confidence threshold
- **Threaded architecture** — bot loop runs on a separate thread, keeping the GUI responsive
- **Hang detection** — monitors cycle count and automatically closes the application if the bot gets stuck
- **Configurable regions** — search areas defined by pixel coordinates, easily adjustable per setup

### Features
- 🖥️ Tkinter GUI with start/stop controls
- ⌨️ F8 hotkey to toggle the bot on/off
- 🔍 Image recognition with adjustable confidence level
- 📸 Efficient screen capture limited to defined regions
- 🔄 Periodic action sequences triggered by cycle count

### Built with
- Python
- `mss`, `pyautogui`, `pydirectinput`, `tkinter`, `keyboard`, `threading`, `numpy`

### About
Built with AI assistance (Claude). Requirements, testing and iteration were done manually.

I normally write my own code, but in this case I used AI to get the tool out 
quickly for the players and for myself. I know AI-generated code can have 
quality, security and scalability issues, so I made sure to understand the 
main functions and libraries involved, not just ship it.

---

## Português

Ferramenta de automação em Python com captura de tela em tempo real e reconhecimento de imagem que detecta elementos visuais na tela e executa sequências de input automaticamente.

Duas versões disponíveis dependendo da latência do servidor:
- `slow_auto.py` — para servidores com alta latência
- `fast_auto.py` — para servidores com baixa latência

### Destaques Técnicos
- **Captura de tela em tempo real** — captura regiões específicas da tela com `mss` para análise eficiente de pixels
- **Reconhecimento de imagem** — detecta imagens alvo na tela via `pyautogui.locate` com threshold de confiança configurável
- **Arquitetura com threads** — o loop do bot roda em thread separada, mantendo a GUI responsiva
- **Detecção de travamento** — monitora o contador de ciclos e fecha automaticamente se o bot travar
- **Regiões configuráveis** — áreas de busca definidas por coordenadas de pixels, facilmente ajustáveis

### Funcionalidades
- 🖥️ GUI em Tkinter com controles de start/stop
- ⌨️ Hotkey F8 para ativar/pausar o bot
- 🔍 Reconhecimento de imagem com nível de confiança ajustável
- 📸 Captura de tela eficiente limitada a regiões definidas
- 🔄 Sequências de ações periódicas disparadas por contador de ciclos

### Tecnologias
- Python
- `mss`, `pyautogui`, `pydirectinput`, `tkinter`, `keyboard`, `threading`, `numpy`

### Sobre
Desenvolvido com assistência de IA (Claude). Requisitos, testes e iterações foram feitos manualmente.

Normalmente escrevo meu próprio código, mas nesse caso usei IA para 
disponibilizar a ferramenta rapidamente para os jogadores e para mim mesmo. 
Sei que código gerado por IA pode ter problemas de qualidade, segurança e 
escalabilidade, então me preocupei em entender as principais funções e 
bibliotecas do código, não só em entregar.

