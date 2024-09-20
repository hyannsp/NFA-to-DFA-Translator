from dfa_conversion import get_dfa_conversion_table, format_to_txt
from file_handling import save_matrix_to_txt
from verify_language import verify_language

# Função para ler o arquivo e transformar em uma matriz
def capture_matrix(type):
    path = input(f"Insira o caminho do arquivo de texto contendo o {type}: ")
    text_matrix = []

    try:
        # Ler e transformar o arquivo de texto em uma matriz com tratamento de erros
        with open(path, 'r') as file:
            for linha in file:
                text_matrix.append(linha.strip().split(" "))
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado no caminho especificado: {path}")
        return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        return None

    return text_matrix

# Função para salvar o arquivo
def save_file(type, matrix):
    name = input("Insira o nome do arquivo txt que será retornado: ")
    file_path = f"./output/{type}/{name}.txt"
    save_matrix_to_txt(matrix, file_path)
    print(f"Seu arquivo foi salvo em: {file_path}")
    return

def main():
    select = ''

    while select != '0':
        print("Conversor de NFA para DFA\nInsira o que deseja fazer: \n1-Converter Autômato Finito não Deterministico\n2-Verificar se as Palavras são aceitas por um DFA\n0-Fechar")
        select = input("")
        match select:

            case '0': # Sair do aplicativo
                pass

            case '1': # Ler arquivo NFA e transformar em DFA
                # Ler o caminho do arquivo
                text_matrix = capture_matrix("NFA")
                if text_matrix is None:  # Verifica se ocorreu algum erro
                    print("Operação cancelada devido a erro na leitura do arquivo.")
                    continue  # Volta ao início do loop principal
                print("Matriz lida do arquivo:", text_matrix)

                # Converter para DFA
                dfa_conversion_table = get_dfa_conversion_table(text_matrix)
                print("Resultado da conversão para DFA:", dfa_conversion_table)

                # Transformar em uma array parecida com o txt de entrada
                new_text_matrix = format_to_txt(dfa_conversion_table, text_matrix[2])

                save_file('dfa',new_text_matrix)

            case '2': # Verificar se a Linguagem entre um NFA e um DFA são  mesma.
                # Ler caminho do DFA
                dfa_matrix = capture_matrix("DFA")
                if dfa_matrix is None:
                    print("Operação cancelada devido a erro na leitura do DFA.")
                    continue
                
                # Ler caminho das palavras
                text_matrix = capture_matrix("conjunto de palavras")
                if dfa_matrix is None:
                    print("Operação cancelada devido a erro na leitura do conjuntop de palavras.")
                    continue

                # Função que retorna o arquivo contendo as palavras e se foram aceitas ou não

                new_text_matrix = verify_language(dfa_matrix, text_matrix)
                save_file('words',new_text_matrix)
                

            case _:
                print("Opção inválida!")
                pass
    # App encerrado
    print("Aplicação Encerrada!")

if __name__ == "__main__":
    main()