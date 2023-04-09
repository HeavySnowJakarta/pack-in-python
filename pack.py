#!/bin/python

# Pack for a-shell
# Proundly developed by Heavysnowjakarta
# Under BSD lisence

VERSION = 0

# = Intro =
# For Vim 8, built-in plugin manager is provided. On GitHub, a project
# named `pack` is a third-party plugin manager have been developed to
# manage plugins designed for the built-in manager. With it, we can
# conveniently download plugins from GitHub and update or remove them.
# However, it is written in Rust that can not be used in a-shell.
# Considering a-shell should have a avilable package manager, I remade
# a plugin manager like `pack` in Python.

# = To do list =


# = Code Structure =
"""
= import modules =
import os
import sys
from rich.console import Console
import argparse

= help texts =

= functions =
def showHelp(t) # t stands for type
def dealWithArgs()
"""

# = Import modules =

import os
import sys

# == Rich ==
# This script uses `rich` to generate nice outputs
from rich.console import Console

# To simplify the code, I use `c` to refer rich console. Attention this while
# reading the following codes.
c = Console()

# == Argparse ==
# This script uses `argparse` to deal with arguments
import argparse

# = Help texts =
help_text=f"""
pack

Version: {VERSION}

A package manager for Vim 8+, written in Python

USAGE: pack <SUBCOMMANDS> [FLAGS]

SUBCOMMANDS:
	list		List all packages installed
	install		Install new packages
	update		Update packages
	uninstall	Remove installed packages
	config		Open the configure file of the package

FLAGS:
	-h, --help		Print the help text
	-v, --version	Print the version
"""
# = Functions =
# `t` stands for `type`.
def showHelp(t):
	if (t="general"):
		c.print(help_text)
	if (t="version"):
		c.print(f"VERSION: {VERSION}")

def dealWithArgs():
	parser = argparser.ArgumentParser(description="A package manager for Vim 8, written in Python", add_help=False)
	parser = add_argument("command", choices=["install", "update", "uninstall", "move", "list", "config"])
	parser = add_argument("-h", "--help", action="store_true")
	parser = add_argument("-v", "--version", action="store_true")

	args = parser.parse_args()
	return args

###

def main():
	# Deal with arguments
	args = dealWithArgs()
	if (args.version):
		showHelp("version")
		exit(0)
	if (not args.command and not args.help):
		showHelp("general")
		exit(1)
	if (args.help):
		if (not args.command):
			showHelp("general")
			exit(0)
		# TODO
		"""else if (args.command = "install"):
			showHelp("install")"""

######

if __name__=='__main__':
	main()
