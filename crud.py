class CRUDStore:
    def __init__(self):
        self._items = {}

    def create(self, item_id, value):
        if item_id in self._items:
            raise ValueError(f"Item '{item_id}' already exists")
        self._items[item_id] = value
        return value

    def read(self, item_id):
        if item_id not in self._items:
            raise KeyError(f"Item '{item_id}' was not found")
        return self._items[item_id]

    def update(self, item_id, value):
        if item_id not in self._items:
            raise KeyError(f"Item '{item_id}' was not found")
        self._items[item_id] = value
        return value

    def delete(self, item_id):
        if item_id not in self._items:
            raise KeyError(f"Item '{item_id}' was not found")
        return self._items.pop(item_id)

    def list_all(self):
        return dict(self._items)
