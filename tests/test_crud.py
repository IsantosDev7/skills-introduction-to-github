import unittest

from crud import CRUDStore


class CRUDStoreTests(unittest.TestCase):
    def setUp(self):
        self.store = CRUDStore()

    def test_create_and_read_item(self):
        self.store.create("1", {"name": "Mona"})
        self.assertEqual(self.store.read("1"), {"name": "Mona"})

    def test_create_duplicate_item_raises_value_error(self):
        self.store.create("1", {"name": "Mona"})
        with self.assertRaises(ValueError):
            self.store.create("1", {"name": "Hubot"})

    def test_update_item(self):
        self.store.create("1", {"name": "Mona"})
        self.store.update("1", {"name": "Hubot"})
        self.assertEqual(self.store.read("1"), {"name": "Hubot"})

    def test_delete_item(self):
        self.store.create("1", {"name": "Mona"})
        deleted = self.store.delete("1")
        self.assertEqual(deleted, {"name": "Mona"})
        with self.assertRaises(KeyError):
            self.store.read("1")

    def test_missing_item_operations_raise_key_error(self):
        with self.assertRaises(KeyError):
            self.store.read("missing")
        with self.assertRaises(KeyError):
            self.store.update("missing", {"name": "Nobody"})
        with self.assertRaises(KeyError):
            self.store.delete("missing")

    def test_list_all_returns_copy(self):
        self.store.create("1", {"name": "Mona"})
        snapshot = self.store.list_all()
        snapshot["2"] = {"name": "Hubot"}
        self.assertNotIn("2", self.store.list_all())


if __name__ == "__main__":
    unittest.main()
