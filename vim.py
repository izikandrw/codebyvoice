from dragonfly import Text, Key, Function

def enable_command_mode():
    Key("escape").execute()

map = {
        "tim": Text("vim") + Key("enter"),
        #text manipulation
        "append [text]": Function(enable_command_mode, char="a"),
        "line append [text]": Function(enable_command_mode) + Key("s-a"),
        "line prepend [text]": Function(enable_command_mode) + Key("I"), 
        "insert line before": Function(enable_command_mode) + Key("O"),
        "insert line after": Function(enable_command_mode) + Key("o"),
        "page up": Key("c-b, c-b"),
        "page down": Key("c-f"),
        "duplicate line": Function(enable_command_mode) + Key("y, y, p"),
        "remove character": Function(enable_command_mode) + Key("x"),
        #commands
        "yank": Function(enable_command_mode) + Key("y, y"),
        "yank all": Function(enable_command_mode) + Key("g, g, y, G"),
        "insert": Function(enable_command_mode) + Key("i"),
        #navigation
        "top": Function(enable_command_mode) + Key("H"),
        "mid": Function(enable_command_mode) + Key("M"),
        "bottom": Function(enable_command_mode) + Key("L")
}
