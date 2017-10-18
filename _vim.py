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

def enable_command_mode():
    Key("escape").execute()

commandMode = MappingRule(
    mapping={
        "tim": Text("vim") + Key("enter"),
        #"append [text]": Function(enable_insert_mode, char="a"),
        #"append [text] (to|at) end [of line]": Function(enable_insert_mode, char="A"),  # @IgnorePep8
        #"insert ([text [before]]|mode)": Function(enable_insert_mode, char="i"),  # @IgnorePep8
        #"insert [text] at beginning [of line]": Function(enable_insert_mode, char="I"),  # @IgnorePep8
        "insert line before": Function(enable_command_mode) + Key("O"),
        "insert line after": Function(enable_command_mode) + Key("o"),
        "page up": Key("c-b, c-b"),
        "page down": Key("c-f"),
        "delete line": Function(enable_command_mode) + Key("d, d"),
        "delete line": Function(enable_command_mode) + Key("d, d"),
        "duplicate line": Function(enable_command_mode) + Key("y, y, p"),
        "paste [(line|lines)]": Function(enable_command_mode) + Key("p"),
        "save": Function(enable_command_mode) + Key("colon, w, enter"),
        "save and exit": Function(enable_command_mode) + Key("colon, w, q, enter"),
        "save as": Key("colon, w, space"),
        "undo": Function(enable_command_mode) + Key("u"),
        "quit": Function(enable_command_mode) + Text(":q") + Key("enter"),
        "quit all": Function(enable_command_mode) + Text(":qa") + Key("enter"),
        "force quit": Function(enable_command_mode) + Text(":q!") + Key("enter"),
        "force quit all": Function(enable_command_mode) + Text(":qa!") + Key("enter"),
        "yank": Function(enable_command_mode) + Key("y, y"),
        "yank all": Function(enable_command_mode) + Key("g, g, y, G"),
        "insert": Function(enable_command_mode) + Key("i"),
        #navigation
        "top": Function(enable_command_mode) + Key("H"),
        "mid": Function(enable_command_mode) + Key("M"),
        "bottom": Function(enable_command_mode) + Key("L"),
        "doc home": Function(enable_command_mode) + Key("g, g"),
        "doc end": Function(enable_command_mode) + Key("s-g"),
        "find [<text>]": Function(enable_command_mode) + Key("slash") + Text("%(text)s") + Key("enter"),
        "next result": Function(enable_command_mode) + Key("n"),
        "previous result": Function(enable_command_mode) + Key("N"),
        "end find": Function(enable_command_mode) + Text(":noh") + Key("enter"),
        #NERDTree
        "open [file]": Key("o"),
        "tree": Function(enable_command_mode) + Text(":NERDTreeToggle") + Key("enter"),
        "bookmark config": Function(enable_command_mode) + Text(":OpenBookmark config") + Key("enter"),
        "bookmark macros": Function(enable_command_mode) + Text(":OpenBookmark macros") + Key("enter"),
        "bookmark journal": Function(enable_command_mode) + Text(":OpenBookmark journal") + Key("enter"),
        "bookmark memory": Function(enable_command_mode) + Text(":OpenBookmark memory") + Key("enter"),
        #windowing
        "[next] window": Function(enable_command_mode) + Key("c-w, w"),
        "[switch] window": Function(enable_command_mode) + Key("c-w, w"),
        #buffers
        "buffer list": Function(enable_command_mode) + Text(":ls") + Key("enter"),
        #tabxs
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

def unload():
    global grammarCommand
    if grammarCommand: grammarCommand.unload()
    grammarCommand = None
