#
# This file is a command-module for Dragonfly.
# (c) Copyright 2008 by Christo Butcher
# Licensed under the LGPL, see <http://www.gnu.org/licenses/>
#

"""
Command-module for cursor movement and **editing**
============================================================================

This module allows the user to control the cursor and
efficiently perform multiple text editing actions within a
single phrase.


Example commands
----------------------------------------------------------------------------

*Note the "/" characters in the examples below are simply
to help the reader see the different parts of each voice
command.  They are not present in the actual command and
should not be spoken.*

Example: **"up 4 / down 1 page / home / space 2"**
   This command will move the cursor up 4 lines, down 1 page,
   move to the beginning of the line, and then insert 2 spaces.

Example: **"left 7 words / backspace 3 / insert hello Cap world"**
   This command will move the cursor left 7 words, then delete
   the 3 characters before the cursor, and finally insert
   the text "hello World".

Example: **"home / space 4 / down / 43 times"**
   This command will insert 4 spaces at the beginning of
   of this and the next 42 lines.  The final "43 times"
   repeats everything in front of it that many times.


Discussion of this module
----------------------------------------------------------------------------

This command-module creates a powerful voice command for
editing and cursor movement.  This command's structure can
be represented by the following simplified language model:

 - *CommandRule* -- top-level rule which the user can say
    - *repetition* -- sequence of actions (name = "sequence")
       - *KeystrokeRule* -- rule that maps a single
         spoken-form to an action
    - *optional* -- optional specification of repeat count
       - *integer* -- repeat count (name = "n")
       - *literal* -- "times"

The top-level command rule has a callback method which is
called when this voice command is recognized.  The logic
within this callback is very simple:

1. Retrieve the sequence of actions from the element with
   the name "sequence".
2. Retrieve the repeat count from the element with the name
   "n".
3. Execute the actions the specified number of times.

"""

try:
    import pkg_resources
    pkg_resources.require("dragonfly >= 0.6.5beta1.dev-r99")
except ImportError:
    pass

from dragonfly import *

from format import (
    camel_case_count,
    pascal_case_count,
    snake_case_count,
    squash_count,
    expand_count,
    uppercase_count,
    lowercase_count,
    format_text,
    FormatTypes as ft,
)

#---------------------------------------------------------------------------
# Here we globally defined the release action which releases all
#  modifier-keys used within this grammar.  It is defined here
#  because this functionality is used in many different places.
#  Note that it is harmless to release ("...:up") a key multiple
#  times or when that key is not held down at all.

release = Key("shift:up, ctrl:up")


#---------------------------------------------------------------------------
# Set up this module's configuration.

config            = Config("multi edit")
config.cmd        = Section("Language section")
config.cmd.map    = Item(
    # Here we define the *default* command map.  If you would like to
    #  modify it to your personal taste, please *do not* make changes
    #  here.  Instead change the *config file* called "_multiedit.txt".
    {
     # Spoken-form    ->    ->    ->     Action object
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

     "space [<n>]":                      release + Key("space:%(n)d"),
     "enter [<n>]":                      release + Key("enter:%(n)d"),
     "tab [<n>]":                        Key("tab:%(n)d"),
     "delete [<n>]":                     release + Key("del:%(n)d"),
     "delete [<n> | this] (line|lines)": release + Key("home, s-down:%(n)d, del"),
     "backspace [<n>]":                  release + Key("backspace:%(n)d"),
     "pop up":                           release + Key("apps"),

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

     "dragonfly":                   Text("cd C:\NatLink\NatLink\MacroSystem") + Key("enter"),

     # Format dictated words. See the formatMap for all available types.
    # Ex: "camel case my new variable" -> "myNewVariable"
    # Ex: "snake case my new variable" -> "my_new_variable
    # Ex: "uppercase squash my new hyphen variable" -> "MYNEW-VARIABLE"
    "<formatType> <text>": Function(format_text),

     "say <text>":                       release + Text("%(text)s"),
     "mimic <text>":                     release + Mimic(extra="text"),
    },
    namespace={
     "Key":   Key,
     "Text":  Text,
    }
)
namespace = config.load()

