from rlp.sedes import (
    CountableList,
)

from eth.rlp.headers import (
    BlockHeader,
)
from eth.vm.forks.byzantium.transactions import (
    ByzantiumTransaction,
)


class StretchBlock(ByzantiumBlock):
    transaction_class = ByzantiumTransaction
    fields = [
        ('header', BlockHeader),
        ('transactions', CountableList(transaction_class)),
        ('uncles', CountableList(BlockHeader))
    ]
