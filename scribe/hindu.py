#!/usr/bin/env python3
"""
'Scribe' a random numerical 'text' on to a 'slab'.
  'text' - A sequence based on an alphabet [0, 1, 2 ...n_chars)
  'slab' - An numpy matrix

  Example:- The text [1, 0, 3, 5, 4, 2] can be written as
     0¦                                 ¦
     1¦             ██  ███       ██    ¦
     2¦            █  █ █        █  █   ¦
     3¦              █  ███   █  █ █    ¦
     4¦   █    ██  █  █   █  █  █ █     ¦
     5¦   █   █  █  ██  █ █ ████ ████   ¦
     6¦   █   █  █      ███   █         ¦
     7¦        ██           █           ¦

"""
import numpy as np
from .alphabet import Alphabet

numbers_ = [
    [
        [0,1,1,0],
        [1,0,0,1],
        [1,0,0,1],
        [0,1,1,0],
    ],
    [
        [1,1,0],
        [0,1,0],
        [0,1,0],
        [1,1,1],
    ],
    [
        [0,1,1,0],
        [1,0,0,1],
        [0,0,1,0],
        [0,1,0,0],
        [1,1,1,1],
    ],
    [
        [0,1,1,0],
        [1,0,0,1],
        [0,0,1,0],
        [1,0,0,1],
        [0,1,1,0],
    ],
    [
        [0,0,1,0,0,1],
        [0,1,0,0,1,0],
        [1,1,1,1,0,0],
        [0,0,1,0,0,0],
        [0,1,0,0,0,0],
    ],
    [
        [1,1,1],
        [1,0,0],
        [1,1,1],
        [0,0,1],
        [1,0,1],
        [1,1,1],
    ],
    [
        [0,1,1,0],
        [1,0,0,0],
        [1,1,1,0],
        [1,0,0,1],
        [0,1,1,0],
    ],
    [
        [1,1,1,1,1],
        [0,0,0,1,0],
        [0,0,1,0,0],
        [0,1,1,1,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
    ],
    [
        [0,1,1,0],
        [1,0,0,1],
        [0,1,1,0],
        [1,0,0,1],
        [0,1,1,0],
    ],
    [
        [0,1,1,0],
        [1,0,0,1],
        [0,1,1,1],
        [0,0,0,1],
        [0,0,1,0],
    ]

]

numbers = [np.asarray(num) for num in numbers_]
hindu_alphabet = Alphabet(numbers)