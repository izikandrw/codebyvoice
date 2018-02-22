from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Key, Text, Integer, Mimic, Function)

context = AppContext(executable="ConEmu64")
grammar = Grammar("conEmu", context=context)

noSpaceNoCaps = Mimic("\\no-caps-on") + Mimic("\\no-space-on")

rules = MappingRule(
    name = "bashVim",
    mapping = {
      "first tab": Key("c-1"),
      "second tab": Key("c-2"),
      "third tab": Key("c-3"),
      "fourth tab": Key("c-4"),
      "fifth tab": Key("c-5"),
      "sixth tab": Key("c-5"),
      "seventh tab": Key("c-5"),
      "eigth tab": Key("c-5"),
      "ninth tab": Key("c-5"),
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
