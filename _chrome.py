from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Key, Text, Integer, Mimic)

context = AppContext(executable="chrome")
grammar = Grammar("chrome", context=context)
noSpaceNoCaps = Mimic("\\no-caps-on") + Mimic("\\no-space-on")

rules = MappingRule(
    name = "chrome",
    mapping = {
      "edit": Key("w-a"),
      "reload" : Key("f5"),
      "open tab": Key("c-t"),
      "new tab": Key("c-t"),
      "search tabs": Key("T"),
      "find": Key("c-f"),
      "console": Key("cs-j"),
      "developer tools": Key("cs-i"),
      "close tab": Key("c-w"),
      "escape": Key('escape'),
      "first tab": Key("c-1"),
      "Second tab": Key("c-2"),
      "Third tab": Key("c-3"),
      "Fourth tab": Key("c-4"),
      "Fifth tab": Key("c-5")
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
