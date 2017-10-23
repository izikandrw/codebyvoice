from dragonfly import *
from utilities import release
from format import (format_text)

map = {
    "space [<n>]":                      release + Key("space:%(n)d"),
    "enter [<n>]":                      release + Key("enter:%(n)d"),
    "tab [<n>]":                        Key("tab:%(n)d"),
    "delete [<n>]":                     release + Key("del:%(n)d"),
    "delete [<n> | this] (line|lines)": release + Key("home, s-down:%(n)d, del"),
    "delete [<n>] words":               release + Key("ctrl:down, shift:down, left:%(n)d, del"),
    "select [<n>] words":               release + Key("ctrl:down, shift:down, left:%(n)d"),
    "backspace [<n>]":                  release + Key("backspace:%(n)d"),
    "paste":                            release + Key("c-v"),
    "duplicate <n>":                    release + Key("c-c, c-v:%(n)d"),
    "copy":                             release + Key("c-c"),
    "cut":                              release + Key("c-x"),
    "select all":                       release + Key("c-a"),
    "[hold] shift":                     Key("shift:down"),
    "release shift":                    Key("shift:up"),
    "[hold] control":                   Key("ctrl:down"),
    "release control":                  Key("ctrl:up"),
    "release [all]":                    release,
    "new file":                         release + Key("c-n"),
    "close tab":                        release + Key("c-w"),
    "save file":                        release + Key("c-s"),
    "<formatType> <text>":              Function(format_text)
}
