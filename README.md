# Identificação e Contagem de Moedas

**Disciplina:** Processamento de Imagens

**Professor:** Marcelo Lopes

## Integrantes
- Gabriel Maximiano dos Santos
- Diego Augusto Carvalho
- Seiki Takao Iizuka

---

## Resumo do Projeto

### Problema investigado
&emsp; A identificação e contagem manual de moedas em estabelecimentos comerciais, trocos ou por quaisquer outros motivos pode se tornar um atividade repetitiva e maçante, ainda mais quando estamos lidando com um grande volumes de moedas e não temos a nossa disposição um contator digital.

### Contexto de Aplicação
&emsp; Essa solução é destinada principalmente a pequenos comerciantes, mas também pode ser utilizada em casa, caso seja necessário contar uma grande quantidade de moedas.

### Objetivo Geral
&emsp; Desenvolver um sistema computacional capaz de segmentar, identificar o valor nominal e contabilizar moedas em imagens digitais, informando o somatório dos valores.

### Visão da Solução Proposta
&emsp; Inicialmente, a imagem passará por um pré-processamento utilizando a biblioteca OpenCV. Em seguida, um modelo de detecção e classificação desenvolvido com o TensorFlow será responsável por classificar o valor nominal de cada moeda. Por fim, o sistema realizará o somatório dos valores, retornando o montante final.

---

## Conjunto de Imagens

### 1. Imagens para Treinamento
* **Origem:** [Brazilian Coins - Kaggle](https://www.kaggle.com/datasets/lgmoneda/br-coins/data)
* **Licença:** *CC BY-NC-SA 4.0*.
* **Quantidade:** 28.2 mil imagens no formato *.jpg*.
* **Características:** Contém fotos de moedas do Real, divididas em imagens de moedas únicas e múltiplas moedas, com iluminações diferentes no ambiente, com fundo branco, com e sem o [COCO format](https://cocodataset.org/#home).

### 2. Imagens para Teste
* **Origem:** Fotos autorais capturadas pelos integrantes do grupo, disponíveis na pasta `/images/input`.
* **Quantidade:** 10 imagens.
* **Variabilidade:** As fotos foram tiradas variando:
  * **Fundo:** Superfícies lisas e texturizadas.
  * **Disposição:** Moedas em conjunto, isoladas, próximas e separadas.

---

## Estágio Atual

**Estágio Atual:** M1 concluída. Definimos o problema, conjunto de imagens, pipeline e estudo de viabilidade. O próximo passo é começar o desenvolvimento do código de acordo com o que foi planejado na proposta.

---

## Organização do Repositório

```text
identificacao-e-contagem-de-moedas/
├── README.md               # Este arquivo
├── docs/
│   └── proposta.md         # Documento detalhado da proposta M1
├── images/
│   ├── input/              # Imagens de input
│   └── results/            # Imagens de output
├── LICENSE                 # GNU General Public License v3.0
└── .gitignore
```

---

## Tecnologias previstas
* **Linguagem:** Python
* **Bibliotecas Principais:** OpenCV e TensorFlow

## Vídeo de apresentação
Link do vídeo: <https://youtu.be/GODjVWywVVA>

## Documentação adicional 
- Proposta do Projeto, disponível na pasta `/docs`
