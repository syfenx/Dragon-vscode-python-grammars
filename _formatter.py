#
# This file is a command-module for Dragonfly.
# (c) Copyright 2008 by Christo Butcher
# Licensed under the LGPL, see <http://www.gnu.org/licenses/>
# based on modified https://github.com/t4ngo/dragonfly-modules/blob/master/command-modules/_multiedit.py
# created by Sam @ https://twitter.com/shuff_co

print("formatter grammar loaded")

from dragonfly import (Grammar, AppContext, MappingRule, Dictation,
                       Key, Text, IntegerRef, Integer, ShortIntegerRef, Function)


grammar_context = AppContext(executable="code")
grammar = Grammar("formatter", context=grammar_context)


# Format: some_words
def format_score(dictation):
    """ score <dictation> """
    text = str(dictation)
    output = "_".join(text.split(" "))
    Text(output).execute()

# Format: some_words()
def format_under_function(dictation):
    """ under func <dictation> """
    text = str(dictation)
    output=  "_".join(text.split(" ")) + "()"
    Text(output).execute()

# Format: SomeWords
def format_studley(dictation):
    """ studley <dictation> """
    text = str(dictation)
    words = [word.capitalize() for word in text.split(" ")]
    output = "".join(words)
    Text(output).execute()

# Format: somewords
def format_one_word(dictation):
    """ [all] one word <dictation> """
    text = str(dictation)
    output = "".join(text.split(" "))
    Text(output).execute()

# Format: SOMEWORDS
def format_upper_one_word(dictation):
    """ one word upper <dictation> """
    text = str(dictation)
    words = [word.upper() for word in text.split(" ")]
    output = "".join(words)
    Text(output).execute()

# Format: SOME_WORDS
def format_upper_score(dictation):
    """ upper score <dictation> """
    text = str(dictation)
    words = [word.upper() for word in text.split(" ")]
    output = "_".join(words)
    Text(output).execute()

# Format: someWords
def camel_case_method(dictation):
    """ camel case <dictation> """
    text = str(dictation)
    words = text.split(" ")
    output = words[0] + "".join(w.capitalize() for w in words[1:])
    Text(output).execute()

#----------------------------------------------------------
# general
#----------------------------------------------------------
formatter = MappingRule(
    name="formatter",
    mapping={
            "score <dictation>":            Function(format_score, dictation="%(dictation)s"),
            "under func <dictation>":       Function(format_under_function, dictation="%(dictation)s"),
            "studley <dictation>":          Function(format_studley, dictation="%(dictation)s"),
             "[all] one word <dictation>":  Function(format_one_word, dictation="%(dictation)s"),
             "one word upper <dictation>":  Function(format_upper_one_word, dictation="%(dictation)s"),
             "upper score <dictation>":     Function(format_upper_score, dictation="%(dictation)s"),
             "camel case <dictation>":     Function(camel_case_method, dictation="%(dictation)s"),
            },
    extras=  [
            Dictation("dictation"),
           ],
    )


grammar.add_rule(formatter)

grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
