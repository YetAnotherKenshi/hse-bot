import os
import numpy as np 
from image import latex_generator

def convert_number(n):
    """Округляет число до 3 знаков после запятой"""
    n = np.round(n, 3)
    if n%1 != 0:
        return n
    else:
        return int(n)

def determinant(matrix, colors, cid):
    """
    Функция вычисляет определитель и генерирует изображение
    
    Параметры:
        matrix (str): Входная матрица
        colors (tuple): Кортеж с цветовой схемой
        cid (str): id текущего пользователя

    Возвращаемое значение:
        id (str): id сгенерированного изображения
    """
    matrix = np.matrix(matrix).tolist()
    det = convert_number(np.linalg.det(matrix))
    rows = []
    for row in matrix:
        row_str = " & ".join([str(elem) for elem in row])
        rows.append(row_str)
    s = "\\\\".join(rows)
    latex_string = fr"""
    $$
    \begin{{pmatrix}}
        {s}
    \end{{pmatrix}} = A
    $$
    $$
    \det A = {det}
    $$
    """

    id = "image_"+cid

    latex_generator(latex_string, f'{id}.png', colors)

    return id

def inverse(matrix, colors, cid):
    """
    Функция вычисляет обратную матрицу и генерирует изображение
    
    Параметры:
        matrix (str): Входная матрица
        colors (tuple): Кортеж с цветовой схемой
        cid (str): id текущего пользователя

    Возвращаемое значение:
        id (str): id сгенерированного изображения
    """
    matrix = np.matrix(matrix).tolist()
    det = convert_number(np.linalg.det(matrix))
    rows1 = []
    rows2 = []

    for row in matrix:
        row_str = " & ".join([str(elem) for elem in row])
        rows1.append(row_str)
    s = "\\\\".join(rows1)

    if det != 0:
        for row in np.linalg.inv(matrix).tolist():
            row_str = " & ".join([str(convert_number(elem)) for elem in row])
            rows2.append(row_str)
        s2 = "\\\\".join(rows2)

    latex_string = fr"""
    $$
    \begin{{pmatrix}}
        {s}
    \end{{pmatrix}} = A
    $$
    """ + (fr"""
    $$
    A^{{-1}} = \begin{{pmatrix}}
        {s2}
    \end{{pmatrix}}
    $$
    """ if det else fr"""
    $$
    A^{{-1}} = \not\exists
    $$
    """)

    id = "image_"+cid

    latex_generator(latex_string, f'{id}.png', colors)

    return id

def solve(matrix, vector, colors, cid):
    """
    Функция решает систему линейных уравнений и генерирует изображение
    
    Параметры:
        matrix (str): Входная матрица
        vector (str): Входной вектор
        colors (tuple): Кортеж с цветовой схемой
        cid (str): id текущего пользователя

    Возвращаемое значение:
        id (str): id сгенерированного изображения
    """
    matrix = np.matrix(matrix).tolist()
    vector = np.matrix(vector).tolist()
    solution = np.linalg.solve(matrix, vector).tolist()
    s = list(map(lambda x: r" & ".join(map(str,x)) + r" \\", matrix))
    s2 = list(map(lambda x: r" & ".join(map(str,x)) + r" \\", vector))
    s3 = list(map(lambda x: "$$\n" + f"x_{x[0]+1} = " + f"{convert_number(x[1][0])}\n" + "$$", enumerate(solution)))
    latex_string = r"""
    $$
    A = \left(
        \begin{array}""" + "{ " + "r "*len(matrix[0]) + "}" + "\n".join(s) + r"""
    \end{array}
    \right)""" + " " + r"""
    B = \left(
        \begin{array}""" + "{ " + "r "*len(vector[0]) + "}" + "\n".join(s2) + r"""
    \end{array}
    \right)
    $$""" + "\n".join(s3)

    id = "image_"+cid

    latex_generator(latex_string, f'{id}.png', colors)

    return id


def power(matrix, power, colors, cid):
    """
    Функция решает систему линейных уравнений и генерирует изображение
    
    Параметры:
        matrix (str): Входная матрица
        power (int): Степень возведения
        colors (tuple): Кортеж с цветовой схемой
        cid (str): id текущего пользователя

    Возвращаемое значение:
        id (str): id сгенерированного изображения
    """
    matrix = np.matrix(matrix).tolist()
    inv = []
    for i in np.linalg.matrix_power(matrix, power).tolist():
        row = []
        for j in i:
            row.append(convert_number(j))
        inv.append(row)
    s = list(map(lambda x: r" & ".join(map(str,x)) + r" \\", matrix))
    s_power = list(map(lambda x: r" & ".join(map(str,x)) + r" \\", inv))
    latex_string = r"""
    $$
    \left(
        \begin{array}""" + "{ " + "r"*len(matrix[0]) + " }" + "\n".join(s) + r"""
    \end{array}
    \right) = A
    $$""" + r"""
    $$
    """ + "A^{" + f"{power}" + "}" + r"""= \left(
        \begin{array}""" + "{ " + "r"*len(matrix[0]) + " }" + "\n".join(s_power) + r"""
    \end{array}
    \right)
    $$"""
    id = "image_"+cid

    latex_generator(latex_string, f'{id}.png', colors)

    return id

def check_matrix_issquare(matrix, func):
    """Проверяет, является ли матрица квадратной"""
    matrix = np.linalg.matrix_power(np.matrix(matrix), 2)
    det = int(np.linalg.det(matrix))
    if det == 0 and func == "solve":
        raise np.linalg.LinAlgError("Singular matrix")

def remove_file(id, folder):
    """Удаляет изображение с определённым id"""
    os.remove(os.path.join(folder, f'{id}.png'))