letterMap = {
    "(A|alpha)": "a",
    "(B|bravo) ": "b",
    "(C|charlie) ": "c",
    "(D|delta) ": "d",
    "(E|echo) ": "e",
    "(F|foxtrot) ": "f",
    "(G|golf) ": "g",
    "(H|hotel) ": "h",
    "(I|india|indigo) ": "i",
    "(J|juliet) ": "j",
    "(K|kilo) ": "k",
    "(L|lima) ": "l",
    "(M|mike) ": "m",
    "(N|november) ": "n",
    "(O|oscar) ": "o",
    "(P|papa|poppa) ": "p",
    "(Q|quebec|quiche) ": "q",
    "(R|romeo) ": "r",
    "(S|sierra) ": "s",
    "(T|tango) ": "t",
    "(U|uniform) ": "u",
    "(V|victor) ": "v",
    "(W|whiskey) ": "w",
    "(X|x-ray) ": "x",
    "(Y|yankee) ": "y",
    "(Z|zulu) ": "z",
}

numberMap = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

formatMap = {
    "camel case": ft.camelCase,
    "pascal case": ft.pascalCase,
    "snake case": ft.snakeCase,
    "uppercase": ft.upperCase,
    "lowercase": ft.lowerCase,
    "squash": ft.squash,
    "lowercase squash": [ft.squash, ft.lowerCase],
    "uppercase squash": [ft.squash, ft.upperCase],
    "squash lowercase": [ft.squash, ft.lowerCase],
    "squash uppercase": [ft.squash, ft.upperCase],
    "dashify": ft.dashify,
    "lowercase dashify": [ft.dashify, ft.lowerCase],
    "uppercase dashify": [ft.dashify, ft.upperCase],
    "dashify lowercase": [ft.dashify, ft.lowerCase],
    "dashify uppercase": [ft.dashify, ft.upperCase],
    "dotify": ft.dotify,
    "lowercase dotify": [ft.dotify, ft.lowerCase],
    "uppercase dotify": [ft.dotify, ft.upperCase],
    "dotify lowercase": [ft.dotify, ft.lowerCase],
    "dotify uppercase": [ft.dotify, ft.upperCase],
    "say": ft.spokenForm,
    "environment variable": [ft.snakeCase, ft.upperCase],
}

abbreviationMap = {
    "administrator": "admin",
    "administrators": "admins",
    "application": "app",
    "applications": "apps",
    "argument": "arg",
    "arguments": "args",
    "attribute": "attr",
    "attributes": "attrs",
    "(authenticate|authentication)": "auth",
    "binary": "bin",
    "button": "btn",
    "class": "cls",
    "command": "cmd",
    "(config|configuration)": "cfg",
    "context": "ctx",
    "control": "ctrl",
    "database": "db",
    "(define|definition)": "def",
    "description": "desc",
    "(develop|development)": "dev",
    "(dictionary|dictation)": "dict",
    "(direction|directory)": "dir",
    "dynamic": "dyn",
    "example": "ex",
    "execute": "exec",
    "exception": "exc",
    "expression": "exp",
    "(extension|extend)": "ext",
    "function": "func",
    "framework": "fw",
    "(initialize|initializer)": "init",
    "instance": "inst",
    "integer": "int",
    "iterate": "iter",
    "java archive": "jar",
    "javascript": "js",
    "keyword": "kw",
    "keyword arguments": "kwargs",
    "language": "lng",
    "library": "lib",
    "length": "len",
    "number": "num",
    "object": "obj",
    "okay": "ok",
    "package": "pkg",
    "parameter": "param",
    "parameters": "params",
    "pixel": "px",
    "position": "pos",
    "point": "pt",
    "previous": "prev",
    "property": "prop",
    "python": "py",
    "query string": "qs",
    "reference": "ref",
    "references": "refs",
    "(represent|representation)": "repr",
    "regular (expression|expressions)": "regex",
    "request": "req",
    "revision": "rev",
    "ruby": "rb",
    "session aidee": "sid",  # "session id" didn't work for some reason.
    "source": "src",
    "(special|specify|specific|specification)": "spec",
    "standard": "std",
    "standard in": "stdin",
    "standard out": "stdout",
    "string": "str",
    "(synchronize|synchronous)": "sync",
    "system": "sys",
    "utility": "util",
    "utilities": "utils",
    "temporary": "tmp",
    "text": "txt",
    "value": "val",
    "window": "win",
}

