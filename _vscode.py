#
# This file is part of Dragonfly.
# (c) Copyright 2007, 2008 by Christo Butcher
# Licensed under the LGPL.
#
#   Dragonfly is free software: you can redistribute it and/or modify it 
#   under the terms of the GNU Lesser General Public License as published 
#   by the Free Software Foundation, either version 3 of the License, or 
#   (at your option) any later version.
#
#   Dragonfly is distributed in the hope that it will be useful, but 
#   WITHOUT ANY WARRANTY; without even the implied warranty of 
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU 
#   Lesser General Public License for more details.
#
#   You should have received a copy of the GNU Lesser General Public 
#   License along with Dragonfly.  If not, see 
#   <http://www.gnu.org/licenses/>.
#
#   file based on modified https://github.com/t4ngo/dragonfly-modules/blob/master/command-modules/notepad_example.py
#   vscode version created by Sam @ https://twitter.com/shuff_co

print("vscode grammar loaded")

from dragonfly import (Grammar, AppContext, MappingRule, Dictation,
                       Key, Text, IntegerRef, Integer, ShortIntegerRef)


grammar_context = AppContext(executable="code")
grammar = Grammar("vscode", context=grammar_context)

#----------------------------------------------------------
# general
#----------------------------------------------------------
general = MappingRule(
    name="general",
    mapping={
             "palette":            Key("cs-p"),
             "quick open":         Key("c-p"),
             "new window":         Key("cs-n"),
             "close window":       Key("cs-w"),
             "open settings":      Key("c-comma"),
            },
    extras=[
            Dictation("text"),
           ],
    )
#----------------------------------------------------------
# editing
#----------------------------------------------------------
editing = MappingRule(
    name="editing",
    mapping={
             "cut":                 Key("c-x"),
             "copy":                Key("c-c"),
             "paste":               Key("c-v"),
             "move line up":        Key("a-up"),
             "move line down":      Key("a-down"),
             "copy line up":        Key("sa-up"),
             "copy line down":      Key("sa-down"),
             "delete line":         Key("cs-k"),
             "insert below":        Key("c-enter"),
             "insert above":        Key("cs-enter"),
             "jump bracket":        Key("cs-backslash"),
             "indent":              Key("c-]"),
             "outdent":             Key("c-["),
             "home":                Key("home"),
             "end":                 Key("end"),
             "top":                 Key("c-home"),
             "bottom":              Key("c-end"),
             "line up":             Key("c-up"),
             "line down":           Key("c-down"),
             "scroll up":           Key("a-pgup"),
             "scroll down":         Key("a-pgdown"),
             "fold":                Key("cs-["),
             "unfold":              Key("cs-]"),
             "comment":             Key("c-slash"),
             "block comment":       Key("sa-a"),
            },
    extras=[
            Dictation("text"),
           ],
    )
#----------------------------------------------------------
# navigation
#----------------------------------------------------------
navigation = MappingRule(
    name="navigation",
    mapping={
             "line <num>":       Key("c-g") + Text("%(num)d") + Key("enter"),
             #"go to <text>":      Key("c-p/200") + Text("%(text)s") + Key("enter"),
             "show problems":      Key("cs-m"),
             "show next error":    Key("f8"),
             "show previous error":Key("s-f8"),
             "cursor back":        Key("a-right"),
             "cursor forward":     Key("a-left"),
            },
    extras=[
            IntegerRef("n", 1, 9999),
            Dictation("text"),
            ShortIntegerRef("num", 0, 1000),
           ]
    )
#----------------------------------------------------------
# search and replace
#----------------------------------------------------------
search = MappingRule(
    name="search",
    mapping={
             "find <text>":         Key("c-f") + Text("%(text)s") + Key("enter"),
             "find next":           Key("f3"),
             "find previous":       Key("s-f3"),

            },
    extras=[
            Dictation("text"),
           ],
    )
#----------------------------------------------------------
# multi-cursor and selection
#----------------------------------------------------------
cursor = MappingRule(
    name="cursor-selection",
    mapping={             
             "find all current word":Key("c-f2"),
             "expand select":        Key("sa-right"),
             "shrink select":        Key("sa-left"),
            },
    extras=[
            Dictation("text"),
           ],
    )
#----------------------------------------------------------
# Rich languages editing
#----------------------------------------------------------
richediting = MappingRule(
    name="rich-editing",
    mapping={
            "suggest":              Key("c-space"),
             "hint":                Key("cs-space"),
             "rename word":         Key("f2"),
            },
    extras=[
            Dictation("text"),
           ],
    )
#----------------------------------------------------------
# editor management
#----------------------------------------------------------
editor_management = MappingRule(
    name="editor-management",
    mapping={
             "split editor":        Key("c-backslash"),
             "close editor":        Key("c-f4"),
             "focus one":           Key("c-1"),
             "focus two":           Key("c-2"),
             "focus three":         Key("c-3"),
             "focus four":          Key("c-4"),
            },
    extras=[
            Dictation("text"),
           ],
    )
#----------------------------------------------------------
# file management
#----------------------------------------------------------
file_management = MappingRule(
    name="file-management",
    mapping={
             "open file":           Key("c-o"),
             "new file":            Key("c-n"),
             "save file":           Key("c-s"),
             "save file as":        Key("cs-s"),
             "close":               Key("c-f4"),
             "open next tab":       Key("c-tab"),
             "open previous tab":   Key("cs-tab"),
             "copy file path":      Key("c-k, p"),
             "open directory":      Key("c-k, r"),
             "new instance":        Key("c-k, o"),
             "show explorer":        Key("cs-e"),
            },
    extras=[
            Dictation("text"),
           ],
    )
#----------------------------------------------------------
# display
#----------------------------------------------------------
display = MappingRule(
    name="display",
    mapping={
             "full screen":        Key("f11"),
             "zoom in":            Key("c-equals"),
             "zoom out":           Key("c-minus"),
             "sidebar":            Key("c-b"),
             "show search":        Key("cs-f"),
             "show source control":Key("cs-g"),
             "show debug":         Key("cs-d"),
             "show extensions":    Key("cs-x"),
             "replace in files":   Key("cs-h"),
             "toggle search details":Key("cs-j"),
             "show output panel":    Key("cs-u"),
             "zen mode":             Key("c-k, z"),
            },
    extras=[
            Dictation("text"),
           ],
    )
#----------------------------------------------------------
# debug
#----------------------------------------------------------
debug = MappingRule(
    name="debug",
    mapping={
             "breakpoint":          Key("f9"),
             "run file debug|start debug":Key("f5"),
             "run file|start no debug":Key("c-f5"),
             "stop debug":          Key("s-f5"),
             "step into":           Key("f11"),
             "step out":            Key("s-f11"),
             "step over":           Key("f10"),
             "show bug":         Key("cs-d"),
            },
    extras=[
            Dictation("text"),
           ],
    )
#----------------------------------------------------------
# terminal
#----------------------------------------------------------
terminal = MappingRule(
    name="terminal",
    mapping={
             "show (terminal|term)":        Key("c-backtick"),
             "new terminal":                Key("cs-backtick"),
            },
    extras=[
            Dictation("text"),
           ],
    )

grammar.add_rule(general)
grammar.add_rule(editing)
grammar.add_rule(navigation)
grammar.add_rule(search)
grammar.add_rule(cursor)
grammar.add_rule(editing)
grammar.add_rule(editor_management)
grammar.add_rule(file_management)
grammar.add_rule(display)
grammar.add_rule(debug)
grammar.add_rule(terminal)

grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
