from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Key, Text, Integer, Mimic)

grammar = Grammar("git")

rules = MappingRule(
    name = "git",
    mapping = {
      "get status": Text("git status") + Key("enter"),
      "get add all": Text("git add .") + Key("enter"),
      "get diff all": Text("git diff *") + Key("enter"),
      "get commit <text>": Text("git commit -m \"%(text)s\""),
      "get push": Text("git push") + Key("enter")
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
