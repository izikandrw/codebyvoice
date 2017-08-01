from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Key, Text, Integer, Mimic)

context = AppContext(executable="bash")
grammar = Grammar("bash", context=context)
noSpaceNoCaps = Mimic("\\no-caps-on") + Mimic("\\no-space-on")

rules = MappingRule(
    name = "bash",
    mapping = {
      "edit": Key("i"),
      "normal": Key("escape"),
      "line [<n>]" : Key("escape, %(n)d, g, g"),
      "line [<n>] edit" : Key("escape, %(n)d, g, g, i"),
      "list directory": Text("ls") + Key("enter"),
      "up directory": Text("cd ..") + Key("enter"),
      "change directory": Text("cd "),
      "current directory": Text("pwd") + Key("enter"),
      "quit editor": Key("escape, colon, q, enter"),
      "quit editor force": Key("escape, colon, q, exclamation, enter"),
      "edit <text>": Text("vim %(text)s") + Key("enter"),
      "abort": Key("c-c")
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
