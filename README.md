# Objetivo do Projeto

Parte 1: Converter um AFND (com movimentos vazios) em um AFD.
Alfabeto: {0,1}

Entrada: um arquivo com a tabela do AFND.

Formato do arquivo de entrada:
Linha 0: a sequência de estados separados por espaço. EX: A B C D E F
Linha 1: estado inicial
Linha 2: estados finais separados por espaço ( se houver mais de um estado final)
Linha 3 em diante: estado atual, espaço, caractere lido, espaço, próximo estado
Obs: respresentar a transição vazia por h.

Saída: um arquivo com a tabela do AFD

Formato do arquivo de saída: o mesmo do arquivo de entrada.
Usar o GraphViz para fazer a exibição do grafo do AFND e do AFD.
Usar o JFLAP e desenhar os dois autômatos: o de entrada e o de saída.

Parte 2: Dado um conjunto de palavras, determinar se a palavra é reconhecida ou não pelo
AFD equivalente gerado na parte 1.
Alfabeto: {0,1}
Entrada: um arquivo com as palavras a serem reconhecidas
Uma palavra por linha.
Saída: um arquivo com todas as palavras e na frente de cada palavra por aceito ou não aceito
(reconhecido ou não reconhecido). Por uma palavra por linha.
Ex: 
  Na linha 1: qwefr aceito
  Na linha 2: abder não aceito