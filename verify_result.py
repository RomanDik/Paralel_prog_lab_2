import numpy as np

def read_matrix_from_file(filename):
    with open(filename, 'r') as file:
        size = tuple(map(int, file.readline().split()))
        matrix = [list(map(float, line.split())) for line in file]
    return np.array(matrix)

def compare_matrices(mat1, mat2, tol=1e-6):
    return np.allclose(mat1, mat2, atol=tol)

def main(mat1_filename, mat2_filename, result_filename, output_filename="check_result.txt"):
    mat1 = read_matrix_from_file(mat1_filename)
    mat2 = read_matrix_from_file(mat2_filename)
    result = read_matrix_from_file(result_filename)

    np_result = np.matmul(mat1, mat2)

    with open(output_filename, 'a') as f:
        if compare_matrices(result, np_result):
            f.write("true\n")
            print("true")
        else:
            f.write("false\n")
            print("false")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 5:
        print("Usage: python verify_result.py mat1.txt mat2.txt result.txt output.txt")
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])