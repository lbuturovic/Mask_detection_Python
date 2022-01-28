import os
import numpy as np
from matplotlib import pyplot as plt

PATH = './Resources/charts/'


def create_folder():
    if (os.path.isdir(PATH) == False):
        # kreiraj folder
        os.mkdir(PATH)


def plot_barchart(categories, values, title, xlabel, ylabel, file_title, color="mediumorchid"):
    create_folder()
    x_pos = np.arange(len(categories))
    plt.bar(x_pos, values, color=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(x_pos, categories)
    plt.savefig('./Resources/charts/{}.png'.format(file_title))
    plt.show()


def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct, v=val)

    return my_autopct


def plot_pie_chart(categories, values, title, file_title, colors):
    create_folder()
    if colors is None or len(colors) != len(categories):
        colors = plt.rcParams['axes.color_cycle']
    plt.figure(figsize=plt.figaspect(1))
    plt.pie(values, labels=categories, autopct=make_autopct(values), colors=colors)
    plt.title(title)
    plt.savefig('./Resources/charts/{}.png'.format(file_title))
    plt.show()


