from eth.vm.forks.byzantium import ByzantiumVM
from .blocks import StretchBlock
from eth.vm.forks.byzantium.state import ByzantiumState

class StretchVM(ByzantiumVM):
    # fork name
    fork = 'stretch'

    # classes
    block_class = StretchBlock  # type: Type[BaseBlock]
    _state_class = ByzantiumState  # type: Type[BaseState]
