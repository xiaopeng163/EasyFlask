# Copyright 2015-2018 Cisco Systems, Inc.
# All rights reserved.


"""CLI Basic
"""
import os
import sys

import click

CONTEXT_SETTINGS = dict(auto_envvar_prefix='NETSEEN')


class Context(object):

    def __init__(self):
        self.verbose = False
        self.home = os.getcwd()

    def log(self, msg, *args):
        """Logs a message to stderr."""
        if args:
            msg %= args
        click.echo(msg, file=sys.stderr)

    def vlog(self, msg, *args):
        """Logs a message to stderr only if verbose is enabled."""
        if self.verbose:
            self.log(msg, *args)


pass_context = click.make_pass_decorator(Context, ensure=True)
cmd_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'commands'))


class NETCLI(click.MultiCommand):
    """basic class for {{cookiecutter.module_name}} cli
    """
    def list_commands(self, ctx):
        """command list
        """
        cmds = []
        for filename in os.listdir(cmd_folder):
            if filename.endswith('.py') and \
               filename.startswith('cmd_'):
                cmds.append(filename[4:-3])
        cmds.sort()
        return cmds

    def get_command(self, ctx, name):
        """get command from source file
        """
        try:
            if sys.version_info[0] == 2:
                name = name.encode('ascii', 'replace')
            mod = __import__('{{cookiecutter.module_name}}.cli.commands.cmd_' + name,
                             None, None, ['cli'])
        except ImportError:
            return
        return mod.cli


@click.command(cls=NETCLI, context_settings=CONTEXT_SETTINGS)
@click.option('-v', '--verbose', is_flag=True,
              help='show debug message.')
@pass_context
def cli(ctx, verbose):
    """{{cookiecutter.module_name}} Command Line Interface"""
    ctx.verbose = verbose
