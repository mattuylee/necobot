"""Slash command routing and built-in handlers."""

from necobot.command.builtin import register_builtin_commands
from necobot.command.router import CommandContext, CommandRouter

__all__ = ["CommandContext", "CommandRouter", "register_builtin_commands"]
