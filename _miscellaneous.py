from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Key, Text, Integer, Mimic)

grammar = Grammar("misc")

rules = MappingRule(
    name = "misc",
    mapping = {
      "personal email": Text("izikandrw@gmail.com"),
      "business email": Text("isaac.stennett@goftwaresolutions.com"),
      "daily script": Text("todoist.com")
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
