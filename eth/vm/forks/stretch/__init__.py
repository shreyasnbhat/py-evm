from eth.vm.forks.byzantium import ByzantiumVM
from .blocks import StretchBlock
from eth.vm.forks.byzantium.state import ByzantiumState
from .xmessage import StretchXMessage
from typing import (
    Tuple,
)

from .headers import StretchBlockHeader
from eth.db.trie import make_trie_root_and_nodes


class StretchVM(ByzantiumVM):
    # fork name
    fork = 'stretch'

    # classes
    block_class = StretchBlock
    _state_class = ByzantiumState

    def set_block_xmessages_received(self,
                               base_block: StretchBlock,
                               new_header: StretchBlockHeader,
                               xmessages_received: Tuple[StretchXMessage, ...]) -> StretchBlock:

        tx_root_hash, tx_kv_nodes = make_trie_root_and_nodes(xmessages_received)
        self.chaindb.persist_trie_data_dict(tx_kv_nodes)

        return base_block.copy(
            xmessages_received=xmessages_received,
            header=new_header.copy(
                xmessages_received_root=tx_root_hash,
            ),
        )

    def set_block_xmessages_sent(self,
                               base_block: StretchBlock,
                               new_header: StretchBlockHeader,
                               xmessages_sent: Tuple[StretchXMessage, ...]) -> StretchBlock:

        tx_root_hash, tx_kv_nodes = make_trie_root_and_nodes(xmessages_sent)
        self.chaindb.persist_trie_data_dict(tx_kv_nodes)

        return base_block.copy(
            xmessages_sent=xmessages_sent,
            header=new_header.copy(
                xmessages_sent_root=tx_root_hash,
            ),
        )
