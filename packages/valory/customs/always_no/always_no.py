# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2023-2024 Valory AG
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""This module contains a conservative strategy that never bets."""

from typing import Union, Dict, Tuple


def get_bet_amount() -> Dict[str, Union[int, Tuple[str]]]:
    """Get the bet amount 0."""
    return {"bet_amount": 0}


def run(*_args, **kwargs) -> Dict[str, Union[int, Tuple[str]]]:
    """Run the strategy."""
    return get_bet_amount(**kwargs)
