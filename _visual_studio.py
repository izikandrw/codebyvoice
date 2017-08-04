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
      "find file": Key("c-comma"),
      "search": Key("c-f"),
      "solution explorer": Key("ca-l"),
      "continue": Key("f5"),
      "step": Key("f10"),
      "step into": Key("f11"),
      "step out": Key("s-f11"),
      "breakpoint": Key("f9"),
      "line number": Key("c-g"),
      "comment": Key("c-k") + Key("c-c"),
      "uncomment": Key("c-k") + Key("c-u"),
      "immediate": Key("ca-i"),
      "call stack": Key("ca-c"),
      "next pane": Key("a-f6"),
      "pending": Key("c-k") + Key("c"),
      "rebuild": Key("cs-r"),
      "delete line": Key("cs-l"),
      "delete until end": Key("cs-w"),
      "close all": Key("cs-o"),
      "collapse": Key("c-minus")
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
