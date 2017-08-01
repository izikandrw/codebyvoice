from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Key, Text, Integer, Mimic)
import dragonfly
import natlinkmain
import os
import sys

grammar = Grammar("natlink")

def topy(path):
    if path.endswith == ".pyc":
        return path[:-1]

    return path

def reload_code():
    # Do not reload anything in these directories or their subdirectories.
    dir_reload_blacklist = set(["core"])
    macro_dir = "C:\\NatLink\\NatLink\\MacroSystem"

    # Unload all grammars.
    natlinkmain.unloadEverything()

    # Unload all modules in macro_dir except for those in directories on the
    # blacklist.
    # Consider them in sorted order to try to make things as predictable as possible to ease debugging.
    for name, module in sorted(sys.modules.items()):
        if module and hasattr(module, "__file__"):
            # Some builtin modules only have a name so module is None or
            # do not have a __file__ attribute.  We skip these.
            path = module.__file__

            # Convert .pyc paths to .py paths.
            path = topy(path)

            # Do not unimport this module!  This will cause major problems!
            if (path.startswith(macro_dir) and
                not bool(set(path.split(os.path.sep)) & dir_reload_blacklist)
                and path != topy(os.path.abspath(__file__))):

                print "removing %s from cache" % name

                # Remove the module from the cache so that it will be reloaded
                # the next time # that it is imported.  The paths for packages
                # end with __init__.pyc so this # takes care of them as well.
                del sys.modules[name]

    try:
        # Reload the top-level modules in macro_dir.
        natlinkmain.findAndLoadFiles()
    except Exception as e:
        print "reloading failed: {}".format(e)
    else:
        print "finished reloading"

rules = MappingRule(
    name = "natlink",
    mapping = {
      'reload grammars': dragonfly.Function(reload_code)
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
