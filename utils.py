from datetime import datetime
import os

def save_feedback(cid, text, folder='reports'):
    """
    Генерирует изображение из LaTeX формулы
    
    Параметры:
        text (str): Текст обратной связи
        cid (str): id пользователя
        folder (str): Путь, где будут храниться обратная связь
    """
    fn = f'report_{str(cid)}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt'
    path = os.path.join(folder, fn)
    if not os.path.exists(folder):
        os.mkdir(folder)
    else:
        if not os.path.isdir(folder):
            return None
    try:
        with open(path, 'w') as f:
            f.write(text)
    except:
        return None
    else:
        return path

def check_matrix_input(text):
    """
    Проверяет пользовательский ввод матрицы на наличие недопустимых символов.
    
    Параметры
    text (str): Строка, введённая пользователем
    
    Возвращает True если строка подходит, и False, если есть недопустимые символы
    """
    
    ALLOWED = '0123456789;- '
    for c in text:
        if c not in ALLOWED:
            return False
    return True
