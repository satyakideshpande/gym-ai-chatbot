"""
Conversation Memory Module for Gym Chatbot

This module handles storing and managing conversation history between the user and the assistant.
It maintains an in-memory store of recent exchanges to provide context for the LLM.

Key Features:
- Stores conversation history as user-assistant exchanges (pairs)
- Maintains only the last 4 exchanges to keep memory efficient
- Provides methods to add exchanges, retrieve history, and format for LLM prompts
- Completely in-memory implementation (no external storage)
"""

from typing import List, Dict


class ConversationMemory:
    """
    In-memory conversation history manager for the gym chatbot.
    
    This class maintains a rolling window of the last 4 user-assistant exchanges.
    When a new exchange is added and the limit is exceeded, the oldest exchange is removed.
    """
    
    def __init__(self, max_exchanges: int = 4):
        """
        Initialize the conversation memory.
        
        Args:
            max_exchanges (int): Maximum number of exchanges to keep in memory. Default is 4.
        """
        # List to store conversation exchanges
        # Each exchange is a dict with "user" and "assistant" keys
        self.history: List[Dict[str, str]] = []
        self.max_exchanges = max_exchanges
    
    def add_exchange(self, user_message: str, assistant_response: str) -> None:
        """
        Add a new user-assistant exchange to the conversation history.
        
        If the history exceeds the maximum number of exchanges, the oldest exchange
        is automatically removed.
        
        Args:
            user_message (str): The user's question or message.
            assistant_response (str): The assistant's response to the user.
        
        Returns:
            None
        
        Example:
            memory.add_exchange(
                "What is the annual membership fee?",
                "The annual membership fee is 14000 INR."
            )
        """
        # Create a new exchange dictionary
        exchange = {
            "user": user_message,
            "assistant": assistant_response
        }
        
        # Add the exchange to history
        self.history.append(exchange)
        
        # Remove the oldest exchange if we exceed the maximum limit
        if len(self.history) > self.max_exchanges:
            self.history.pop(0)  # Remove the first (oldest) exchange
    
    def get_recent_history(self) -> List[Dict[str, str]]:
        """
        Retrieve the current conversation history.
        
        Returns a list of recent exchanges, each containing "user" and "assistant" keys.
        
        Returns:
            List[Dict[str, str]]: List of exchanges. Each exchange is a dictionary with
                                 "user" and "assistant" keys.
        
        Example:
            history = memory.get_recent_history()
            # Returns: [
            #     {"user": "...", "assistant": "..."},
            #     {"user": "...", "assistant": "..."}
            # ]
        """
        return self.history.copy()  # Return a copy to prevent external modifications
    
    def format_history_for_prompt(self) -> str:
        """
        Format the conversation history as a text string suitable for LLM prompts.
        
        Converts the stored exchanges into a readable format that can be directly
        inserted into the LLM system prompt or context window.
        
        Format:
            User: [user message]
            Assistant: [assistant response]
            
            User: [user message]
            Assistant: [assistant response]
        
        Returns:
            str: Formatted conversation history. Returns empty string if no history exists.
        
        Example:
            formatted = memory.format_history_for_prompt()
            # Returns:
            # User: What is the annual membership fee?
            # Assistant: The annual membership fee is 14000 INR.
            #
            # User: Is there any discount?
            # Assistant: Yes, up to 2000 INR discount is available.
        """
        # If no history exists, return an empty string
        if not self.history:
            return ""
        
        # Build the formatted string
        formatted_parts = []
        for exchange in self.history:
            user_part = f"User: {exchange['user']}"
            assistant_part = f"Assistant: {exchange['assistant']}"
            formatted_parts.append(f"{user_part}\n{assistant_part}")
        
        # Join all exchanges with blank lines between them
        return "\n\n".join(formatted_parts)
    
    def clear_history(self) -> None:
        """
        Clear all conversation history.
        
        This method removes all stored exchanges and resets the memory.
        Useful for starting a fresh conversation or for testing purposes.
        
        Returns:
            None
        """
        self.history.clear()
    
    def get_history_length(self) -> int:
        """
        Get the current number of exchanges in memory.
        
        Returns:
            int: Number of exchanges currently stored.
        """
        return len(self.history)


# Create a global instance of ConversationMemory for use throughout the application
conversation_memory = ConversationMemory(max_exchanges=4)
