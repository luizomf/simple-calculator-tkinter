import re
# import math
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
        fixed_text = self._fix_text(self.display.get())

        try:
            result = eval(fixed_text)
            self.display.delete(0, 'end')
            self.display.insert('end', result)
            self.label.config(text=f'{fixed_text} = {result}')

        except OverflowError:
            self.label.config(text='Não consegui realizar essa conta, sorry!')
        except Exception:
            self.label.config(text='Conta inválida')

    def _get_equations(self, text):
        return re.split(r'\^', text, 0)

    def _fix_text(self, text):
        # Substitui tudo que não for 0123456789./*-+^ para nada
        text = re.sub(r'[^\d\.\/\*\-\+\^\(\)e]', r'', text, 0)
        # Substitui sinais repetidos para apenas um sinal
        text = re.sub(r'([\.\+\/\-\*\^])\1+', r'\1', text, 0)
        # Substitui () ou *() para nada
        text = re.sub(r'\*?\(\)', '', text)
        # Substitui ^ para **
        text = text.replace('^', '**')

        return text

    def add_text_to_display(self, event=None):
        self.display.insert('end', event.widget['text'])
        self.display.focus()

    def clear(self, event=None):
        self.display.delete(0, 'end')
