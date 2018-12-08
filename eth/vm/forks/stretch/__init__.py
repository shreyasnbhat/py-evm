from typing import (  # noqa: F401
    Type,
)

from eth.rlp.blocks import BaseBlock  # noqa: F401
from eth.vm.forks.byzantium import (
    ByzantiumVM,
    get_uncle_reward,
)
from eth.vm.state import BaseState  # noqa: F401

from .blocks import StretchBlock
from .constants import EIP1234_BLOCK_REWARD
from .headers import (
    compute_stretch_difficulty,
    configure_stretch_header,
    create_stretch_header_from_parent,
)
from .state import StretchState


class StretchVM(ByzantiumVM):
    # fork name
    fork = 'stretch'

    # classes
    block_class = StretchBlock  # type: Type[BaseBlock]
    _state_class = StretchState  # type: Type[BaseState]

    # Methods
    create_header_from_parent = staticmethod(create_stretch_header_from_parent)  # type: ignore  # noqa: E501
    compute_difficulty = staticmethod(compute_stretch_difficulty)    # type: ignore
    configure_header = configure_stretch_header
    get_uncle_reward = staticmethod(get_uncle_reward(EIP1234_BLOCK_REWARD))

    @staticmethod
    def get_block_reward() -> int:
        return EIP1234_BLOCK_REWARD
