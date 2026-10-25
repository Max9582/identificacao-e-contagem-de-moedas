import argparse
import cv2

parser = argparse.ArgumentParser()

parser.add_argument("--entrada", required=True)
parser.add_argument("--saida", required=True)
parser.add_argument("--abertura", type=int, default=1)
parser.add_argument("--fechamento", type=int, default=1)

args = parser.parse_args()

imagem = cv2.imread(args.entrada, cv2.IMREAD_GRAYSCALE)

if imagem is None:
    raise FileNotFoundError(f"imagem não encontrada")

_, mascara = cv2.threshold(
    imagem, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

mascara = cv2.morphologyEx(
    mascara, cv2.MORPH_OPEN, kernel, iterations=args.abertura
)

mascara = cv2.morphologyEx(
    mascara, cv2.MORPH_CLOSE, kernel, iterations=args.fechamento
)

if not cv2.imwrite(args.saida, mascara):
    raise OSError(f"Caminho de output não encontrado")
