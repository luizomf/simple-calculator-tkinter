from calculator_factories import make_root, make_display, make_label, \
    make_buttons
from calculator_gui import CalculatorGui
from calculator_class import Calculator


def main():
    root = make_root()
    display = make_display(root, row=1, column=0, columnspan=5, sticky='news')
    display.grid_configure(pady=(0, 10))
    label = make_label(root, row=0, column=0, columnspan=5, sticky='news')
    buttons = make_buttons(root, starting_row=2)

    calculator = Calculator()
    calculator_gui = CalculatorGui(root, label, display, buttons, calculator)
    calculator_gui.start()


if __name__ == '__main__':
    main()
