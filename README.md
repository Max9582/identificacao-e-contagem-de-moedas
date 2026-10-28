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

**Estágio Atual:** M2: há um protótipo de segmentação por limiarização e morfologia, além de uma baseline de detecção de círculos. A avaliação da segmentação ainda é preliminar: as máscaras de referência cobrem quatro das dez imagens e o IoU médio ainda não atingiu a meta definida. Na M3, vamos completar as máscaras e aprimorar e reavaliar o método. A classificação das moedas e o cálculo automático do valor total também serám realizados na M3.

---

## Organização do Repositório

```text
identificacao-e-contagem-de-moedas/
├── README.md               # Este arquivo
├── docs/
│   ├── relatorio_m2.md     # Relatório da M2
│   └── proposta.md         # Documento detalhado da proposta M1
├── images/
│   ├── input/              # Imagens de input
│   ├── results/            # Imagens de output
│   └── segmentacaoManual/  # Máscaras de referência
├── src/                    # Implementação do código em Python
├── requirements.txt        # Dependências do protótipo
├── LICENSE                 # GNU General Public License v3.0
└── .gitignore
```

## Tecnologias
* **Linguagem:** Python
* **Protótipo atual:** OpenCV para segmentação e detecção de círculos.
* **Planejado:** TensorFlow para classificação das moedas na M3.

## Instalação e execução

Na raiz do repositório, instale as dependências:

```bash
python -m pip install -r requirements.txt
```

Exemplo de segmentação; a máscara será salva em `images/results/exemplo.png`:

```bash
python src/main.py --entrada images/input/diversas_fundoTexturizado.jpg --saida images/results/exemplo.png --abertura 2 --fechamento 2
```

Exemplo de detecção de círculos; a imagem marcada será salva no caminho indicado:

```bash
python src/identifica.py --entrada images/input/diversas_fundoTexturizado.jpg --saida images/results/diversas_fundoTexturizado_identificacao.png
```

## Instruções dos experimentos realizados

- **Testes de segmentação com o uso da morfologia, para geração de máscaras binárias**

``` Bash
python src/main.py --entrada images/input/<imagem>.jpg --saida images/results/<saida>.png --abertura <int> --fechamento <int>
```

- **Testes de identificação das moedas**

``` Bash
python src/identifica.py --entrada <input-relative-path> --saida <output-relative-path>
```

## Vídeos de apresentação
* M1: <https://youtu.be/GODjVWywVVA>
* M2: Link aqui

## Documentação adicional 
- Proposta do Projeto, disponível na pasta `/docs`
- Relatório da M2, disponível em `/docs/relatorio_m2.md`
- Documentação detalhada dos parâmetros utilizados nos experimentos, disponível em `/docs/teste_parametros.md`
- Referências manuais das imagens de input em `/images/input/README.md`
