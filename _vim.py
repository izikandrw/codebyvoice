from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Key, Text, Integer, Mimic, Function)

def enable_command_mode():
    Key("escape").execute()

context = AppContext(executable="bash")
grammar = Grammar("bashVim", context=context)

noSpaceNoCaps = Mimic("\\no-caps-on") + Mimic("\\no-space-on")

rules = MappingRule(
    name = "bashVim",
    mapping = {
        "paste [(line|lines)]": Function(enable_command_mode) + Key("p"),
        "delete line": Function(enable_command_mode) + Key("d, d"),
        "doc home": Function(enable_command_mode) + Key("g, g"),
        "find [<text>]": Function(enable_command_mode) + Key("slash") + Text("%(text)s") + Key("enter"),
        "next result": Function(enable_command_mode) + Key("n"),
        "previous result": Function(enable_command_mode) + Key("N"),
        "end find": Function(enable_command_mode) + Text(":noh") + Key("enter"),
        "doc end": Function(enable_command_mode) + Key("s-g"),
        "save": Function(enable_command_mode) + Key("colon, w, enter"),
        "save and exit": Function(enable_command_mode) + Key("colon, w, q, enter"),
        "save as": Key("colon, w, space"),
        "undo": Function(enable_command_mode) + Key("u"),
        "quit": Function(enable_command_mode) + Text(":q") + Key("enter"),
        "quit all": Function(enable_command_mode) + Text(":qa") + Key("enter"),
        "force quit": Function(enable_command_mode) + Text(":q!") + Key("enter"),
        "force quit all": Function(enable_command_mode) + Text(":qa!") + Key("enter"),
        #NERDTree
        "open [file]": Key("o"),
        "tree": Function(enable_command_mode) + Text(":NERDTreeToggle") + Key("enter"),
        "bookmark config": Function(enable_command_mode) + Text(":OpenBookmark config") + Key("enter"),
        "bookmark macros": Function(enable_command_mode) + Text(":OpenBookmark macros") + Key("enter"),
        "bookmark journal": Function(enable_command_mode) + Text(":OpenBookmark journal") + Key("enter"),
        "bookmark memory": Function(enable_command_mode) + Text(":OpenBookmark memory") + Key("enter"),
        "bookmark desktop": Function(enable_command_mode) + Text(":OpenBookmark desktop") + Key("enter"),
        "bookmark log": Function(enable_command_mode) + Text(":OpenBookmark log") + Key("enter"),
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

    extras = [
        Dictation("text"),
        Integer("n", 0, 20000),
      ],
    defaults = {
      "n" : 1
      }
    )

grammar.add_rule(rules)

grammar.load()

def unload():
  global grammar
  if grammar: grammar.unload()
  grammar = None
