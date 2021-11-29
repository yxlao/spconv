# Copyright 2021 Yan Yan
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from pathlib import Path
from typing import List
from pccm.utils import project_is_editable, project_is_installed

PACKAGE_NAME = "spconv"
PACKAGE_ROOT = Path(__file__).parent.resolve()

EDITABLE_INSTALLED = project_is_installed(
    PACKAGE_NAME) and project_is_editable(PACKAGE_NAME)

_filter_hwio_env = os.getenv("SPCONV_FILTER_HWIO", None)
if _filter_hwio_env is not None:
    raise NotImplementedError("SPCONV_FILTER_HWIO is deprecated. use SPCONV_SAVED_WEIGHT_LAYOUT instead.")

DISABLE_JIT = os.getenv("SPCONV_DISABLE_JIT", "0") == "1"
NDIM_DONT_CARE = 3
FILTER_HWIO = False

SAVED_WEIGHT_LAYOUT = os.getenv("SPCONV_SAVED_WEIGHT_LAYOUT", "")

if SAVED_WEIGHT_LAYOUT != "":
    assert SAVED_WEIGHT_LAYOUT in ["KRSC", "RSKC", "RSCK"], "please set SAVED_WEIGHT_LAYOUT to KRSC, RSKC or RSCK"

ALL_WEIGHT_IS_KRSC = True

SPCONV_DEBUG_SAVE_PATH = os.getenv("SPCONV_DEBUG_SAVE_PATH", "")


_BOOST_ROOT = os.getenv("BOOST_ROOT", None)

if _BOOST_ROOT is None:
    BOOST_ROOT = None 
else:
    BOOST_ROOT = Path(_BOOST_ROOT)
    assert BOOST_ROOT.exists(), "you provide BOOST_ROOT, but it not exists"
    assert (BOOST_ROOT / "boost" / "geometry").exists(), "you provide BOOST_ROOT, but BOOST_ROOT/boost/geometry not exists"
