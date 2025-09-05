# conversation/context_manager.py

# In-memory user context store (can be swapped for persistent storage)
USER_CONTEXTS = {}

def get_context(user_id: str):
    """Retrieve user context."""
    return USER_CONTEXTS.get(user_id, {"history": []})

def update_context(user_id: str, user_message: str, bot_response: str):
    """Update user context with latest message/response."""
    context = USER_CONTEXTS.setdefault(user_id, {"history": []})
    context["history"].append({"user": user_message, "bot": bot_response})

def reset_context(user_id: str):
    """Clear a user's conversation context."""
    if user_id in USER_CONTEXTS:
        USER_CONTEXTS[user_id]["history"] = []
