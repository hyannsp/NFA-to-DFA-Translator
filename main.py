# Função para converter a tabela em uma tabela DFA
def get_next_lambda(node, nfa_table):
    return [line[2] for line in nfa_table[2:] if line[0] == node and line[1] == 'h']

def get_line(node, nfa_table,rec=False):
    dfa_line = [[],[],[]]
    if node in nfa_table[2]:
        dfa_line[0] = node
        return dfa_line
    final_node = [node]

    results = [line for line in nfa_table[2:] if line[0] == node]
    print("results: ",results)
    for result_line in results:
        print("result line:", result_line)
        print("result line[1]:", result_line[1])

        match result_line[1]:
            case '0':
                print(f"Result Line = 0")
                dfa_line[1].append(result_line[2])
                dfa_line[1] += get_next_lambda(result_line[2],nfa_table)
            case '1':
                print(f"Result Line = 1")
                dfa_line[2].append(result_line[2]) 
                dfa_line[2] += get_next_lambda(result_line[2],nfa_table)
            case 'h':
                if rec:
                    pass # Caso seja uma recursão, não faça nada
                else:
                    print("Entrando na recursão:",result_line[2])
                    rec_result = get_line(result_line[2],nfa_table,True)
                    # Concatena o resultado da recursão com a linha atual
                    dfa_line[1] += rec_result[1]
                    dfa_line[2] += rec_result[2]
                    # Adiciona o nó final retornado da recursão
                    final_node += rec_result[0]
        
    dfa_line[0] = final_node
    return dfa_line

def convert_to_dfa(nfa_table):
    dfa = []
    dfa_line = []
    # Selecionar qual inicia e qual finaliza
    all_nodes = nfa_table[0]
    first_node = nfa_table[1][0]
    final_nodes = nfa_table[2] # Pode ter mais de 1
    
    
    return dfa

# Ler o caminho do arquivo
path = input("Ïnsira o caminho do arquivo de texto desejado: ")
text_matrix = []

# Ler e transformar o arquivo de texto em uma matriz
with open(path,'r') as file:
    for linha in file:
        text_matrix.append(linha.strip().split(" "))

print(text_matrix)
teste = get_line('b', text_matrix)
print(teste)
#dfa = convert_to_dfa(text_matrix)