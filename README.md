## 🚀 SpaceGuard — Sistema Inteligente de Monitoramento Espacial


## 📌 Visão Geral
O SpaceGuard é um sistema de monitoramento em tempo real desenvolvido para simulação de cápsulas espaciais. O projeto integra computação física, processamento de dados e visão computacional, utilizando Python e OpenCV para criar uma interface intuitiva no estilo "painel de controle" de uma nave espacial.

O sistema processa dados de sensores (temperatura e luminosidade) e gera alertas automáticos de segurança, simulando os desafios de um ambiente crítico de missão espacial.


## 🎯 Objetivo
Garantir o monitoramento contínuo de variáveis ambientais críticas dentro de uma cápsula espacial simulada, fornecendo:

- Monitoramento: Visualização em tempo real de métricas.

- Diagnóstico: Classificação automática de risco baseada em thresholds.

- Interface: Experiência imersiva com visual cockpit.

- Simulação: Replicação fiel de sistemas de telemetria aeroespacial.


## ⚙️ Funcionalidades
🌡️ Telemetria em Tempo Real
- Monitoramento de Temperatura (°C).

- Monitoramento de Luminosidade (%).

## 🖥️ Interface Gráfica Dinâmica
- Interface construída nativamente com OpenCV.

- Estilo de cockpit espacial (Cápsula: ISIS-IX).

- Atualização de frames em tempo real.


## 🚨 Sistema de Alertas Inteligentes
Classificação automática do estado da cápsula:

🟢 OPERACIONAL

🟡 ATENÇÃO

🔴 PERIGO CRÍTICO

📊 Visualização de Dados
- Histórico gráfico de temperatura.

- Barras de progresso dinâmicas.

- Indicadores visuais de status (Gauges).

⚠️ Modo de Emergência
Alertas visuais intermitentes em situações de perigo crítico.


## 🧠 Tecnologias Utilizadas
- Python 3.x

- OpenCV (cv2): Renderização gráfica e processamento de imagem.

- NumPy: Processamento numérico e manipulação de arrays.


## 🚀 Como Executar
- 📦 Pré-requisitos
Certifique-se de ter o Python instalado e instale as dependências:

**Bash**
`pip install opencv-python numpy`

### Node-RED
Instale o Node-RED e importe o flow.json

## ▶️ Execução
Clone este repositório:

Bash
`git clone <url-do-repositorio>`
Acesse a pasta do projeto:


Bash
`cd spaceguard`
Execute o sistema:


Bash
`python main.py`


Abra o Wokwi e execute a simulação

Abra o Node-RED e importe o flow.json

Voce pode alterar as informações de Temperatura e Luminosidade no proprio Wokwi

Na aba de Debug do Node-RED voce vai ver as informações sendo atualizadas em tempo real

Na aba de dashboard voce vera um esboço dos graficos e informações sendo registradas


## ⌨️ Controles
Pressione ESC a qualquer momento para encerrar a simulação em python.

## 🧩 Arquitetura do Sistema
- desenhar_card_transparente(): Função auxiliar para a criação de elementos visuais com efeito glassmorphism.

- Loop Principal: Gerencia a amostragem de dados a cada 2 segundos, valida condições de segurança e renderiza a interface.

- Renderização: Utilização intensiva de primitivas gráficas (cv2.putText, cv2.rectangle, cv2.circle).


## 📈 Possíveis Melhorias
- Integração com hardware real (IoT / ESP32).

- Implementação de modelos de Machine Learning para predição de falhas.


## 👥 Integrantes
Gustavo Vieira Lopes Martins — RM555885

Gustavo Yuji Osugi — RM555034

Kaio Drago Lima Souza — RM556095

Otávio Santos de Lima Ferrão — RM556452

Vitor Rivas Cardoso — RM556404

## 🛰️ Observação Final
Este projeto simula um sistema crítico de monitoramento espacial com foco em visualização em tempo real, lógica de estados e interface inspirada em sistemas aeroespaciais reais.


## Prototipo no Wokwi
`https://wokwi.com/projects/465112817023960065`
<img width="1655" height="729" alt="image" src="https://github.com/user-attachments/assets/03b4542e-f314-4cba-a33d-995ad3c553f3" />


## Dashboard no Node-RED
<img width="1869" height="911" alt="image" src="https://github.com/user-attachments/assets/9f5a8d96-9bf0-4833-a0f5-8321070b7621" />

## Dashboard Simulado em Python
<img width="1274" height="745" alt="image" src="https://github.com/user-attachments/assets/cfc45c38-d491-49c0-afb4-4a64fa1683e8" />

