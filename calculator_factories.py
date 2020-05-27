import tkinter as tk
from typing import List


def make_root() -> tk.Tk:
    root = tk.Tk()
    root.title('Calculator')
    root.config(padx=10, pady=10, background='#fff')
    root.resizable(False, False)
    return root


def make_label(root, **grid_options) -> tk.Label:
    label = tk.Label(
        root, text='Sem conta ainda',
        anchor='e', justify='right', background='#fff'
    )
    label.grid(**grid_options)
    return label


def make_display(root, **grid_options) -> tk.Entry:
    display = tk.Entry(root)
    display.grid(**grid_options)
    display.config(
        font=('Helvetica', 40, 'bold'),
        justify='right', bd=1, relief='flat',
        highlightthickness=1, highlightcolor='#ccc'
    )
    display.bind('<Control-a>', _display_control_a)
    return display


def _display_control_a(event):
    event.widget.select_range(0, 'end')
    event.widget.icursor('end')
    return 'break'


def make_button(root, text, **grid_options) -> tk.Button:
    btn = tk.Button(root, text=text)
    btn.grid(**grid_options)
    btn.config(
        font=('Helvetica', 15, 'normal'),
        pady=40, width=1, background='#f1f2f3', bd=0,
        cursor='hand2', highlightthickness=0,
        highlightcolor='#ccc', activebackground='#ccc',
        highlightbackground='#ccc'
    )
    return btn


def make_buttons(root, starting_row) -> List[List[tk.Button]]:
    button_texts: List[List[str]] = [
        ['7', '8', '9', '+', 'C'],
        ['4', '5', '6', '-', '/'],
        ['1', '2', '3', '*', '^'],
        ['0', '.', '(', ')', '='],
    ]

    buttons: List[List[tk.Button]] = []

    for row, row_value in enumerate(button_texts, start=starting_row):
        button_row = []
        for col_index, col_value in enumerate(row_value):
            btn = make_button(
                root, text=col_value,
                row=row, column=col_index, sticky='news', padx=5, pady=5
            )
            button_row.append(btn)
        buttons.append(button_row)
    return buttons
