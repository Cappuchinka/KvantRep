def sum_matrix(matr1, matr2):
    for i in range(len(matr1)):
        for j in range(len(matr1[i])):
            matr1[i][j] += matr2[i][j]
    return matr1

if __name__ == '__main__':
    _matr1 = [[1, 2],
              [3, 4]]

    _matr2 = [[5, 6],
              [7, 8]]

    print(sum_matrix(_matr1, _matr2))