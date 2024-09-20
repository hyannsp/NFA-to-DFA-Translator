import os

def save_matrix_to_txt(matrix, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    with open(file_path, 'w') as file:
        for row in matrix:
            line = ' '.join(map(str, row))
            file.write(line + '\n')

