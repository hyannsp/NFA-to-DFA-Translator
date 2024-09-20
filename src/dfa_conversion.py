import string

def get_dictionary(dfa_table):
    # Criar um alfabeto com letras
    alphabet = string.ascii_lowercase
    unique_nodes = []
    for line in dfa_table:
        node = tuple(line[0]) # Deve ser colocado em tupla
        if node not in unique_nodes:
            unique_nodes.append(node)
    # Cria um dicionário para cada node a, b, c...
    nodes_dict = {node: alphabet[i] for i, node in enumerate(unique_nodes)}
    return nodes_dict

def translate_matrix(matrix, nodes_dict):
    translated_matrix = []
    # Itera sobre cada linha da matriz
    for row in matrix:
        translated_row = []
        # Itera sobre cada item na linha
        for item in row:
            if isinstance(item, list):
                # Procura uma tradução para a lista
                translation = next((value for key, value in nodes_dict.items() if list(key) == item), item)
                translated_row.append(translation)
            else: # Adiciona o item não traduzido (caso seja um caractere)
                translated_row.append(item)
        # Adiciona a linha traduzida à matriz traduzida
        translated_matrix.append(translated_row)
    return translated_matrix

def format_to_txt(dfa_table, final_nodes_nfa):
    new_text_matrix = []

    # Um dicionário representado cada node como uma letra do alfabeto: { ('a', 'b', 'c') : a } 
    nodes_dict = get_dictionary(dfa_table)
    print(nodes_dict)

    # Linha 0: Todos os nodes (já como alfabeto)
    all_nodes = list(nodes_dict.keys())
    all_nodes = [list(item) for item in all_nodes]
    new_text_matrix.append(all_nodes)

    # Linha 1: Node que inicializa o automato
    initial_node = [dfa_table[0][0]]
    new_text_matrix.append(initial_node)

    # Linha 2: Nodes que finalizam o automato (Se o nfa é finalizado em 'f', qualquer um que contenha 'f' pode ser um finalizador)
    final_nodes = []
    for line in all_nodes:
        for node in line:
            if node in final_nodes_nfa:
                final_nodes.append(line)
    new_text_matrix.append(final_nodes)

    # Linha 3+: Os nodes e seus caminhos dependendo do alfabeto 
    for line in dfa_table:
        if line[1] != []:
            new_text_matrix.append([line[0], '0', line[1]])
        if line[2] != []:
            new_text_matrix.append([line[0], '1', line[2]])

    # Traduzir matriz utilizando alfabeto
    translated_matrix = translate_matrix(new_text_matrix, nodes_dict)
    print("Matriz traduzida:")
    for row in translated_matrix:
        print(row)
    
    return translated_matrix

# pegar os nodes conectados por lambda ('h')
def get_next_lambda(node, nfa_table):
    return [line[2] for line in nfa_table[2:] if len(line) >= 3 and line[0] == node and line[1] == 'h'] or []

# Retorna a conversão de um node para uma linha
def get_line(nodes, nfa_table, rec=False):
    dfa_line = [[], [], []] # Inicializar as três colunas (para 0, 1 e o estado final)
    final_node = list(nodes) # Garante que 'node' é uma lista

    # Filtrar as linhas da NFA que correspondem ao node atual
    results = [line for line in nfa_table[3:] if len(line) >= 3 and line[0] in nodes]

    for result_line in results:
        match result_line[1]:
            case '0':  # Adicionar à coluna de transições '0'
                dfa_line[1].append(result_line[2]) 
                dfa_line[1] += get_next_lambda(result_line[2], nfa_table)
            case '1': # Adicionar à coluna de transições '1'
                dfa_line[2].append(result_line[2])
                dfa_line[2] += get_next_lambda(result_line[2], nfa_table)
            case 'h': # Recursão para lidar com lambda ('h')
                if rec:
                    continue
                else:
                    rec_result = get_line([result_line[2]], nfa_table, True)
                    # Concatenar o resultado da recursão com a linha atual
                    dfa_line[1] += rec_result[1]
                    dfa_line[2] += rec_result[2]
                    final_node += rec_result[0]

    # Remover duplicatas e ordenar as listas
    dfa_line[0] = sorted(set(final_node))
    dfa_line[1] = sorted(set(dfa_line[1]))
    dfa_line[2] = sorted(set(dfa_line[2]))

    return dfa_line

def get_dfa_conversion_table(nfa_table):
    dfa = []
    nodes_to_convert = []
    nodes_already_converted = []
    
    # Obter os nós iniciais (com possíveis lambdas)
    initial_nodes = get_next_lambda(nfa_table[1][0], nfa_table)
    initial_nodes.append(nfa_table[1][0])# Adicionar o node inicial à lista

    # Converter a primeira linha (nó inicial)
    first_line = get_line(initial_nodes, nfa_table)
    dfa.append(first_line)

    # Marcar o nó inicial como convertido
    nodes_already_converted.append(first_line[0])

    # Adicionar nós das transições (coluna 1 e 2) para conversão, se ainda não foram convertidos
    if first_line[1] and first_line[1] not in nodes_already_converted:
        nodes_to_convert.append(first_line[1])
    if first_line[2] and first_line[2] not in nodes_already_converted:
        nodes_to_convert.append(first_line[2])

    # Processar todos os nós a serem convertidos
    while nodes_to_convert:
        nodes = nodes_to_convert.pop(0)
        if nodes in nodes_already_converted:
            continue # Se o nó já foi convertido, ignorar
        
        # Converter a linha do nó atual
        temp_line = get_line(nodes, nfa_table)
        dfa.append(temp_line)

        # Marcar o nó atual como convertido
        nodes_already_converted.append(temp_line[0])

        # Adicionar nós das transições (colunas 1 e 2) para conversão
        if temp_line[1] and temp_line[1] not in nodes_already_converted:
            nodes_to_convert.append(temp_line[1])
        if temp_line[2] and temp_line[2] not in nodes_already_converted:
            nodes_to_convert.append(temp_line[2])
    
    return dfa
