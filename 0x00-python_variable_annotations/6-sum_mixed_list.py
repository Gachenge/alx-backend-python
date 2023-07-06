#!/usr/bin/env python3
from typing import List, Union
"""
type-annotated function sum_mixed_list which takes a list mxd_lst
of integers and floats and returns their sum as a float.
"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return the sum of either int or float return as float"""
    return sum(mxd_lst)
