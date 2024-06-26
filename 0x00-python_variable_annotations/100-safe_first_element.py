#!/usr/bin/env python3
"""defines duck typed function"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """elements of the input not known"""
    if lst:
        return lst[0]
    else:
        return None
