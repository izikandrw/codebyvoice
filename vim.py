from dragonfly import Text, Key, Function  
def enable_command_mode():
    Key("escape").execute()  

map = {
        "tim": Text("vim") + Key("enter"),
        #text manipulation
        "append [text]": Function(enable_command_mode, char="a"),
        "line append [text]": Function(enable_command_mode) + Key("s-a"),
        "line prepend [text]": Function(enable_command_mode) + Key("I"),
        "insert line above": Function(enable_command_mode) + Key("O"),
        "insert line below": Function(enable_command_mode) + Key("o"),
        "delete line": Function(enable_command_mode) + Key("d, d"),
        "delete word": Function(enable_command_mode) + Key("d, w"),
        "duplicate line": Function(enable_command_mode) + Key("y, y, p"),
        "remove character": Function(enable_command_mode) + Key("x"),
        #commands
        "yank": Function(enable_command_mode) + Key("y, y"),
        "shove": Function(enable_command_mode) + Key("p"),
        "yank all": Function(enable_command_mode) + Key("g, g, y, G"),
        "insert": Function(enable_command_mode) + Key("i"),
        #navigation
        "top": Function(enable_command_mode) + Key("H"),
        "mid": Function(enable_command_mode) + Key("M"),
        "bottom": Function(enable_command_mode) + Key("L"),
        "doc home": Function(enable_command_mode) + Key("g, g"),
        "doc end": Function(enable_command_mode) + Key("s-g"),
  }
