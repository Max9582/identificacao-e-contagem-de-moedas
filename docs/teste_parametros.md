# Registro de Parâmetros dos testes

## Execução do código

``` bash
python scr/main.py --entrada <input-relative-path> --saida <output-relative-path> --abertura <int> --fechamento <int>

python scr/identifica.py --entrada <input-relative-path> --saida <output-relative-path>
```

## Teste com a máscara binária

| Entrada | Parâmetros | Saída |
| --- | --- | --- |
| ![[images/input/diversas_espalhadas_papel.jpg]] | `--abertura 1 --fechamento 13` | ![[images/results/diversas_espalhadas_papel_teste.png]] |
| ![[images/input/diversas_espalhadas_papel2.jpg]] | `--abertura 1 --fechamento 3` | ![[images/results/diversas_espalhadas_papel2_teste.png]] |
| ![[images/input/diversas_fundoTexturizado.jpg]] | `--abertura 10 --fechamento 1` | ![[images/results/diversas_fundoTexturizado_teste.png]] |
| ![[images/input/diversas_fundoTexturizadoFlash.jpg]] | `--abertura 5 --fechamento 0` | ![[images/results/diversas_fundoTexturizadoFlash_teste.png]] |
| ![[images/input/diversas_porCima_papeljpg.jpg]] | `--abertura 0 --fechamento 4` | ![[images/results/diversas_porCima_papel_teste.png]] |
| ![[images/input/poucas_bemPerto_papel.jpg]] | `--abertura 0 --fechamento 4` | ![[images/results/poucas_bemPerto_papel_teste.png]] |
| ![[images/input/poucas_fundoTexturizado.jpg]] | `--abertura 4 --fechamento 0` | ![[images/results/poucas_fundoTexturizado_teste.png]] |
| ![[images/input/poucas_perto_fundoTexturizado.jpg]] | `--abertura 4 --fechamento 0` | ![[images/results/poucas_perto_fundoTexturizado_teste.png]] |
| ![[images/input/poucas_perto_papel.jpg]] | `--abertura 1 --fechamento 4` | ![[images/results/poucas_perto_papel_teste.png]] |
| ![[images/input/real_papel.jpg]] | `--abertura 6 --fechamento 0` | ![[images/results/real_papel_teste.png]] |
