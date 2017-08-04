from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Key, Text, Integer, Mimic)

grammar = Grammar("globalcommands")
noSpaceNoCaps = Mimic("\\no-caps-on") + Mimic("\\no-space-on")

rules = MappingRule(
    name = "globalcommands",
    mapping = {
      "switch" : Key("a-tab"),
      "find" : Key("c-f"),
      "save" : Key("c-s"),
      "close tab": Key("c-w"),
      "new tab": Key("c-t"),
      "open" : Key("c-o"),
      "open file": Key("c-o"),
      "select all": Key("c-a")
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
