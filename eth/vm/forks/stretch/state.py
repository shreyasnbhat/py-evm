from eth.vm.forks.byzantium.state import (
    ByzantiumState
)

from .computation import StretchComputation


class ConstantinopleState(ByzantiumState):
    computation_class = StretchComputation