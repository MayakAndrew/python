class Matrix:
    def __init__(self, list_1, list_2):
        self.matr_sum = [list_1, list_2]
        self.list_1 = list_1
        self.list_2 = list_2

    def __str__(self):
        return str('\n'.join(['\n'.join([str(i) for i in j]) for j in self.matr_sum]))

    def __add__(self):
        matr_sum = [[0, 0],
                    [0, 0]]
        for i in range(len(self.list_1)):
            for j in range(len(self.list_2[i])):
                matr_sum[i][j] = self.list_1[i][j] + self.list_2[i][j]
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr_sum]))

my_matrix = Matrix([[10, 20],
                    [30, 40]],
                   [[50, 60],
                    [70, 80]])

print(my_matrix.__str__())
print('\n', 'Суммарная матрица', '\n', my_matrix.__add__())