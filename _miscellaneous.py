from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Key, Text, Integer, Mimic)

grammar = Grammar("misc")

rules = MappingRule(
    name = "misc",
    mapping = {
      "personal email": Text("izikandrw@gmail.com"),
      "business email": Text("isaac.stennett@goftwaresolutions.com"),
      "daily script": Text("todoist.com"),
      "desktop": Text("cd /mnt/c/Users/isaac/Desktop/") + Key("enter"),
      "journal": Text("cd /mnt/c/Users/isaac/Google\ Drive/Information/") + Key("enter"),
      "today": Text("/mnt/c/Users/isaac/Google\ Drive/shellScripts/makeNewJournalEntry.sh") + Key("enter"),
      "source code": Text("cd /mnt/c/Users/isaac/Documents/SourceCode") + Key("enter"),
      "macros": Text("cd /mnt/c/NatLink/NatLink/MacroSystem") + Key("enter"),
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
