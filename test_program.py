#cwiczymy TDD
import unittest
from random import randint
import program

class TestProgram(unittest.TestCase):


    def test_zwroc_100(self):


        wynik = program.zwroc_100()
        self.assertEqual(wynik, 100)


    def test_dodawanko(self):
        x = randint(0,100)
        y = randint(0,100)
        wynik = program.dodawanko(x,y)
        self.assertEqual(wynik, x+y)

    def test_odejmowanko(self):
        x = randint(0,100)
        y = randint(0,100)
        wynik = program.odejmowanko(x,y)
        self.assertEqual(wynik, x-y)

    def test_mnozonko(self):
        x = randint(0,100)
        y = randint(0,100)
        wynik = program.mnozonko(x,y)
        self.assertEqual(wynik, x*y)

    def test_dzielonko(self):
        x = randint(1,100)
        y = randint(1,100)
        wynik = program.dzielonko(x,y)
        self.assertEqual(wynik, x/y)

    def test_rand_100(self):
        for x in range (0, 100):
            wynik = program.rand_100()
            self.assertLessEqual(wynik, 100)



if __name__ == "__main__":
    unittest.main()    

