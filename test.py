import re
import math


class CalculatorStub:
    def _fix_text(self, text):
        # Substitui tudo que não for 0123456789./*-+^ para nada
        text = re.sub(r'[^\d\.\/\*\-\+\^\(\)e]', r'', text, 0)
        # Substitui sinais repetidos para apenas um sinal
        text = re.sub(r'([\.\+\/\-\*\^])\1+', r'\1', text, 0)
        # Substitui () ou *() para nada
        text = re.sub(r'\*?\(\)', '', text)
        # Substitui ^ para **
        # text = text.replace('^', '**')

        return text

    def _solve_exponentiations(self, equation):
        exp_regex = re.compile(r'\d+\.?\d*(?:\^|\*\*)\d+\.?\d*', flags=re.S)
        new_equation = self._fix_text(equation)
        found_equations = exp_regex.findall(new_equation)

        while found_equations:
            for equation in found_equations:
                first_value, second_value = re.split(r'(?:\^|\*\*)', equation)
                result = math.pow(float(first_value), float(second_value))
                new_equation = new_equation.replace(equation, str(result), 1)
            found_equations = exp_regex.findall(new_equation)
        return new_equation

    def _solve_parentheses(self, equation):
        parentheses_regex = re.compile(r'\([\d\^\/\*\-\+\.]+\)', flags=re.S)
        new_equation = self._fix_text(equation)
        found_equations = parentheses_regex.findall(new_equation)

        while found_equations:
            for equation in found_equations:
                exponentiations_solved = self._solve_exponentiations(equation)
                result = eval(self._fix_text(exponentiations_solved))
                new_equation = new_equation.replace(equation, str(result), 1)
            found_equations = parentheses_regex.findall(new_equation)
        return new_equation


if __name__ == "__main__":
    equation = '9^9^9^9'
    c = CalculatorStub()
    test = c._fix_text(equation)
    print('par')
    test = c._solve_parentheses(test)
    print('vai?')
    test = c._solve_exponentiations(test)
    print(test)
