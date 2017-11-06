from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Key, Text, Integer, Mimic)

context = AppContext(executable="devenv")
grammar = Grammar("visualstudio", context=context)

noSpaceNoCaps = Mimic("\\no-caps-on") + Mimic("\\no-space-on")

rules = MappingRule(
    name = "visualStudio",
    mapping = {
      "[start] debug" : Key("f5"),
      "stop debug": Key("s-f5"),
      "open file": Key("c-comma"),
      # search commands
      "find file": Key("c-comma"),
      "search": Key("c-f"),
      "all refs": Key("s-f12"),
      # debug commands
      "continue": Key("f5"),
      "step": Key("f10"),
      "step into": Key("f11"),
      "step out": Key("s-f11"),
      "breakpoint": Key("f9"),
      "line number": Key("c-g"),
      "comment": Key("c-k") + Key("c-c"),
      "uncomment": Key("c-k") + Key("c-u"),
      # tool windows
      "immediate": Key("ca-i"),
      "power shell": Key("cs-backslash"),
      "[solution] explorer": Key("ca-l"),
      "server explorer": Key("ca-s"),
      "call stack": Key("ca-c"),
      "next pane": Key("a-f6"),
      "close tool": Key("s-escape"),
      "pending": Key("c-k") + Key("c"),
      "rebuild": Key("cs-r"),
      "code": Key("f7"),
      #window navigation
      "next tab": Key("c-k") + Key("c-n"),
      "previous tab": Key("c-k") + Key("c-p"),
      #editing commands
      "delete line": Key("cs-l"),
      "delete until end": Key("cs-w"),
      "close all": Key("cs-o"),
      "collapse": Key("c-minus"),
      "call stack": Key("ca-c"),
      "history": Key("cs-h"),
      "execute [sql]": Key("cs-e"),
      "whitespace": Key("c-r, c-w")
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
