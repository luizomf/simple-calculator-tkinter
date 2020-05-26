import re
import math
import tkinter as tk
from typing import List


class Calculator:
    def __init__(
        self,
        root: tk.Tk,
        label: tk.Label,
        display: tk.Entry,
        buttons: List[List[tk.Button]]
    ) -> None:
        self.root = root
        self.label = label
        self.display = display
        self.buttons = buttons

    def start(self):
        self._config_display()
        self._config_buttons()
        self.root.mainloop()

    def _config_display(self):
        d = self.display
        d.bind('<Return>', self.calculate)
        d.bind('<KP_Enter>', self.calculate)

    def _config_buttons(self):
        buttons = self.buttons
        for row_values in buttons:
            for button in row_values:
                button_text = button['text']

                if button_text == 'C':
                    button.bind('<Button-1>', self.clear)
                    button.config(bg='#EA4335', fg='#fff')

                if button_text in '0123456789.+-/*()^':
                    button.bind('<Button-1>', self.add_text_to_display)

                if button_text == '=':
                    button.bind('<Button-1>', self.calculate)
                    button.config(bg='#4785F4', fg='#fff')

    def calculate(self, event=None):
        # Tive que alterar esse trecho de código
        # as contas estavam sendo resolvidas em ordens
        # incorretas. Deu uma diferença boa =)
        fixed_text = self._fix_text(self.display.get())

        try:
            fixed_text = self._solve_parentheses(fixed_text)
            fixed_text = self._solve_exponentiations(fixed_text)
            result = eval(fixed_text)

            self.display.delete(0, 'end')
            self.display.insert('end', result)
            self.label.config(text=f'{fixed_text} = {result}')
        except OverflowError:
            self.label.config(text='Não consegui realizar essa conta, sorry!')
        except Exception:
            self.label.config(text='Conta inválida')

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

    def add_text_to_display(self, event=None):
        self.display.insert('end', event.widget['text'])
        self.display.focus()

    def clear(self, event=None):
        self.display.delete(0, 'end')
