from dragonfly import *

map = {
    "up [<n>]":                         Key("up:%(n)d"),
    "down [<n>]":                       Key("down:%(n)d"),
    "left [<n>]":                       Key("left:%(n)d"),
    "right [<n>]":                      Key("right:%(n)d"),
    "page up [<n>]":                    Key("pgup:%(n)d"),
    "page down [<n>]":                  Key("pgdown:%(n)d"),
    "up <n> (page | pages)":            Key("pgup:%(n)d"),
    "down <n> (page | pages)":          Key("pgdown:%(n)d"),
    "left <n> (word | words)":          Key("c-left:%(n)d"),
    "right <n> (word | words)":         Key("c-right:%(n)d"),
    "home":                             Key("home"),
    "end":                              Key("end"),
    "doc home":                         Key("c-home"),
    "doc end":                          Key("c-end"),
}

