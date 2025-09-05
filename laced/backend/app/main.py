from fastapi import Request
from . import app
from .routes import (
    auth, users, generation, toggles, loras, avatars, video, editor, community,
    uploads, moderation, webhooks, settings, feedback, rooms, messages, reaction,
    subscriptions, notifications, admin, collections, exports, premium, Api_keys, activity, logs
)
from .tasks import start_background_tasks
from .Event_hooks import register_event_hooks

# Include all routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(generation.router, prefix="/generate", tags=["generation"])
app.include_router(toggles.router, prefix="/toggles", tags=["toggles"])
app.include_router(loras.router, prefix="/loras", tags=["loras"])
app.include_router(avatars.router, prefix="/avatars", tags=["avatars"])
app.include_router(video.router, prefix="/video", tags=["video"])
app.include_router(editor.router, prefix="/editor", tags=["editor"])
app.include_router(community.router, prefix="/community", tags=["community"])
app.include_router(uploads.router, prefix="/uploads", tags=["uploads"])
app.include_router(moderation.router, prefix="/moderation", tags=["moderation"])
app.include_router(webhooks.router, prefix="/webhooks", tags=["webhooks"])
app.include_router(settings.router, prefix="/settings", tags=["settings"])
app.include_router(feedback.router, prefix="/feedback", tags=["feedback"])
app.include_router(rooms.router, prefix="/rooms", tags=["rooms"])
app.include_router(messages.router, prefix="/messages", tags=["messages"])
app.include_router(reaction.router, prefix="/reactions", tags=["reactions"])
app.include_router(subscriptions.router, prefix="/subscriptions", tags=["subscriptions"])
app.include_router(notifications.router, prefix="/notifications", tags=["notifications"])
app.include_router(admin.router, prefix="/admin", tags=["admin"])
app.include_router(collections.router, prefix="/collections", tags=["collections"])
app.include_router(exports.router, prefix="/exports", tags=["exports"])
app.include_router(premium.router, prefix="/premium", tags=["premium"])
app.include_router(Api_keys.router, prefix="/api-keys", tags=["api-keys"])
app.include_router(activity.router, prefix="/activity", tags=["activity"])
app.include_router(logs.router, prefix="/logs", tags=["logs"])

# Startup event
@app.on_event("startup")
async def startup_event():
    await start_background_tasks()
    await register_event_hooks()

# Shutdown event
@app.on_event("shutdown")
async def shutdown_event():
    # Perform cleanup, flush caches, close DB connections if needed
    pass
