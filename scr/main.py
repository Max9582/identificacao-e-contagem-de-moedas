import argparse
import cv2
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--entrada", required=True)
parser.add_argument("--saida", required=True)
parser.add_argument("--abertura", type=int, default=2)
parser.add_argument("--fechamento", type=int, default=2)
args = parser.parse_args()

imagem = cv2.imread(args.entrada)
if imagem is None:
    raise FileNotFoundError(f"Erro ao abrir imagem")

cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
cinza_blur = cv2.medianBlur(cinza, 7) 

_, mascara = cv2.threshold(cinza_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

pixels_borda = np.concatenate([
    mascara[0, :], mascara[-1, :], mascara[:, 0], mascara[:, -1]
])
if np.mean(pixels_borda) > 127:
    mascara = cv2.bitwise_not(mascara)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
mascara = cv2.morphologyEx(mascara, cv2.MORPH_CLOSE, kernel, iterations=args.fechamento)
mascara = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel, iterations=args.abertura)
mascara_com_borda = cv2.copyMakeBorder(mascara, 1, 1, 1, 1, cv2.BORDER_CONSTANT, value=0)

altura_b, largura_b = mascara_com_borda.shape
mascara_flood = np.zeros((altura_b + 2, largura_b + 2), np.uint8)
cv2.floodFill(mascara_com_borda, mascara_flood, (0, 0), 255)

mascara_auxiliar = mascara_com_borda[1:-1, 1:-1]

buracos = cv2.bitwise_not(mascara_auxiliar)
mascara = cv2.bitwise_or(mascara, buracos)

if not cv2.imwrite(args.saida, mascara):
    raise OSError(f"Erro ao salvar imagem")

print(f"Imagem salva: {args.saida}")
