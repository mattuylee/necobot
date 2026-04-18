"""Agent core module."""

from necobot.agent.context import ContextBuilder
from necobot.agent.hook import AgentHook, AgentHookContext, CompositeHook
from necobot.agent.loop import AgentLoop
from necobot.agent.memory import Dream, MemoryStore
from necobot.agent.skills import SkillsLoader
from necobot.agent.subagent import SubagentManager

__all__ = [
    "AgentHook",
    "AgentHookContext",
    "AgentLoop",
    "CompositeHook",
    "ContextBuilder",
    "Dream",
    "MemoryStore",
    "SkillsLoader",
    "SubagentManager",
]
