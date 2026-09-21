class LRUCache:

    def __init__(self, capacity: int):
        self.dict = {}
        self.capacity = capacity
    

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        self.dict[key] = self.dict.pop(key)
        return self.dict[key]
        
    def put(self, key: int, value: int) -> None:
        self.dict.pop(key, None)
        self.dict[key] = value

        if len(self.dict) > self.capacity:
            del self.dict[next(iter(self.dict))]
    
