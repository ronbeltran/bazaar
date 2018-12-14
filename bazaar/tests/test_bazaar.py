from unittest import TestCase

from bazaar import Bazaar


class TestBazaar(TestCase):
    def setUp(self):
        self.bazaar = Bazaar()

    def test_item(self):
        self.assertTrue(isinstance(self.bazaar.item, str))

    def test_Item(self):
        self.assertTrue(isinstance(self.bazaar.Item, str))
        self.assertEqual(self.bazaar.Item, self.bazaar.item.title())

    def test_adj(self):
        self.assertTrue(isinstance(self.bazaar.adj, str))

    def test_Adj(self):
        self.assertTrue(isinstance(self.bazaar.Adj, str))
        self.assertEqual(self.bazaar.Adj, self.bazaar.adj.title())

    def test_obj(self):
        self.assertTrue(isinstance(self.bazaar.obj, str))

    def test_Obj(self):
        self.assertTrue(isinstance(self.bazaar.obj, str))
        self.assertEqual(self.bazaar.Obj, self.bazaar.obj.title())

    def test_super_item(self):
        self.assertTrue(isinstance(self.bazaar.super_item, str))

    def test_Super_item(self):
        self.assertTrue(isinstance(self.bazaar.Super_item, str))
        self.assertEqual(self.bazaar.Super_item, self.bazaar.super_item.title())

    def test_super_adj(self):
        self.assertTrue(isinstance(self.bazaar.super_adj, str))

    def test_Super_adj(self):
        self.assertTrue(isinstance(self.bazaar.Super_adj, str))
        self.assertEqual(self.bazaar.Super_adj, self.bazaar.super_adj.title())

    def test_super_obj(self):
        self.assertTrue(isinstance(self.bazaar.super_obj, str))

    def test_Super_obj(self):
        self.assertTrue(isinstance(self.bazaar.super_obj, str))
        self.assertEqual(self.bazaar.Super_obj, self.bazaar.super_obj.title())

    def test_heroku(self):
        self.assertTrue(isinstance(self.bazaar.heroku, str))
        adj, item, number = self.bazaar.heroku.split("-")
        self.assertEqual(adj, self.bazaar.super_adj)
        self.assertEqual(item, self.bazaar.super_item)
        self.assertIn(int(number), [x for x in range(1000, 9999)])
