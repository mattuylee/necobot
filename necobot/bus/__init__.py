"""Message bus module for decoupled channel-agent communication."""

from necobot.bus.events import InboundMessage, OutboundMessage
from necobot.bus.queue import MessageBus

__all__ = ["MessageBus", "InboundMessage", "OutboundMessage"]
