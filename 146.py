class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.capacity_usage = 0
        self.cache = {}
        self.uses = []

    def update_lru(self, key):
        if key in self.uses:      # if it had already been used
            self.uses.pop(self.uses.index(key))
        self.uses.append(key)     # add to end of array to show most recent


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        value = self.cache.get(key, -1)
        if value != -1:
            self.update_lru(key)
        return value


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        is_existing = self.get(key) != -1
        self.cache[key] = value
        if not is_existing and self.capacity_usage + 1 > self.capacity:

            # need to remove least recently used
            lru_key = self.uses[0]
            self.cache.pop(lru_key)
            self.uses.pop(0)

        self.update_lru(key)
