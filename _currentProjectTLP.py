from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Key, Text, Integer, Mimic)

grammar = Grammar("tlp")
noSpaceNoCaps = Mimic("\\no-caps-on") + Mimic("\\no-space-on")

rules = MappingRule(
    name = "tlp",
    mapping = {
      "data import log edit": Text("vim /mnt/c/Users/isaac/Desktop/Debug/log/reliant-sync-log.txt") + Key("enter"),
      "data import log view": Text("tail -f /mnt/c/Users/isaac/Desktop/Debug/log/reliant-sync-log.txt") + Key("enter"),
      "data import log directory": Text("cd /mnt/c/Users/isaac/Desktop/Debug/log/") + Key("enter"),
      "data import install": Text("cp -r /mnt/c/Users/isaac/Documents/SourceCode/Constellation/TLP.Reliant.AgentPortalImporter/bin/Debug/ /mnt/c/Users/isaac/Desktop/") + Key("enter"),
      "constellation source code": Text("cd /mnt/c/Users/isaac/Documents/SourceCode/Constellation/") + Key("enter")
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
