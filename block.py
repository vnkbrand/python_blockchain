class Block:
    """
    Block: unit of storage
    Store txns in a blockchain that supports cryptocurrency
    """
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f'Block - data: {self.data}'

block = Block('foo')
print(block)