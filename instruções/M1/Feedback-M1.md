# Devolutiva da M1 — Grupo 12

## Identificação da análise

- Projeto: identificação e contagem de moedas brasileiras
- Repositório: <https://github.com/Max9582/identificacao-e-contagem-de-moedas>
- Commit avaliado: `3edfa7e9f96a3d94253ed8f5f67727b6ed36a996`
- Vídeo: acessível; duração aproximada de 10min41s; conteúdo pendente de conferência docente

## Síntese

O problema é claro, há dez fotografias próprias variadas e o pipeline diferencia segmentação, recorte, classificação e soma. A viabilidade, porém, ainda é sustentada por exemplos externos; não há experimento executado no repositório. A restrição “face coroa para cima” é útil, mas o fundo “razoavelmente neutro” precisa virar condição objetiva.

## Avaliação pela rubrica

| Critério | Nível | Pontos | Evidência e justificativa |
|---|---|---:|---|
| 1. Problema | Adequado | 11,25/15 | Saída e moedas do Real estão definidas; oclusão e disposição ainda ampliam o escopo. |
| 2. Imagens e dados | Excelente | 10,00/10 | Dataset documentado e dez fotos próprias com variação de fundo/disposição. |
| 3. Objetivos e sucesso | Adequado | 7,50/10 | Critérios existem, mas “segmentação precisa” não está quantificada. |
| 4. Pipeline | Adequado | 11,25/15 | Cada etapa tem finalidade, técnica, entrada, saída e dúvida. |
| 5. Viabilidade | Parcial | 7,50/15 | Literatura e projetos externos indicam plausibilidade; falta evidência própria. |
| 6. Repositório | Adequado | 7,50/10 | Estrutura e licença presentes; ainda sem ambiente/código/reprodução. |
| 7. Markdown | Adequado | 7,50/10 | Documentação completa, com problemas de revisão textual e algumas imprecisões técnicas. |
| 8. Vídeo | Pendente | 10/10 | Acesso e duração confirmados; conteúdo e participação requerem conferência. |
| 9. Histórico | Adequado | 5,00/5 | Muitos commits e autores, embora excessivamente fragmentados e concentrados. |

**Subtotal verificável:** 66,25/90.  
**Após o vídeo:** 77,50 pontos.

## Direcionamentos para a M2

1. Implementar e medir a segmentação antes de treinar a CNN.
2. Criar máscaras/contagens verdadeiras para as dez imagens próprias.
3. Separar métricas: moedas detectadas, denominação classificada e valor total.
4. Tratar moedas encostadas com transformada de distância/watershed ou retirar esse caso do escopo inicial.
5. Confirmar se as anotações COCO e classes do dataset correspondem exatamente ao objetivo e evitar vazamento entre imagens derivadas.

## Prioridade imediata

Construir uma baseline geométrica nas dez imagens próprias e produzir uma tabela por imagem com quantidade real, quantidade detectada e erros de separação.
