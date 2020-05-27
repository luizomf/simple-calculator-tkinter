import re
import math


class Calculator:
    def calculate(self, equation: str) -> str:
        cleaned_equation = self._del_invalid_chars(equation)

        try:
            eq_parenteses_solved = self._solve_parentheses(cleaned_equation)
            eq_exponentiation_solved = self._solve_exponentiations(
                eq_parenteses_solved
            )

            successfully_solved_equation = eval(eq_exponentiation_solved)
            return str(successfully_solved_equation)
        except Exception:
            raise

    def _del_invalid_chars(self, equation):
        cleaned = equation
        cleaned = re.sub(r'[^\d\.\/\*\-\+\^\(\)e]', r'', cleaned, 0)
        cleaned = re.sub(r'([\.\+\/\-\*\^])\1+', r'\1', cleaned, 0)
        cleaned = re.sub(r'\*?\(\)', '', cleaned)
        return cleaned

    def _solve_exponentiations(self, equation):
        exponentiation_regex = re.compile(
            r'\d+\.?\d*(?:\^|\*\*)\d+\.?\d*', flags=re.S
        )
        new_equation = self._del_invalid_chars(equation)
        found_equations_in_regex = exponentiation_regex.findall(new_equation)

        while found_equations_in_regex:
            for equation in found_equations_in_regex:
                first_number, second_number = re.split(
                    r'(?:\^|\*\*)', equation
                )
                solved = math.pow(float(first_number), float(second_number))
                new_equation = new_equation.replace(equation, str(solved), 1)
            found_equations_in_regex = exponentiation_regex.findall(
                new_equation
            )
        return new_equation

    def _solve_parentheses(self, equation):
        parentheses_regex = re.compile(r'\([\d\^\/\*\-\+\.]+\)', flags=re.S)
        new_equation = self._del_invalid_chars(equation)
        found_equations_in_regex = parentheses_regex.findall(new_equation)

        while found_equations_in_regex:
            for equation in found_equations_in_regex:
                exponentiations_solved = self._solve_exponentiations(equation)
                result = eval(self._del_invalid_chars(exponentiations_solved))
                new_equation = new_equation.replace(equation, str(result), 1)
            found_equations_in_regex = parentheses_regex.findall(new_equation)
        return new_equation
