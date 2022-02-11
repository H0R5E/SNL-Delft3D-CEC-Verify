# -*- coding: utf-8 -*-

from __future__ import annotations

import math
import platform
from typing import Callable, List, Sequence
from pathlib import Path
from datetime import datetime
from importlib.metadata import version

from .shared import generate_grid_xy
from ..types import Num, StrOrPath
from .._docs import docstringtemplate


@docstringtemplate
def write_rectangle(path: StrOrPath,
                    dx: Num,
                    dy: Num,
                    x0: Num = 0,
                    x1: Num = 18,
                    y0: Num = 1,
                    y1: Num = 5):
    """Create a rectangular Delft3D structured mesh grid, in a rectangular 
    domain (``x0``, ``y0``, ``x1``, ``y1``), and save to the given path as
    ``D3D.grd``.
    
    :param path: destination path for the grid file
    :param dx: grid spacing in the x-direction, in metres
    :param dy: grid spacing in the y-direction, in metres
    :param x0: minimum x-value, in metres, defaults to {x0}
    :param x1: maximum x-value, in metres, defaults to {x1}
    :param y0: minimum y-value, in metres, defaults to {y0}
    :param y1: maximum y-value, in metres, defaults to {y1}
    
    """
    
    xsize = x1 - x0
    ysize = y1 - y0
    x, y = [tuple(v) for v in generate_grid_xy(x0, y0, xsize, ysize, dx, dy)]
    
    msgs = make_header(x, y) + make_eta_x(x, y) + make_eta_y(x, y)
    msgs = [v + "\n" for v in msgs]
    
    file_path = Path(path) / "D3D.grd"
    
    with open(file_path, "w") as f:
        f.writelines(msgs)


def make_header(x: Sequence[Num],
                y: Sequence[Num]) -> List[str]:
    
    msgs = [
         "*",
         "* Data Only Greater, SNL-Delft3D-CEC-Verify Version "
        f"{version('SNL-Delft3D-CEC-Verify')} ({platform.system()})",
         "* File creation date: "
        f"{datetime.today().strftime('%Y-%m-%d, %H:%M:%S')}",
         "*",
         "Coordinate System = Cartesian",
         "Missing Value     =   -9.99999000000000024E+02",
        f" {len(x):>7} {len(y):>7}",
         "0 0 0"
    ]
    
    return msgs


def make_eta_x(x: Sequence[Num],
               y: Sequence[Num]) -> List[str]:
    makex = lambda x, y, i, j, nnums: x[5 * j:5 * (j + 1)]
    return _make_eta(x, y, makex)


def make_eta_y(x: Sequence[Num],
               y: Sequence[Num]) -> List[str]:
    makey = lambda x, y, i, j, nnums: [y[i]] * nnums
    return _make_eta(x, y, makey)


def _make_eta(x: Sequence[Num],
              y: Sequence[Num],
              func: Callable[[Sequence[Num],
                              Sequence[Num],
                              int,
                              int,
                              int], Sequence[Num]]) -> List[str]:
    
    msgs = []
    
    for i in range(len(y)):
        
        msg = f' ETA={i + 1:>5}   '
        
        for j in range(math.ceil(len(x) / 5)):
            
            nnums = len(x[5 * j:5 * (j + 1)])
            nums = func(x, y, i, j, nnums)
            
            fmt = '{:.17E}   ' * (nnums - 1) + '{:.17E}'
            msg += fmt.format(*nums)
            msgs.append(msg)
            msg = ' ' * 13
    
    return msgs