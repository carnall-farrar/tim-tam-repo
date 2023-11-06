import matplotlib as mpl

CYAN = "#26a5b8"
MAGENTA = "#dd0075"
YELLOW = "#ffcc00"
GREEN = "#61B776"
PURPLE = "#612aa1"
ORANGE = "#ff9900"


class CF:
    cyan = CYAN
    magenta = MAGENTA
    yellow = YELLOW
    green = GREEN
    purple = PURPLE
    orange = ORANGE
    colours = [CYAN, MAGENTA, YELLOW, GREEN, PURPLE, ORANGE]

    @staticmethod
    def set_colours():
        mpl.rcParams["axes.prop_cycle"] = mpl.cycler(color=CF.colours)


def show_trivial_demo():
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.DataFrame()
    df.index = list(range(10))
    df["y1"] = df.index ** 2
    df["y2"] = df.index ** 3

    msg1 = "Before setting CF colours (please quit this popup window now)"
    print(msg1)
    df.plot(lw=5, title=msg1)
    plt.show()

    msg2 = "After setting CF colours:"
    print(msg2)
    CF.set_colours()
    df.plot(lw=5, title=msg2)
    plt.show()


if __name__ == "__main__":
    show_trivial_demo()
