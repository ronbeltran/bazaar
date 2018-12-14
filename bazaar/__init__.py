import os

try:
    from secrets import choice  # >= python3.6
except ImportError:
    from random import choice  # < python3.6

BASE_DIR = os.path.join(os.path.dirname(__file__))
WORDS_DIR = os.path.join(BASE_DIR, 'words')


class Bazaar(object):

    def __init__(self):
        self.item = self.get_item("items.txt")
        self.adj = self.get_item("adj.txt")
        self.obj = "{} {}".format(self.adj, self.item)
        self.super_item = self.get_item("superitems.txt")
        self.super_adj = self.get_item("superadj.txt")
        self.super_obj = "{} {}".format(self.super_adj, self.super_item)
        self.heroku = "-".join([self.super_adj, self.super_item,
                               str(choice([x for x in range(1000, 9999)]))])

    @property
    def Adj(self):
        return self.adj.title()

    @property
    def Item(self):
        return self.item.title()

    @property
    def Obj(self):
        return self.obj.title()

    @property
    def Super_adj(self):
        return self.super_adj.title()

    @property
    def Super_item(self):
        return self.super_item.title()

    @property
    def Super_obj(self):
        return self.super_obj.title()

    def get_item(self, filename):
        path = os.path.join(WORDS_DIR, filename)
        with open(path) as f:
            content = f.read()
            return choice(content.split('\n'))
