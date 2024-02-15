import os

"""
This class will contain all functionality needed to store and
retreive relevant memory information
"""
class Memory:

    def __init__(self):
        # initialize the memory directory with the root ARI if it does not exist
        self.path = os.path.join(os.path.dirname(__file__), "../.memory_data")
        if not os.path.exists(self.path):
            os.makedirs(self.path)
            with open(f"{self.path}/root.ari", "w") as f:
                f.write("")


    def memory_search(self, memory):
        with open(f"{self.path}/root.ari", "r") as f:
            root_mem = f.read()

mem = Memory()
mem.memory_search("")