# Modifiers for the press-command, if only the modifier is pressed.
singleModifierMap = {
    "alt": "alt",
    "control": "ctrl",
    "shift": "shift",
    "super": "win",
}

# Modifiers for the press-command.
modifierMap = {
    "alt": "a",
    "control": "c",
    "shift": "s",
    "super": "w",
}

# For repeating of characters.
specialCharMap = {
    "(bar|vertical bar|pipe)": "|",
    "(dash|minus|hyphen)": "-",
    "(dot|period)": ".",
    "comma": ",",
    "backslash": "\\",
    "underscore": "_",
    "(star|asterisk)": "*",
    "colon": ":",
    "(semicolon|semi-colon)": ";",
    "at": "@",
    "[double] quote": '"',
    "single quote": "'",
    "hash": "#",
    "dollar": "$",
    "percent": "%",
    "and": "&",
    "slash": "/",
    "equal": "=",
    "plus": "+",
    "space": " "
}

reservedWord = {
    "up": "up",
    "down": "down",
    "left": "left",
    "right": "right",
    "home": "home",
    "end": "end",
    "space": "space",
    "tab": "tab",
    "backspace": "backspace",
    "delete": "delete",
    "enter": "enter",
    "paste": "paste",
    "copy": "copy",
    "cut": "cut",
    "undo": "undo",
    "release": "release",
    "page up": "page up",
    "page down": "page down",
    "say": "say",
    "select": "select",
    "select all": "select all",
    "abbreviate": "abbreviate",
    "uppercase": "uppercase",
    "lowercase": "lowercase",
    "expand": "expand",
    "squash": "squash",
    "dash": "dash",
    "underscore": "underscore",
    "dot": "dot",
    "period": "period",
    "minus": "minus",
    "semi-colon": "semi-colon",
    "hyphen": "hyphen",
    "triple": "triple"
}

controlKeyMap = {
    "left": "left",
    "right": "right",
    "up": "up",
    "down": "down",
    "page up": "pgup",
    "page down": "pgdown",
    "home": "home",
    "end": "end",
    "space": "space",
    "(enter|return)": "enter",
    "escape": "escape",
    "tab": "tab"
}

# F1 to F12.
functionKeyMap = {
    'F one': 'f1',
    'F two': 'f2',
    'F three': 'f3',
    'F four': 'f4',
    'F five': 'f5',
    'F six': 'f6',
    'F seven': 'f7',
    'F eight': 'f8',
    'F nine': 'f9',
    'F ten': 'f10',
    'F eleven': 'f11',
    'F twelve': 'f12',
}

pressKeyMap = {}
pressKeyMap.update(letterMap)
pressKeyMap.update(numberMap)
pressKeyMap.update(controlKeyMap)
pressKeyMap.update(functionKeyMap)

#---------------------------------------------------------------------------
# Here we prepare the list of formatting functions from the config file.

# Retrieve text-formatting functions from this module's config file.
#  Each of these functions must have a name that starts with "format_".
format_functions = {}
if namespace:
    for name, function in namespace.items():
     if name.startswith("format_") and callable(function):
        spoken_form = function.__doc__.strip()

        # We wrap generation of the Function action in a function so
        #  that its *function* variable will be local.  Otherwise it
        #  would change during the next iteration of the namespace loop.
        def wrap_function(function):
            def _function(dictation):
                formatted_text = function(dictation)
                Text(formatted_text).execute()
            return Function(_function)

        action = wrap_function(function)
        format_functions[spoken_form] = action


# Here we define the text formatting rule.
# The contents of this rule were built up from the "format_*"
#  functions in this module's config file.
if format_functions:
    class FormatRule(MappingRule):

        mapping  = format_functions
        extras   = [Dictation("dictation")]

