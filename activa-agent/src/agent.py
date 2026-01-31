from a2a.types import Message, TaskState
from a2a.utils import get_message_text, new_agent_text_message
from a2a.server.tasks import TaskUpdater

class Agent:
    """A simple Activa agent that participates in tasks/debates."""

    async def run(self, message: Message, updater: TaskUpdater) -> None:
        """
        Implement the agent logic.
        This simple agent just acknowledges the message and provides a generic response.
        """
        input_text = get_message_text(message)

        # Acknowledge the request
        await updater.update_status(
            TaskState.working,
            new_agent_text_message(f"Processing input: '{input_text[:50]}...'")
        )

        # Basic response logic
        # In a real agent, you might call an LLM here.
        response_text = (
            f"As an Activa (purple) agent, I've analyzed your message: '{input_text}'.\n\n"
            "My perspective is that collaboration between human and artificial intelligence "
            "is the key to unlocking future potential. We should focus on augmentative "
            "capabilities rather than just replacement."
        )

        # Complete the task with the final response
        await updater.complete(new_agent_text_message(response_text))
