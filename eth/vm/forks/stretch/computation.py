from cytoolz import (
    merge,
)

from eth.vm.forks.byzantium.computation import (
    BYZANTIUM_PRECOMPILES
)
from eth.vm.forks.byzantium.computation import (
    ByzantiumComputation
)
from eth.vm.gas_meter import (
    allow_negative_refund_strategy,
    GasMeter,
)

STRETCH_PRECOMPILES = merge(
    BYZANTIUM_PRECOMPILES,
    {
        # TODO: add new pre-compiles
    },
)


class StretchComputation(ByzantiumComputation):
    """
    A class for all execution computations in the ``Stretch`` fork.
    Inherits from :class:`~eth.vm.forks.byzantium.computation.ByzantiumComputation`
    """

    # Override
    opcodes = STRETCH_OPCODES
    _precompiles = STRETCH_PRECOMPILES

    def get_gas_meter(self) -> GasMeter:
        return GasMeter(
            self.msg.gas,
            allow_negative_refund_strategy
        )
