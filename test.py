import os
import unittest
import numpy as np
import shutil
from image import latex_generator
from math_module import check_matrix_issquare, convert_number, determinant, inverse, remove_file, solve, power
from utils import save_feedback

class ImageTest(unittest.TestCase):
    def test_correct_latex(self):
        """Тест с правильным значением"""
        latex = r"$\frac{1}{2}$"
        filename = "image1.png"
        colors = ((255, 255, 255), (0, 0, 0))
        folder = "images"
        fontsize = 300
        latex_generator(latex, filename, colors, folder, fontsize)
        self.assertTrue(os.path.exists(os.path.join(folder, filename)))
        
    def test_incorrect_latex(self):
        """Тест с неправильным значением"""
        latex = r"""$$
                12"""
        filename = "image2.png"
        colors = ((255, 255, 255), (0, 0, 0))
        folder = "images"
        fontsize = 300
        with self.assertRaises(Exception):
            latex_generator(latex, filename, colors, folder, fontsize)

class ConvertationTest(unittest.TestCase):
    def test_correct_convert_1(self):
        """Тест со значением float"""
        n = 3.14159265359
        expected_output = 3.142
        self.assertEqual(convert_number(n), expected_output)
        
    def test_correct_convert_2(self):
        """Тест со значением int"""
        n = 5
        expected_output = 5
        self.assertEqual(convert_number(n), expected_output)
        
    def test_correct_convert_3(self):
        """Тест с отрицательным значением"""
        n = -2.71828182846
        expected_output = -2.718
        self.assertEqual(convert_number(n), expected_output)

    def test_correct_convert_4(self):
        """Тест с отбрасыванием дробной части"""
        n = 0.00000000001
        expected_output = 0
        self.assertEqual(convert_number(n), expected_output)

class TestDeterminant(unittest.TestCase):
    def test_determinant_1(self):
        """Тест с правильным вводом"""
        matrix = '1 2; 3 4'
        colors = ((255, 255, 255), (0, 0, 0))
        cid = 'determinant1'
        expected_output = 'image_determinant1'
        expected_path = 'image_determinant1.png'
        self.assertEqual(determinant(matrix, colors, cid), expected_output)
        self.assertTrue(os.path.exists(os.path.join("images", expected_path)))
    def test_determinant_2(self):
        """Тест с неквадратной матрицей"""
        matrix = '1 2 3; 4 5 6'
        colors = ((255, 255, 255), (0, 0, 0))
        cid = 'determinant2'
        with self.assertRaises(np.linalg.LinAlgError):
            determinant(matrix, colors, cid)
    def test_determinant_3(self):
        """Тест с неверной матрицей"""
        matrix = '1 2 3; 4 5 6; 7 8'
        colors = ((255, 255, 255), (0, 0, 0))
        cid = 'determinant3'
        with self.assertRaises(ValueError):
            determinant(matrix, colors, cid)
    def test_determinant_5(self):
        """Тест с нулевой матрицей"""
        matrix = '0 0; 0 0'
        colors = ((255, 255, 255), (0, 0, 0))
        cid = 'determinant5'
        expected_output = 'image_determinant5'
        expected_path = 'image_determinant5.png'
        self.assertEqual(determinant(matrix, colors, cid), expected_output)
        self.assertTrue(os.path.exists(os.path.join("images", expected_path)))

class TestInverse(unittest.TestCase):
    def test_inverse_1(self):
        """Тест с правильным вводом"""
        matrix = '1 2; 3 4'
        colors = ((255, 255, 255), (0, 0, 0))
        cid = 'inverse1'
        expected_output = 'image_inverse1'
        expected_path = 'image_inverse1.png'
        self.assertEqual(inverse(matrix, colors, cid), expected_output)
        self.assertTrue(os.path.exists(os.path.join("images", expected_path)))
    def test_inverse_2(self):
        """Тест с неквадратной матрицей"""
        matrix = '1 2 3; 4 5 6'
        colors = ((255, 255, 255), (0, 0, 0))
        cid = 'inverse2'
        with self.assertRaises(np.linalg.LinAlgError):
            inverse(matrix, colors, cid)
    def test_inverse_3(self):
        """Тест с неверной матрицей"""
        matrix = '1 2 3; 4 5 6; 7 8'
        colors = ((255, 255, 255), (0, 0, 0))
        cid = 'inverse3'
        with self.assertRaises(ValueError):
            inverse(matrix, colors, cid)
    def test_inverse_4(self):
        """Тест с нулевой матрицей"""
        matrix = '0 0; 0 0'
        colors = ((255, 255, 255), (0, 0, 0))
        cid = 'inverse4'
        expected_output = 'image_inverse4'
        expected_path = 'image_inverse4.png'
        self.assertEqual(inverse(matrix, colors, cid), expected_output)
        self.assertTrue(os.path.exists(os.path.join("images", expected_path)))