else:
    FormatRule = None


#---------------------------------------------------------------------------
# Here we define the keystroke rule.

# This rule maps spoken-forms to actions.  Some of these
#  include special elements like the number with name "n"
#  or the dictation with name "text".  This rule is not
#  exported, but is referenced by other elements later on.
#  It is derived from MappingRule, so that its "value" when
#  processing a recognition will be the right side of the
#  mapping: an action.
# Note that this rule does not execute these actions, it
#  simply returns them when it's value() method is called.
#  For example "up 4" will give the value Key("up:4").
# More information about Key() actions can be found here:
#  http://dragonfly.googlecode.com/svn/trunk/dragonfly/documentation/actionkey.html
class KeystrokeRule(MappingRule):

    exported = False

    mapping  = config.cmd.map
    extras   = [
                IntegerRef("n", 1, 100),
                Dictation("text"),
                Dictation("text2"),
                Choice("char", specialCharMap),
                Choice("modifier1", modifierMap),
                Choice("modifier2", modifierMap),
                Choice("modifierSingle", singleModifierMap),
                #Choice("pressKey", pressKeyMap),
                Choice("formatType", formatMap),
                Choice("abbreviation", abbreviationMap),
                Choice("reservedWord", reservedWord)
                ]
    defaults = {
                "n": 1,
               }
    # Note: when processing a recognition, the *value* of
    #  this rule will be an action object from the right side
    #  of the mapping given above.  This is default behavior
    #  of the MappingRule class' value() method.  It also
    #  substitutes any "%(...)." within the action spec
    #  with the appropriate spoken values.

#---------------------------------------------------------------------------
# Here we create an element which is the sequence of keystrokes.

# First we create an element that references the keystroke rule.
#  Note: when processing a recognition, the *value* of this element
#  will be the value of the referenced rule: an action.
alternatives = []
alternatives.append(RuleRef(rule=KeystrokeRule()))
if FormatRule:
    alternatives.append(RuleRef(rule=FormatRule()))
single_action = Alternative(alternatives)

# Second we create a repetition of keystroke elements.
#  This element will match anywhere between 1 and 16 repetitions
#  of the keystroke elements.  Note that we give this element
#  the name "sequence" so that it can be used as an extra in
#  the rule definition below.
# Note: when processing a recognition, the *value* of this element
#  will be a sequence of the contained elements: a sequence of
#  actions.
sequence = Repetition(single_action, min=1, max=16, name="sequence")


#---------------------------------------------------------------------------
# Here we define the top-level rule which the user can say.

# This is the rule that actually handles recognitions.
#  When a recognition occurs, it's _process_recognition()
#  method will be called.  It receives information about the
#  recognition in the "extras" argument: the sequence of
#  actions and the number of times to repeat them.
class RepeatRule(CompoundRule):

    # Here we define this rule's spoken-form and special elements.
    spec     = "<sequence> [[[and] repeat [that]] <n> times]"
    extras   = [
                sequence,                 # Sequence of actions defined above.
                IntegerRef("n", 1, 100),  # Times to repeat the sequence.
               ]
    defaults = {
                "n": 1,                   # Default repeat count.
               }

    # This method gets called when this rule is recognized.
    # Arguments:
    #  - node -- root node of the recognition parse tree.
    #  - extras -- dict of the "extras" special elements:
    #     . extras["sequence"] gives the sequence of actions.
    #     . extras["n"] gives the repeat count.
    def _process_recognition(self, node, extras):
        sequence = extras["sequence"]   # A sequence of actions.
        count = extras["n"]             # An integer repeat count.
        for i in range(count):
            for action in sequence:
                action.execute()
        release.execute()


#---------------------------------------------------------------------------
# Create and load this module's grammar.

grammar = Grammar("multi edit")   # Create this module's grammar.
grammar.add_rule(RepeatRule())    # Add the top-level rule.
grammar.load()                    # Load the grammar.

# Unload function which will be called at unload time.
def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
