## PEP: Python Enhancement Proposals
# Collection of guidelines, practices, descriptions of (new) features, processes, mechanisms and important information.
# Statuses: Draft -> Accepted -> Final -> Active. (contains ALL PEPs).
# PEP champion: A guy who write a PEP proposal and put it up for discussion trying to get a community consensus over it.
# 3 types of PEPS:
#  - Standard Track (new features and implementation)
#  - Informational (design issues, guidelines and information)
#  - Process (various processes that revolve around Python)

## PEP 1: PEP Purpose and Guidelines


## PEP 8: Style Guide for Python Code (coding conventions and best practices)
# PEP 8 guidelines are a set of rules for formatting Python code to enhance readability and maintainability.
# pycodestyle will check python style guide.
# Code Layout: 4 spaces per indentation levels, don't use tabs.
# Continuation lines: 80/120 chars max (disagree on indentation). 79/72 (code/comment).
# Blank Lines:
#  - two blank lines to surround top-level function and class definitions.
#  - a single blank line to surround method definitions inside a class.
#  - blank lines in functions in order to indicate logical sections (ex: after a 'for', before a 'return').
# Default encodings: ASCII-only, english words.
# String quotes, whitespace, and trailing commas: Either ' or " (avoiding '\'), no useless whitespaces (even after trailing commas).
# Comments: # followed by space, full sentences, not too much comments. Documentation strings (PEP257) start and fininish with """
# Naming conventions:
#  - Capitalize all the letters that make up the acronym (disagree).
#  - A name that starts with a single leading underscore indicates a weak "internal use".
#  - A single trailing underscore is used by convention in order to avoid any conflicts with Python keywords
#  - A name that starts with a double leading underscore is used for class attributes where it invokes name mangling.
#  - A name that starts and ends with a double underscore is used for "magic" objects and attributes.
#  - Variables, functions, methods, modules: lower snake_case.
#  - Packages: lower strings, no space separator.
#  - Constant: upper SNAKE_CASE
#  - Class, exception, type variable: Pascal Case.
# Programming recommendations
#  - Compare with None/booleans using 'is' / 'is not', don't use 'not is'
#  - Use string methods rather than import string module.
#  - Break lines before binary operators.
#  - Imports: At the beginning of the script, on separated lines (except from <a> import <b>,<c>). No wildcard (*).
#  - Imports order: Standard libray, Related third party, Local application/library-specific.


## PEP 20: The Zen of Python (design principles)
# Collection of 19 aphorisms, wrote by Tim Peters.
import this
# Beautiful is better than ugly: Code readability, style rules (ex: 79 char max line length).
# Explicit is better than implicit: Code verbosity (ex: named attributes).
# Simple is better than complex: Adjust tools to project specificity, divide problems into smaller/simpler parts.
# Complex is better than complicated: Divide complicated code into well-separated parts, avoid lack of clarity and miscomprehension.
# Flat is better than nested: Avoid too many levels of code nesting (3 max...), flat code is easier to understand and maintain.
# Sparse is better than dense: Code readability, reduce density.
# Readability counts: Code readability, (ex: meaningful names to variables and functions, comments).
# Special cases aren't special enough to break the rules: Keep discipline, consistency, and compliance with standards and conventions.
# Although, practicality beats purity: Break the rules if there is a good reason for it (ex: keep standards, improve performance).
# Errors should never pass silently: Don't ignore errors, unless explicitly (manage all errors cases explicitly).
# In the face of ambiguity, refuse the temptation to guess: Avoid writing ambiguous code, comments, always write tests.
# There should be one obvious way to do it: Agree on the best way to achieve a particular goal, each 'entity' should have a single responsibility.
# Now is better than never: Fix stuff now (avoid todo, raise DeprecationWarning).
# If the implementation is hard to explain, it's a bad idea: keep things simple.
# Namespaces are one honking great idea: Avoid conflicts with already existing names, don't use 'global' keyword.


## PEP 257: Docstring Conventions
# Documentation strings are used to provide information about the functionality in a prescriptive way.
# Becomes the __doc__ special attribute of that object, and appear in the help() function.
# Docstrings => document, comments => increase code's readability.
# All public modules, functions, classes, and methods that are exported by a given module should have docstrings.
# For packages, should write docstring in the module docstring of the __init__.py file.
# Two types:
#  - Attribute docstrings (first statement of a module / class / __init__ class method), extracted by tools such as Docutils.
#  - Additional docstrings (located immediately after another docstring, see PEP-287)
# How to docstring :
#  - """Always starts with upper case and end with a period, imperative form (Do this, take that...)."""
#  - Blank line right after when in a class.
#  - When multiline, summary on the same line of opening marker, followed by a blank line. Closing marker on a new line. See exampleMultilineDocstrings.py.
#  - Sphinx: use docstrings to generate documentation (html...).
# Document a prj: readme, examples.py, license, how to contribute.
# Linters (Flake8, Pylint, Pyflakes) and fixers (Black, YAPF, autopep8)


## PEP 484: Type hinting
# def hello(name: str) -> str:
# Not mandatory but helps to document the code.
# Only used for code readability, ignored on code execution.


