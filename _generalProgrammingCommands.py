from dragonfly import (
    Function,
    MappingRule,
    IntegerRef,
    Grammar,
    Dictation,
    Key,
    Text,
    AppContext
)

grammar = Grammar("general programming commands")

rules = MappingRule(
    mapping={
        "brax": Text("{}") + Key("left")
        },
    extras=[
        IntegerRef("n", 1, 100),
        Dictation("text"),
    ],
    defaults={
        "n": 1
    }
)

grammar.add_rule(rules)
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
