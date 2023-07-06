#!/usr/bin/env python3
"""
type-annotated function make_multiplier that takes a float
multiplier as argument and returns a function that multiplies a float
by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function that returns a fuction"""
    def multiply(number: float) -> float:
        """multiply the arguments and return the product as a float"""
        return number * multiplier
    return multiply
