import unittest
from calculadora import *

class Teste(unittest.TestCase):
    def test_basico(self):
        calculadora = Calculadora()
        testeDivisao = calculadora.calcular(10, 2, OperacaoFabrica.criar(Divisao()))
        self.assertEqual(testeDivisao, 5)
        testeSoma = calculadora.calcular(1, 2, OperacaoFabrica.criar(Soma()))
        self.assertEqual(testeSoma, 3)
        testeSubtracao = calculadora.calcular(10, 7, OperacaoFabrica.criar(Subtracao()))
        self.assertEqual(testeSubtracao, 3)
        testeMultiplicacao = calculadora.calcular(4, 2, OperacaoFabrica.criar(Multiplicacao()))
        self.assertEqual(testeMultiplicacao, 8)
