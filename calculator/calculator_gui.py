import tkinter as tk
from typing import List, Callable


class CalculatorGui:
    """ Manages tkinter """

    def __init__(
        self,
        root: tk.Tk,
        label: tk.Label,
        display: tk.Entry,
        button_list: List[List[tk.Button]],
        do_calculate: Callable[[str], str]
    ) -> None:
        self.root = root
        self.label = label
        self.display = display
        self.button_list = button_list
        self.do_calculate = do_calculate

    def start(self) -> None:
        """Start the gui"""
        self._config_display()
        self._config_buttons()
        self.root.mainloop()

    def _config_display(self) -> None:
        """Display configs"""
        display = self.display
        display.bind('<Return>', self.do_calculate)
        display.bind('<KP_Enter>', self.do_calculate)

    def _config_buttons(self) -> None:
        """All button configs"""
        buttons_list = self.button_list
        for row in buttons_list:
            for button in row:
                button_text = button['text']

                if button_text == 'C':
                    button.bind('<Button-1>', self.clear_display)
                    button.config(bg='#EA4335', fg='#fff')

                if button_text in '0123456789.+-/*()^':
                    button.bind('<Button-1>', self.add_text_to_display)

                if button_text == '=':
                    button.bind('<Button-1>', self.calculate)
                    button.config(bg='#4785F4', fg='#fff')

    def calculate(self, event=None) -> None:
        """Solve equations"""
        equation = self.display.get()

        try:
            result = self.do_calculate(equation)

            self.display.delete(0, 'end')
            self.display.insert('end', result)
            self.label.config(text=f'{equation} = {result}')
        except OverflowError:
            self.label.config(text='Não consegui realizar essa conta, sorry!')
        except Exception:
            self.label.config(text='Conta inválida')

    def add_text_to_display(self, event=None) -> None:
        """Add text to display"""
        self.display.insert('end', event.widget['text'])
        self.display.focus()

    def clear_display(self, event=None) -> None:
        """Clear display"""
        self.display.delete(0, 'end')
