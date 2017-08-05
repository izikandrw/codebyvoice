from dragonfly import (
    Function,
    MappingRule,
    IntegerRef,
    Grammar,
    Dictation,
    Key,
    Text,
    AppContext
)

context = AppContext(executable="bash")
grammarCommand = Grammar("Vim command grammar", context=context)

context = AppContext(executable="bash")
grammarInsert = Grammar("Vim insert grammar", context=context)

def enable_insert_mode(char):
    global grammarCommand
    print("in enable_insert_mode")
    global grammarInsert
    grammarCommand.disable()
    grammarInsert.enable()
    Key(char).execute()

def enable_command_mode():
    global grammarCommand
    global grammarInsert
    grammarCommand.enable()
    grammarInsert.disable()
    Key("escape").execute()

commandMode = MappingRule(
    mapping={
        "tim": Text("vim") + Key("enter"),
        "append [text]": Function(enable_insert_mode, char="a"),
        "append [text] (to|at) end [of line]": Function(enable_insert_mode, char="A"),  # @IgnorePep8
        "copy [(line|lines)]": Key("y, y"),
        "insert ([text [before]]|mode)": Function(enable_insert_mode, char="i"),  # @IgnorePep8
        "insert [text] at beginning [of line]": Function(enable_insert_mode, char="I"),  # @IgnorePep8
        "insert line before": Function(enable_insert_mode, char="O"),
        "insert line after": Function(enable_insert_mode, char="o"),
        "page up": Key("c-b, c-b"),
        "page down": Key("c-f"),
        "paste [(line|lines)]": Key("p"),
        "save": Key("colon, w, enter"),
        "save and exit": Key("colon, x, space"),
        "save as": Key("colon, w, space"),
        "undo": Function(enable_command_mode) + Key("u"),
        "cut [(line|lines)]": Key("d, d"),
        "quit": Function(enable_command_mode) + Text(":q") + Key("enter"),
        "force quit": Function(enable_command_mode) + Text(":q!") + Key("enter"),
        #Navigation
        "top": Function(enable_command_mode) + Key("H"),
        "mid": Function(enable_command_mode) + Key("M"),
        "bottom": Function(enable_command_mode) + Key("L"),
        #NERDTree
        "open [file]": Key("o"),
        "tree": Function(enable_command_mode) + Text(":NERDTreeToggle") + Key("enter"),
        "bookmark config": Function(enable_command_mode) + Text(":OpenBookmark config") + Key("enter"),
        "bookmark macros": Function(enable_command_mode) + Text(":OpenBookmark macros") + Key("enter"),
        "bookmark journal": Function(enable_command_mode) + Text(":OpenBookmark journal") + Key("enter"),
        #windowing
        "[next] window": Function(enable_command_mode) + Key("c-w, w"),
        "[switch] window": Function(enable_command_mode) + Key("c-w, w"),
        #buffers
        "buffer list": Function(enable_command_mode) + Text(":ls") + Key("enter"),
        #tabs
        "next tab": Function(enable_command_mode) + Key("g, t"),
        "previous tab": Function(enable_command_mode) + Key("g, T"),
        "close tab": Function(enable_command_mode) + Text(":tabclose") + Key("enter")
        },
    extras=[
        IntegerRef("n", 1, 100),
        Dictation("text"),
    ],
    defaults={
        "n": 1
    }
)

grammarCommand.add_rule(commandMode)
grammarCommand.load()

insertMode = MappingRule(
    mapping={
        "(command [mode]|press escape)": Function(enable_command_mode),
    },
    extras=[
        IntegerRef("n", 1, 100),
        Dictation("text"),
    ],
    defaults={
        "n": 1
    }
)

grammarInsert.add_rule(insertMode)
grammarInsert.load()

def unload():
    global grammarCommand
    global grammarInsert
    if grammarCommand: grammarCommand.unload()
    grammarCommand = None
    if grammarInsert: grammarInsert.unload()
