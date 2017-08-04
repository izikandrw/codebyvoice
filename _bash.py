from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Key, Text, Integer, Mimic, Function)

context = AppContext(executable="bash")
grammar = Grammar("bash", context=context)
noSpaceNoCaps = Mimic("\\no-caps-on") + Mimic("\\no-space-on")

rules = MappingRule(
    name = "bash",
    mapping = {
      "abort": Key("c-c"),
      #navigating directories
      "list directory": Text("ls") + Key("enter"),
      "list directory details": Text("ls -l") + Key("enter"),
      "up directory": Text("cd ..") + Key("enter"),
      "change directory": Text("cd"),
      "change directory [<text>]": Text("cd %(text)s") + Key("enter"),
      "current directory": Text("pwd") + Key("enter"),
      "present directory": Text("pwd") + Key("enter"),
      #TMUX
      "Tmax": Text("tmux") + Key("enter"),
      "split vertical": Key("c-b, percent"),
      "split horizontal": Key("c-b, quote"),
      "pane up": Key("c-b, up"),
      "pane down": Key("c-b, down"),
      "pane left": Key("c-b, left"),
      "pane right": Key("c-b, right"),
      "close pane": Key("c-b, x, y, enter"),
      "new window": Key("c-b, c, enter"),
      "next window": Key("c-b, n"),
      "previous window": Key("c-b, p"),
      "close window": Key("c-d")
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
