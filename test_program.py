#cwiczymy TDD
import unittest

import program

class TestProgram(unittest.TestCase):


    def test_zwroc_100(self):


        wynik = program.test_zwroc_100()
        self.assertEqual(wynik, 100)


    def test_inna_metoda(self):

        pass


    def test_inna_metoda_2(self):

        pass



if __name__ == "__main__":
    unittest.main()    

