from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Key, Text, Integer, Mimic)

context = AppContext(executable="chrome")
grammar = Grammar("chrome", context=context)
noSpaceNoCaps = Mimic("\\no-caps-on") + Mimic("\\no-space-on")

rules = MappingRule(
    name = "chrome",
    mapping = {
      "edit": Key("w-a"),
      "reload" : Key("f5"),
      "refresh": Key("f5"),
      "open tab": Key("c-t"),
      "new tab": Key("c-t"),
      "search tabs": Key("T"),
      "find": Key("c-f"),
      "console": Key("cs-j"),
      "next tool": Key("c-rightbracket"),
      "previous tool": Key("c-leftbracket"),
      "developer tools": Key("cs-i"),
      "close tab": Key("c-w"),
      "escape": Key('escape'),
      "first tab": Key("c-1"),
      "second tab": Key("c-2"),
      "third tab": Key("c-3"),
      "fourth tab": Key("c-4"),
      "fifth tab": Key("c-5"),
      "address": Key("c-l"),
      "continue": Key("f8"),
      "step": Key("f10"),
      "step into": Key("f11"),
      "step out": Key("s-f11"),
      "back to page": Key("f6") + Key("f6") + Key("f6"),
      "back to developer tools": Key("f6")
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
