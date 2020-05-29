import re
import math


def del_invalid_chars(equation: str) -> str:
    cleaned = equation
    # Remove all but 0123456789./*-+^e
    cleaned = re.sub(r'[^\d\.\/\*\-\+\^\(\)e]', r'', cleaned, 0)
    # Remove duplicated operators (.+/-*^)
    cleaned = re.sub(r'([\.\+\/\-\*\^])\1+', r'\1', cleaned, 0)
    # Remove *() or ()
    cleaned = re.sub(r'\*?\(\)', '', cleaned)
    return cleaned


def solve_exponentiations(equation: str) -> str:
    exponentiation_regex = re.compile(
        r'\d+\.?\d*(?:\^|\*\*)\d+\.?\d*', flags=re.S
    )
    new_equation = del_invalid_chars(equation)
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


def solve_parentheses(equation: str) -> str:
    parentheses_regex = re.compile(r'\([\d\^\/\*\-\+\.]+\)', flags=re.S)
    new_equation = del_invalid_chars(equation)
    found_equations_in_regex = parentheses_regex.findall(new_equation)

    while found_equations_in_regex:
        for equation in found_equations_in_regex:
            exponentiations_solved = solve_exponentiations(equation)
            result = eval(del_invalid_chars(exponentiations_solved))
            new_equation = new_equation.replace(equation, str(result), 1)
        found_equations_in_regex = parentheses_regex.findall(new_equation)
    return new_equation


def calculate(equation: str) -> str:
    cleaned_equation = del_invalid_chars(equation)

    try:
        eq_parenteses_solved = solve_parentheses(cleaned_equation)
        eq_exponentiation_solved = solve_exponentiations(
            eq_parenteses_solved
        )

        successfully_solved_equation = eval(eq_exponentiation_solved)
        return str(successfully_solved_equation)
    except Exception:
        raise
