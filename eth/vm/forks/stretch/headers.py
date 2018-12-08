from eth.vm.forks.byzantium.headers import (
    configure_header,
    create_header_from_parent,
    compute_difficulty,
)


compute_stretch_difficulty = compute_difficulty(5000000)

create_stretch_header_from_parent = create_header_from_parent(
    compute_stretch_difficulty
)
configure_stretch_header = configure_header(compute_stretch_difficulty)