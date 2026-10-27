
import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument("--entrada", required=True)
parser.add_argument("--saida", required=True)

args = parser.parse_args()

imagem = cv2.imread(args.entrada)

if imagem is None:
    raise FileNotFoundError(f"Erro ao abrir imagem em: {args.entrada}")

cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
cinza = cv2.GaussianBlur(cinza, (9, 9), 2)

circulos = cv2.HoughCircles(
    cinza,
    cv2.HOUGH_GRADIENT,
    dp=1.2,
    minDist=30,
    param1=100,
    param2=35,
    minRadius=15,
    maxRadius=100
)


if circulos is not None:
    circulos = circulos[0].round().astype(int)

    for x, y, raio in circulos:
        cv2.circle(imagem, (x, y), raio, (0, 255, 0), 2)
        cv2.circle(imagem, (x, y), 3, (0, 0, 255), -1)

if not cv2.imwrite(args.saida, imagem):
    raise OSError(f"Erro ao salvar imagem em: {args.saida}")

print(f"Imagem salva em: {args.saida}")

