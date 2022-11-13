import argparse
import matplotlib.pyplot as plt
import numpy as np

class Hexagon:
    """
    Generate a hexagon with a color and a text
    """
    def __init__(self, fill_color, border_color, text):
        self.fill_color = fill_color
        self.border_color = border_color
        self.text = text

    def _generate_geometry(self):
        """
        Generate a hexagon geometry
        """
        x = []
        y = []
        for i in range(7):
            x.append(np.cos(2 * np.pi / 6 * i))
            y.append(np.sin(2 * np.pi / 6 * i))
        return x, y

    def generate(self):
        """
        Generate a hexagon with a transparent background
        """
        fig = plt.figure()
        ax = fig.add_subplot(111)
        x, y = self._generate_geometry()
        ax.plot(x, y, color=self.border_color, linewidth=5)
        ax.fill(x, y, color=self.fill_color)
        ax.axis('off')
        ax.set_aspect('equal')
        if self.text is not None:
            ax.text(0, 0, self.text, horizontalalignment='center', verticalalignment='center', fontsize=20)
        return plt

    def generate_canvas(self):
        """
        Generate a hexagon with a color and a text
        :return: True if the hexagon is generated, False otherwise
        """
        plt = self.generate()
        plt.savefig('temp.png', transparent=True, bbox_inches='tight', pad_inches=0)
        return plt.imread('temp.png')


    def save(self, filename=None):
        """
        Generate a hexagon with a color and a text
        :return: True if the hexagon is generated, False otherwise
        """
        plt = self.generate()
        plt.savefig(filename, transparent=True, bbox_inches='tight', pad_inches=0)

def show_help():
    print('\nUsage: python main.py --filename filename --fill_color fill_color --border_color border_color --text text')
    print('\nExample: python main.py --filename hexagon.png --fill_color "#00FF00" --border_color "#000000" --text "Hello"')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', type=str, default='hexagon.png', help='filename to save')
    parser.add_argument('--fill_color', type=str, default='#FF0000', help='fill color of the hexagon')
    parser.add_argument('--border_color', type=str, default='#000000', help='border color of the hexagon')
    parser.add_argument('--text', type=str, default=None, help='text to add in the hexagon')
    args = parser.parse_args()

    if args.text is not None:
        args.text = args.text.replace('_', ' ')
        hex = Hexagon(args.fill_color, args.border_color, args.text)
        hex.save(args.filename)
