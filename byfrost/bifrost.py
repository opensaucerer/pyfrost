#!/usr/bin/env python3

from .shared.types.dataclass.bridge import BridgeConfig, RainbowBridge
from .shared.errors.interface import BifrostError
from typing import Tuple


def new_rainbow_bridge(bc: BridgeConfig) -> Tuple[RainbowBridge, BifrostError]:
    pass