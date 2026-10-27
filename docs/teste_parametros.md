# Registro de Parâmetros dos testes

## Execução do código

``` bash
# segmentação utilizando morfologia para a geração da máscara binária
python src/main.py --entrada <input-relative-path> --saida <output-relative-path> --abertura <int> --fechamento <int>

# identificação de objetos na imagem
python src/identifica.py --entrada <input-relative-path> --saida <output-relative-path>
```

## Teste com a máscara binária

| Entrada | Parâmetros | Saída |
| --- | --- | --- |
| ![diversas_espalhadas_papel.jpg](../images/input/diversas_espalhadas_papel.jpg) | `--abertura 1 --fechamento 13` | ![diversas_espalhadas_papel_teste.png](../images/results/diversas_espalhadas_papel_teste.png) |
| ![diversas_espalhadas_papel2.jpg](../images/input/diversas_espalhadas_papel2.jpg) | `--abertura 1 --fechamento 3` | ![diversas_espalhadas_papel2_teste.png](../images/results/diversas_espalhadas_papel2_teste.png) |
| ![diversas_fundoTexturizado.jpg](../images/input/diversas_fundoTexturizado.jpg) | `--abertura 10 --fechamento 1` | ![diversas_fundoTexturizado_teste.png](../images/results/diversas_fundoTexturizado_teste.png) |
| ![diversas_fundoTexturizadoFlash.jpg](../images/input/diversas_fundoTexturizadoFlash.jpg) | `--abertura 5 --fechamento 0` | ![diversas_fundoTexturizadoFlash_teste.png](../images/results/diversas_fundoTexturizadoFlash_teste.png) |
| ![diversas_porCima_papeljpg.jpg](../images/input/diversas_porCima_papeljpg.jpg) | `--abertura 0 --fechamento 4` | ![diversas_porCima_papel_teste.png](../images/results/diversas_porCima_papel_teste.png) |
| ![poucas_bemPerto_papel.jpg](../images/input/poucas_bemPerto_papel.jpg) | `--abertura 0 --fechamento 4` | ![poucas_bemPerto_papel_teste.png](../images/results/poucas_bemPerto_papel_teste.png) |
| ![poucas_fundoTexturizado.jpg](../images/input/poucas_fundoTexturizado.jpg) | `--abertura 4 --fechamento 0` | ![poucas_fundoTexturizado_teste.png](../images/results/poucas_fundoTexturizado_teste.png) |
| ![poucas_perto_fundoTexturizado](../images/input/poucas_perto_fundoTexturizado.jpg) | `--abertura 4 --fechamento 0` | ![poucas_perto_fundoTexturizado_teste.png](../images/results/poucas_perto_fundoTexturizado_teste.png) |
| ![poucas_perto_papel.jpg](../images/input/poucas_perto_papel.jpg) | `--abertura 1 --fechamento 4` | ![poucas_perto_papel_teste.png](../images/results/poucas_perto_papel_teste.png) |
| ![real_papel.jpg](../images/input/real_papel.jpg) | `--abertura 6 --fechamento 0` | ![real_papel_teste.png](../images/results/real_papel_teste.png) |

## Teste na identificação de objetos

| Entrada | Parâmetros | Saída |
| --- | --- | --- |
| ![diversas_espalhadas_papel.jpg](../images/input/diversas_espalhadas_papel.jpg) | ... | ![diversas_espalhadas_papel_identificacao.png](../images/results/diversas_espalhadas_papel_identificacao.png) |
| ![diversas_espalhadas_papel2.jpg](../images/input/diversas_espalhadas_papel2.jpg) | ... | ![diversas_espalhadas_papel2_identificacao.png](../images/results/diversas_espalhadas_papel2_identificacao.png) |
| ![diversas_fundoTexturizado.jpg](../images/input/diversas_fundoTexturizado.jpg) | ... | ![diversas_fundoTexturizado_identificacao.png](../images/results/diversas_fundoTexturizado_identificacao.png) |
| ![diversas_fundoTexturizadoFlash.jpg](../images/input/diversas_fundoTexturizadoFlash.jpg) | ... | ![diversas_fundoTexturizadoFlash_identificacao.png](../images/results/diversas_fundoTexturizadoFlash_identificacao.png) |
| ![diversas_porCima_papeljpg.jpg](../images/input/diversas_porCima_papeljpg.jpg) | ... | ![diversas_porCima_papeljpg_identificacao.png](../images/results/diversas_porCima_papeljpg_identificacao.png) |
| ![poucas_bemPerto_papel.jpg](../images/input/poucas_bemPerto_papel.jpg) | ... | ![poucas_bemPerto_papel_identificacao.png](../images/results/poucas_bemPerto_papel_identificacao.png) |
| ![poucas_fundoTexturizado.jpg](../images/input/poucas_fundoTexturizado.jpg) | ... | ![poucas_fundoTexturizado_identificacao.png](../images/results/poucas_fundoTexturizado_identificacao.png) |
| ![poucas_perto_fundoTexturizado](../images/input/poucas_perto_fundoTexturizado.jpg) | ... | ![poucas_perto_fundoTexturizado_identificacao.png](../images/results/poucas_perto_fundoTexturizado_identificacao.png) |
| ![poucas_perto_papel.jpg](../images/input/poucas_perto_papel.jpg) | ... | ![poucas_perto_papel_identificacao.png](../images/results/poucas_perto_papel_identificacao.png) |
| ![real_papel.jpg](../images/input/real_papel.jpg) | ... | ![real_papel_identificacao.png](../images/results/real_papel_identificacao.png) |