class TestSolve(unittest.TestCase):
    def test_solve_1(self):
        """Тест с правильным вводом"""
        matrix = '1 2; 3 4'
        vector = '1; 2'
        colors = ((255, 255, 255), (0, 0, 0))
        cid = 'solve1'
        expected_output = 'image_solve1'
        expected_path = 'image_solve1.png'
        self.assertEqual(solve(matrix, vector, colors, cid), expected_output)
        self.assertTrue(os.path.exists(os.path.join("images", expected_path)))
    def test_solve_2(self):
        """Тест с неквадратной матрицей и правильным вектором"""
        matrix = '1 2 3; 4 5 6'
        vector = '1; 2'
        colors = ((255, 255, 255), (0, 0, 0))
        cid = 'solve2'
        with self.assertRaises(np.linalg.LinAlgError):
            solve(matrix, vector, colors, cid)
    def test_solve_3(self):
        """Тест с неправильной матрицей и правильным вектором"""
        matrix = '1 2; 3'
        vector = '1; 2'
        colors = ((255, 255, 255), (0, 0, 0))
        cid = 'solve3'
        with self.assertRaises(ValueError):
            solve(matrix, vector, colors, cid)
    def test_solve_4(self):
        """Тест с правильной матрицей и вектором неправильного размера"""
        matrix = '1 2; 3 4'
        vector = '1; 2; 3'
        colors = ((255, 255, 255), (0, 0, 0))
        cid = 'solve4'
        with self.assertRaises(ValueError):
            solve(matrix, vector, colors, cid)
    def test_solve_5(self):
        """Тест с нулевой матрицей и вектором правильного размера"""
        matrix = '0 0; 0 0'
        vector = '1; 2'
        colors = ((255, 255, 255), (0, 0, 0))
        cid = 'solve5'
        with self.assertRaises(ValueError):
            solve(matrix, vector, colors, cid)

class TestPower(unittest.TestCase):
    def test_power_1(self):
        """Тест с правильным вводом"""
        matrix = '1 2; 3 4'
        power_input = 3
        colors = ((255, 255, 255), (0, 0, 0))
        cid = 'power1'
        expected_output = 'image_power1'
        expected_path = 'image_power1.png'
        self.assertEqual(power(matrix, power_input, colors, cid), expected_output)
        self.assertTrue(os.path.exists(os.path.join("images", expected_path)))
    def test_power_2(self):
        """Тест с неквадратной матрицей"""
        matrix = '1 2 3; 4 5 6'
        power_input = 3
        colors = ((255, 255, 255), (0, 0, 0))
        cid = 'power2'
        with self.assertRaises(np.linalg.LinAlgError):
            power(matrix, power_input, colors, cid)
    def test_power_3(self):
        """Тест с неверной матрицей"""
        matrix = '1 2 3; 4 5 6; 7 8'
        power_input = 3
        colors = ((255, 255, 255), (0, 0, 0))
        cid = 'power3'
        with self.assertRaises(ValueError):
            power(matrix, power_input, colors, cid)

class TestSquareCheck(unittest.TestCase):
    def test_square_1(self):
        """Тест с неквадратной матрицей"""
        matrix = '1 2 3; 4 5 6'
        with self.assertRaises(np.linalg.LinAlgError):
            check_matrix_issquare(matrix, "power")
    def test_square_2(self):
        """Тест с неверной матрицей"""
        matrix = '1 2 3; 4 5 6; 7 8'
        with self.assertRaises(ValueError):
            check_matrix_issquare(matrix, "power")
    def test_square_3(self):
        """Тест с правильной матрицей и нулевым определителем"""
        matrix = '1 2 3; 4 5 6; 7 8 9'
        with self.assertRaises(np.linalg.LinAlgError):
            check_matrix_issquare(matrix, "solve")

class TestFileRemoval(unittest.TestCase):
    def test_removal_1(self):
        cid = 'image1'
        path = 'image1.png'
        remove_file(cid, "images")
        self.assertFalse(os.path.exists(os.path.join("images", path)))
    def test_removal_2(self):
        cid = 'image2'
        with self.assertRaises(FileNotFoundError):
            remove_file(cid, "images")

class TestSaveFeedback(unittest.TestCase):
    def setUp(self):
        self.NOT_A_FOLDER_PATH = 'test_not_a_folder'
        self.TEST_FOLDER_PATH = 'test_report_folder'

    def test_report_isnt_folder(self):
        with open(self.NOT_A_FOLDER_PATH, 'w') as f:
            f.write('')
        self.assertIsNone(save_feedback('', 0, folder=self.NOT_A_FOLDER_PATH))

    def test_write_to_folder(self):
        os.mkdir(self.TEST_FOLDER_PATH)
        report_text='hello'
        path = save_feedback(report_text, 0, folder=self.TEST_FOLDER_PATH)
        
        self.assertTrue(os.path.exists(path))

        with open(path, 'r') as f:
            text_from_file = f.read()
        self.assertEqual(text_from_file, report_text)

    def tearDown(self):
        if os.path.exists(self.NOT_A_FOLDER_PATH):
            os.remove(self.NOT_A_FOLDER_PATH)

        if os.path.exists(self.TEST_FOLDER_PATH):
            shutil.rmtree(self.TEST_FOLDER_PATH)

if __name__ == '__main__':
    unittest.main()