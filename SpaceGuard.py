import cv2
import numpy as np
import random
import time

# =====================================
# CONFIGURAÇÕES
# =====================================
WIDTH, HEIGHT = 1280, 720

temperatura = 22.0
luminosidade = 65.0

ultimo_update = time.time()

# =====================================
# PALETA DE CORES
# =====================================
COR_FUNDO = (14, 11, 11)

COR_CARD = (35, 28, 28)

COR_TEXTO_MUTED = (160, 150, 140)

COR_BORDAS = (70, 60, 55)

# =====================================
# FUNÇÃO CARD
# =====================================
def desenhar_card_transparente(
    img,
    pt1,
    pt2,
    cor_bg,
    alpha=0.4
):

    overlay = img.copy()

    cv2.rectangle(
        overlay,
        pt1,
        pt2,
        cor_bg,
        -1
    )

    cv2.addWeighted(
        overlay,
        alpha,
        img,
        1 - alpha,
        0,
        img
    )

    cv2.rectangle(
        img,
        pt1,
        pt2,
        COR_BORDAS,
        1,
        cv2.LINE_AA
    )

# =====================================
# FUNÇÃO GAUGE
# =====================================
def desenhar_gauge(
    img,
    centro,
    raio,
    valor,
    minimo,
    maximo,
    titulo,
    unidade,
    cor
):

    x, y = centro

    # Fundo
    cv2.circle(
        img,
        centro,
        raio,
        (25, 20, 20),
        -1,
        cv2.LINE_AA
    )

    # Glow externo
    cv2.circle(
        img,
        centro,
        raio + 8,
        cor,
        2,
        cv2.LINE_AA
    )

    # Borda
    cv2.circle(
        img,
        centro,
        raio,
        COR_BORDAS,
        2,
        cv2.LINE_AA
    )

    # Arco base
    for angulo in range(-210, 30, 2):

        rad = np.radians(angulo)

        x1 = int(x + (raio - 10) * np.cos(rad))
        y1 = int(y + (raio - 10) * np.sin(rad))

        x2 = int(x + raio * np.cos(rad))
        y2 = int(y + raio * np.sin(rad))

        cv2.line(
            img,
            (x1, y1),
            (x2, y2),
            (55, 45, 45),
            2,
            cv2.LINE_AA
        )

    # Percentual
    pct = np.clip(
        (valor - minimo) / (maximo - minimo),
        0,
        1
    )

    angulo = -210 + (240 * pct)

    # Arco ativo
    for a in range(-210, int(angulo), 2):

        rad = np.radians(a)

        x1 = int(x + (raio - 10) * np.cos(rad))
        y1 = int(y + (raio - 10) * np.sin(rad))

        x2 = int(x + raio * np.cos(rad))
        y2 = int(y + raio * np.sin(rad))

        cv2.line(
            img,
            (x1, y1),
            (x2, y2),
            cor,
            3,
            cv2.LINE_AA
        )

    # Ponteiro
    rad = np.radians(angulo)

    px = int(x + (raio - 25) * np.cos(rad))
    py = int(y + (raio - 25) * np.sin(rad))

    cv2.line(
        img,
        centro,
        (px, py),
        cor,
        4,
        cv2.LINE_AA
    )

    # Centro
    cv2.circle(
        img,
        centro,
        8,
        cor,
        -1,
        cv2.LINE_AA
    )

    # Valor
    cv2.putText(
        img,
        f"{valor:.1f}",
        (x - 45, y + 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.1,
        (255, 255, 255),
        3,
        cv2.LINE_AA
    )

    # Unidade
    cv2.putText(
        img,
        unidade,
        (x - 20, y + 55),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        cor,
        2,
        cv2.LINE_AA
    )

    # Título
    cv2.putText(
        img,
        titulo,
        (x - 70, y - raio - 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        COR_TEXTO_MUTED,
        1,
        cv2.LINE_AA
    )

# =====================================
# LOOP PRINCIPAL
# =====================================
while True:

    # =====================================
    # UPDATE DOS SENSORES
    # =====================================
    if time.time() - ultimo_update > 2:

        temperatura = round(
            random.uniform(10, 35),
            1
        )

        luminosidade = round(
            random.uniform(0, 100),
            1
        )

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
    tela = np.zeros(
        (HEIGHT, WIDTH, 3),
        dtype=np.uint8
    )

    tela[:] = COR_FUNDO

    # =====================================
    # GRID ESPACIAL
    # =====================================
    for x in range(0, WIDTH, 80):

        cv2.line(
            tela,
            (x, 0),
            (x, HEIGHT),
            (22, 18, 18),
            1
        )

    for y in range(0, HEIGHT, 80):

        cv2.line(
            tela,
            (0, y),
            (WIDTH, y),
            (22, 18, 18),
            1
        )

    # =====================================
    # HEADER
    # =====================================
    desenhar_card_transparente(
        tela,
        (0, 0),
        (WIDTH, 70),
        COR_CARD,
        alpha=0.6
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
        (930, 43),
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
        tela,
        (50, 110),
        (480, 320),
        COR_CARD
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
        tela,
        (510, 110),
        (940, 320),
        COR_CARD
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
        tela,
        (970, 110),
        (1230, 320),
        COR_CARD
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
        (1010, 280),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.75,
        cor_status,
        2,
        cv2.LINE_AA
    )

    # =====================================
    # CARD GAUGES
    # =====================================
    desenhar_card_transparente(
        tela,
        (50, 350),
        (1230, 690),
        COR_CARD
    )

    cv2.putText(
        tela,
        "GAUGES DOS SENSORES",
        (80, 390),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        COR_TEXTO_MUTED,
        1,
        cv2.LINE_AA
    )

    # Gauge Temperatura
    desenhar_gauge(
        tela,
        (350, 530),
        110,
        temperatura,
        10,
        35,
        "TEMPERATURA",
        "C",
        cor_status
    )

    # Gauge Luminosidade
    desenhar_gauge(
        tela,
        (930, 530),
        110,
        luminosidade,
        0,
        100,
        "LUMINOSIDADE",
        "%",
        cor_luz
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
                (360, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                (50, 50, 255),
                2,
                cv2.LINE_AA
            )

    # =====================================
    # EXIBIÇÃO
    # =====================================
    cv2.imshow(
        "Painel Espacial Inteligente",
        tela
    )

    tecla = cv2.waitKey(30)

    if tecla == 27:
        break

cv2.destroyAllWindows()
