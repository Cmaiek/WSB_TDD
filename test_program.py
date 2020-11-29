#cwiczymy TDD
import unittest

import program

class TestProgram(unittest.TestCase):


    def test_zwroc_100(self):


        wynik = program.zwroc_100()
        self.assertEqual(wynik, 100)


    def test_inna_metoda(self):

        wynik = program.zwroc_50()
        self.assertEqual(wynik, 50)

    def test_inna_metoda_2(self):
        for x in range (0, 10):
            wynik = program.rand_100()
            self.assertLessEqual(wynik, 100)



if __name__ == "__main__":
    unittest.main()    

