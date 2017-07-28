from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Key, Text, Integer, Mimic)

context = AppContext(executable="devenv")
grammar = Grammar("visualstudio", context=context)

noSpaceNoCaps = Mimic("\\no-caps-on") + Mimic("\\no-space-on")

rules = MappingRule(
    name = "visualStudio",
    mapping = {
      "debug" : Key("f5"),
      "stop debug": Key("s-f5"),
      "open file": Key("c-comma"),
      "search": Key("c-f"),
      "solution explorer": Key("ca-l")
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
