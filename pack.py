#!/usr/bin/env python

# Pack for a-shell, written in Python
# Proundly developed by Heavysnowjakarta
# Under BSD lisence

VERSION = 0

# = Configurations =
# Define and revise your configuration variables here
VIMPATH = "~/Documents/.vim/"

# = Intro =
# For Vim 8, built-in plugin manager is provided. On GitHub, a project
# named `pack` is a third-party plugin manager have been developed to
# manage plugins designed for the built-in manager. With it, we can
# conveniently download plugins from GitHub and update or remove them.
# However, it is written in Rust that can not be used in a-shell.
# Considering a-shell should have an avilable package manager, I remade
# a plugin manager like `pack` in Python.

# = To do list =
#- [x] Deal with arguments simply
#	- [ ] Improve the argument parser
#- [x] Show help texts
#- [ ] Generate and read the pack table (in TOML)
#- [ ] Install packages from GitHub or another Git repository
#- [ ] Update, move and uninstall packages
#- [ ] Configure the packages rapidly

# = Code Structure =
"""
= import modules =
import os
import sys
from rich.console import Console
import argparse

= global variables =
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
parser = argparse.ArgumentParser(description="A package manager for Vim 8, written in Python", add_help=False)

# = Global variables =
PACK_CONFIG = VIMPATH + ".pack-config.toml"
PACK_TABLE = VIMPATH + ".pack-table.toml"

# == Help texts ==
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

help_install=f"""
pack-install
Install new packages or plugins
USAGE:
	pack install [FLAGS] <package>

FLAGS:
	-h, --help			Prints help information
	-o, --opt			Install plugins as opt(ional)
	-v, -V, --version	Prints version information
"""

help_config=f"""
pack-config
Configure/edit the package specific configuration

USAGE:
	pack config [FLAGS] <package>

FLAGS:
	-d, --delete		Delete package configuration
	-h, --help			Prints help information
	-v, -V, --version	Prints version information
"""

help_list="""
pack-list
List installed packages

USAGE:
	pack list [FLAGS]

FLAGS:
	-o, --opt			List optional packages
	-s, --start			List sart packages
	-h, --help			Print help information
	-v, -V, --version	Prints version information
"""

help_move="""
pack move [FLAGS] <package> [CATEGORY]

FLAGS:
	-o, --opt			Make package opt(ional)
	-h, --help			Print help information
	-v, -V, --version	Print version information
"""

help_uninstall="""
pack-uninstall
Uninstall packages/plugins

USAGE:
	pack uninstall [FLAGS] <package>

FLAGS:
	-h, --help			Print help information
	-v, -V, --version	Print version information
"""

help_update="""
pack-update
Update packages

USAGE:
	pack update [FLAGS] [pakage]

FLAGS:
	-h, --help			Print help information
	-s, --skip			Skip packages
	-v, -V, --version	Print version information
"""

# == file texts ==

config_text = """
# This is the configuration file of `pack`.
"""

# = Functions =
# `t` stands for `type`.
def showHelp(t):
	if (t=="general"):
		c.print(help_text)
	if (t=="version"):
		c.print(f"VERSION: {VERSION}")
	if (t=="install"):
		c.print(help_install)
	if (t=="config"):
		c.print(help_config)
	if (t=="list"):
		c.print(help_list)
	if (t=="uninstall"):
		c.print(help_uninstall)
	if (t=="update"):
		c.print(help_update)
	if (t=="move"):
		c.print(help_move)

def dealWithArgs():
	# parser = argparser.ArgumentParser(description="A package manager for Vim 8, written in Python", add_help=False)
	parser.add_argument("command", choices=["install", "update", "uninstall", "move", "list", "config"])
	parser.add_argument("-h", "--help", action="store_true")
	parser.add_argument("-v", "--version", action="store_true")

	args = parser.parse_args()
	return args

"""
# Read or generate and deal with the configuration file
def config():
	if (os.path.isfile(PACK_CONFIG)):
		pass
	else:
		c.print("There is not a configuration file yet. Generating `.vim/mpack-config.toml` for you...")
"""

###

def main():
	# Deal with arguments
	# Show help and version info
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
		if (args.command=="install"):
			showHelp("install")
		elif (args.command == "list"):
			showHelp("list")
		elif (args.command == "config"):
			showHelp("config")
		elif (args.command == "move"):
			showHelp("move")
		elif (args.command == "uninstall"):
			showHelp("uninstall")
		elif (args.command == "update"):
			showHelp("update")
		else:
			showHelp("general")
		exit(0)
	# Read the configuration file
	config()

######

if __name__=='__main__':
	main()
