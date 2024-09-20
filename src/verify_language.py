def verify_word(dfa_matrix, word):
    node = dfa_matrix[1][0] # Estado inicial
    final_nodes = dfa_matrix[2] # Estados Finais

    # Para cada item da palavra, verifica-se a transição
    print(word)
    for item in word:
        transitions = False
        for line in dfa_matrix[3:]: # Verifica as linhas de transiÇão da matriz
            if line[0] == node and line[1] == item:
                node = line[2] # Troca o node para o novo estado
                transitions = True
                break
    
        # Caso não encontre nenhuma transição com o estado e item, o DFA deve parar.
        if not transitions:
            print(f"Não existe Transição de {node} com {item}")
            return False

    return node in final_nodes # Retorna true caso exista algum estado no estado final

def verify_language(dfa_matrix, text_matrix):
    new_text = []

    # Verificar se cada palavra é aceita
    for word in text_matrix:
        if verify_word(dfa_matrix, word[0]):
            new_text.append([word[0], "- Aceito"])
        else:
            new_text.append([word[0], "- Não Aceito"])
    
    return new_text