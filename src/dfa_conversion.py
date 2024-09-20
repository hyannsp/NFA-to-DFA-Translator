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

# Função para capturar todos os estados acessíveis por transição lambda
def get_all_lambda_states(nodes, nfa_table, visited=None):
    if visited is None:
        visited = set()

    lambda_states = set(nodes)

    # Processar cada nó
    for node in nodes:
        # Achar todas as transições lambda do nó atual
        lambda_transitions = [line[2] for line in nfa_table[3:] if line[0] == node and line[1] == 'h']
        for next_state in lambda_transitions:
            if next_state not in visited:
                visited.add(next_state)
                # Adiciona todos os estados acesiveis por lambda de forma recursiva
                lambda_states.update(get_all_lambda_states([next_state], nfa_table, visited))

    return lambda_states


# Função para converter um node para uma linha no DFA
def get_line(nodes, nfa_table):
    dfa_line = [[], [], []]  # Inicializar as três colunas (para 0, 1 e os estados finais)
    final_node = set(nodes)  # Conjunto para armazenar todos os nós alcançados por lambda

    # Obter todos os estados alcançáveis por transições lambda
    lambda_closure = get_all_lambda_states(nodes, nfa_table)
    final_node.update(lambda_closure)

    # Processar as transições para 0 e 1
    for node in final_node:
        results = [line for line in nfa_table[3:] if line[0] == node]

        for result_line in results:
            match result_line[1]:
                case '0':  # Processar transição para '0'
                    dfa_line[1].append(result_line[2])
                    dfa_line[1].extend(get_all_lambda_states([result_line[2]], nfa_table))  # Incluir lambda após '0'
                case '1':  # Processar transição para '1'
                    dfa_line[2].append(result_line[2])
                    dfa_line[2].extend(get_all_lambda_states([result_line[2]], nfa_table))  # Incluir lambda após '1'

    # Remover duplicatas e ordenar as listas
    dfa_line[0] = sorted(final_node)  # Todos os nós alcançados pela recursão lambda
    dfa_line[1] = sorted(set(dfa_line[1]))  # Transições de 0
    dfa_line[2] = sorted(set(dfa_line[2]))  # Transições de 1

    return dfa_line

def get_dfa_conversion_table(nfa_table):
    dfa = []
    nodes_to_convert = []
    nodes_already_converted = []
    
    # Obter os nós iniciais (com possíveis lambdas)
    initial_nodes = list(get_all_lambda_states(nfa_table[1][0], nfa_table))
    initial_nodes.append(nfa_table[1][0])# Adicionar o node inicial à lista

    # Converter a primeira linha (nó inicial)
    first_line = get_line(initial_nodes, nfa_table)
    dfa.append(first_line)

    # Marcar o nó inicial como convertido
    nodes_already_converted.append(first_line[0])

    print("Primeira Linha: ",first_line)
    # Adicionar nós das transições (coluna 1 e 2) para conversão, se ainda não foram convertidos
    if first_line[1] and first_line[1] not in nodes_already_converted:
        nodes_to_convert.append(first_line[1])
    if first_line[2] and first_line[2] not in nodes_already_converted:
        nodes_to_convert.append(first_line[2])

    # Processar todos os nós a serem convertidos
    print("Nodes para Converter: ", nodes_to_convert)
    print("Nodes Ja convertidos: ", nodes_already_converted)
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
