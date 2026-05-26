import cv2
import numpy as np
import random
import time

# =====================================
# CONFIGURAÇÕES E VARIÁVEIS
# =====================================
WIDTH, HEIGHT = 1280, 720

temperatura = 22.0
luminosidade = 65.0  # NOVO SENSOR DE LUZ

historico_temp = []
historico_luz = []

ultimo_update = time.time()

# Paleta de Cores
COR_FUNDO = (14, 11, 11)
COR_CARD = (35, 28, 28)
COR_TEXTO_MUTED = (160, 150, 140)
COR_BORDAS = (70, 60, 55)

# =====================================
# FUNÇÕES AUXILIARES
# =====================================
def desenhar_card_transparente(img, pt1, pt2, cor_bg, alpha=0.4):
    overlay = img.copy()
    cv2.rectangle(overlay, pt1, pt2, cor_bg, -1)
    cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0, img)
    cv2.rectangle(img, pt1, pt2, COR_BORDAS, 1, cv2.LINE_AA)

# =====================================
# LOOP PRINCIPAL
# =====================================
while True:

    # =====================================
    # ATUALIZAÇÃO DOS SENSORES
    # =====================================
    if time.time() - ultimo_update > 2:

        temperatura = round(random.uniform(10, 35), 1)

        # Simulação da luminosidade (%)
        luminosidade = round(random.uniform(0, 100), 1)

        historico_temp.append(temperatura)
        historico_luz.append(luminosidade)

        if len(historico_temp) > 58:
            historico_temp.pop(0)

        if len(historico_luz) > 58:
            historico_luz.pop(0)

        ultimo_update = time.time()

    # =====================================
    # STATUS TEMPERATURA
    # =====================================
    if 18 <= temperatura <= 25:
        status = "OPERACIONAL"
        cor_status = (100, 230, 40)

    elif temperatura < 15 or temperatura > 27:
        status = "PERIGO CRITICO"
        cor_status = (50, 50, 255)

    else:
        status = "ATENCAO"
        cor_status = (0, 190, 255)

    # =====================================
    # STATUS LUMINOSIDADE
    # =====================================
    if luminosidade < 30:
        status_luz = "BAIXA"
        cor_luz = (255, 180, 0)

    elif luminosidade > 80:
        status_luz = "INTENSA"
        cor_luz = (0, 255, 255)

    else:
        status_luz = "NORMAL"
        cor_luz = (100, 230, 40)

    # =====================================
    # BASE DA TELA
    # =====================================
    tela = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
    tela[:] = COR_FUNDO

    # Grade espacial
    for x in range(0, WIDTH, 80):
        cv2.line(tela, (x, 0), (x, HEIGHT), (22, 18, 18), 1)

    for y in range(0, HEIGHT, 80):
        cv2.line(tela, (0, y), (WIDTH, y), (22, 18, 18), 1)

    # =====================================
    # HEADER
    # =====================================
    desenhar_card_transparente(
        tela, (0, 0), (WIDTH, 70), COR_CARD, alpha=0.6
    )

    cv2.putText(
        tela,
        "SISTEMA DE MONITORAMENTO VITAL",
        (50, 45),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (245, 240, 240),
        2,
        cv2.LINE_AA
    )

    cv2.putText(
        tela,
        "CAPSULA: ISIS-IX | ONLINE",
        (950, 43),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        COR_TEXTO_MUTED,
        1,
        cv2.LINE_AA
    )

    # =====================================
    # CARD TEMPERATURA
    # =====================================
    desenhar_card_transparente(
        tela, (50, 110), (480, 320), COR_CARD
    )

    cv2.putText(
        tela,
        "TELEMETRIA DE TEMPERATURA",
        (80, 150),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        COR_TEXTO_MUTED,
        1,
        cv2.LINE_AA
    )

    cv2.putText(
        tela,
        f"{temperatura:.1f}",
        (80, 250),
        cv2.FONT_HERSHEY_SIMPLEX,
        2.8,
        (255, 255, 255),
        5,
        cv2.LINE_AA
    )

    cv2.putText(
        tela,
        "deg C",
        (310, 240),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        cor_status,
        2,
        cv2.LINE_AA
    )

    # =====================================
    # CARD LUMINOSIDADE
    # =====================================
    desenhar_card_transparente(
        tela, (510, 110), (940, 320), COR_CARD
    )

    cv2.putText(
        tela,
        "NIVEL DE LUMINOSIDADE",
        (540, 150),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        COR_TEXTO_MUTED,
        1,
        cv2.LINE_AA
    )

    cv2.putText(
        tela,
        f"{luminosidade:.1f}",
        (540, 250),
        cv2.FONT_HERSHEY_SIMPLEX,
        2.8,
        (255, 255, 255),
        5,
        cv2.LINE_AA
    )

    cv2.putText(
        tela,
        "%",
        (760, 240),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        cor_luz,
        2,
        cv2.LINE_AA
    )

    cv2.putText(
        tela,
        status_luz,
        (760, 285),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        cor_luz,
        2,
        cv2.LINE_AA
    )

    # =====================================
    # CARD STATUS
    # =====================================
    desenhar_card_transparente(
        tela, (970, 110), (1230, 320), COR_CARD
    )

    cv2.putText(
        tela,
        "STATUS",
        (1030, 150),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        COR_TEXTO_MUTED,
        1,
        cv2.LINE_AA
    )

    cv2.circle(
        tela,
        (1090, 220),
        20,
        cor_status,
        -1,
        cv2.LINE_AA
    )

    cv2.circle(
        tela,
        (1090, 220),
        28,
        cor_status,
        2,
        cv2.LINE_AA
    )

    cv2.putText(
        tela,
        status,
        (1020, 280),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        cor_status,
        2,
        cv2.LINE_AA
    )

    # =====================================
    # BARRA TEMPERATURA
    # =====================================
    desenhar_card_transparente(
        tela, (50, 350), (1230, 430), COR_CARD
    )

    cv2.putText(
        tela,
        "TEMPERATURA",
        (80, 390),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        COR_TEXTO_MUTED,
        1,
        cv2.LINE_AA
    )

    cv2.rectangle(
        tela,
        (300, 375),
        (1180, 395),
        (45, 38, 38),
        -1
    )

    pct_temp = np.clip((temperatura - 10) / 25, 0, 1)
    largura_temp = int(pct_temp * (1180 - 300))

    cv2.rectangle(
        tela,
        (300, 375),
        (300 + largura_temp, 395),
        cor_status,
        -1
    )

    # =====================================
    # BARRA LUMINOSIDADE
    # =====================================
    desenhar_card_transparente(
        tela, (50, 450), (1230, 530), COR_CARD
    )

    cv2.putText(
        tela,
        "LUMINOSIDADE",
        (80, 490),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        COR_TEXTO_MUTED,
        1,
        cv2.LINE_AA
    )

    cv2.rectangle(
        tela,
        (300, 475),
        (1180, 495),
        (45, 38, 38),
        -1
    )

    pct_luz = np.clip(luminosidade / 100, 0, 1)
    largura_luz = int(pct_luz * (1180 - 300))

    cv2.rectangle(
        tela,
        (300, 475),
        (300 + largura_luz, 495),
        cor_luz,
        -1
    )

    # =====================================
    # HISTÓRICO
    # =====================================
    desenhar_card_transparente(
        tela, (50, 560), (1230, 690), COR_CARD
    )

    cv2.putText(
        tela,
        "HISTORICO DE TEMPERATURA",
        (80, 595),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        COR_TEXTO_MUTED,
        1,
        cv2.LINE_AA
    )

    origem_x = 80
    origem_y = 660
    altura_grafico = 70
    largura_passo = 18

    if len(historico_temp) > 1:

        pontos = []

        for i, temp in enumerate(historico_temp):

            x = origem_x + (i * largura_passo)

            pct_y = np.clip((temp - 10) / 25, 0, 1)

            y = origem_y - int(pct_y * altura_grafico)

            pontos.append((x, y))

        for i in range(1, len(pontos)):
            cv2.line(
                tela,
                pontos[i - 1],
                pontos[i],
                cor_status,
                2,
                cv2.LINE_AA
            )

    # =====================================
    # ALERTA CRÍTICO
    # =====================================
    if status == "PERIGO CRITICO":

        cv2.rectangle(
            tela,
            (0, 0),
            (WIDTH, HEIGHT),
            (50, 50, 255),
            5
        )

        if int(time.time() * 2) % 2 == 0:

            cv2.putText(
                tela,
                "EVACUAR OU CORRIGIR IMEDIATAMENTE",
                (420, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (50, 50, 255),
                2,
                cv2.LINE_AA
            )

    # =====================================
    # EXIBIÇÃO
    # =====================================
    cv2.imshow("Painel Espacial Inteligente", tela)

    tecla = cv2.waitKey(30)

    if tecla == 27:
        break

cv2.destroyAllWindows()
