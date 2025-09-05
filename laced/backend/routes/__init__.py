# backend/routes/__init__.py

from fastapi import APIRouter

# Import all route modules
from .Auth_route import router as auth_router
from .User_route import router as user_router
from .Generation_route import router as generation_router
from .Toggles_route import router as toggles_router
from .Lora_route import router as lora_router
from .Avatars_route import router as avatars_router
from .Video_route import router as video_router
from .Editor_route import router as editor_router
from .Community_route import router as community_router
from .Uploads_route import router as uploads_router
from .Moderation_route import router as moderation_router
from .Webhooks_route import router as webhooks_router
from .Settings_route import router as settings_router
from .Feedback_route import router as feedback_router
from .Rooms_route import router as rooms_router
from .Messages_route import router as messages_router
from .Reaction_route import router as reaction_router
from .Subscription_route import router as subscription_router
from .Notifications_route import router as notifications_router
from .Admin_route import router as admin_router
from .Collections_route import router as collections_router
from .Exports_route import router as exports_router
from .Premium_route import router as premium_router
from .Api_key_route import router as api_key_router
from .Activity_route import router as activity_router
from .Logs_route import router as logs_router
from .Image_route import router as image_router
from .Comment_route import router as comment_router
from .Post_route import router as post_router
from .Report_route import router as report_router
from .Job_route import router as job_router
from .search_route import router as search_router

# Create main API router
router = APIRouter()

# Include all routes
router.include_router(auth_router, prefix="/auth", tags=["Auth"])
router.include_router(user_router, prefix="/users", tags=["Users"])
router.include_router(generation_router, prefix="/generate", tags=["Generation"])
router.include_router(toggles_router, prefix="/toggles", tags=["Toggles"])
router.include_router(lora_router, prefix="/lora", tags=["Lora"])
router.include_router(avatars_router, prefix="/avatars", tags=["Avatars"])
router.include_router(video_router, prefix="/videos", tags=["Video"])
router.include_router(editor_router, prefix="/editor", tags=["Editor"])
router.include_router(community_router, prefix="/community", tags=["Community"])
router.include_router(uploads_router, prefix="/uploads", tags=["Uploads"])
router.include_router(moderation_router, prefix="/moderation", tags=["Moderation"])
router.include_router(webhooks_router, prefix="/webhooks", tags=["Webhooks"])
router.include_router(settings_router, prefix="/settings", tags=["Settings"])
router.include_router(feedback_router, prefix="/feedback", tags=["Feedback"])
router.include_router(rooms_router, prefix="/rooms", tags=["Rooms"])
router.include_router(messages_router, prefix="/messages", tags=["Messages"])
router.include_router(reaction_router, prefix="/reactions", tags=["Reactions"])
router.include_router(subscription_router, prefix="/subscriptions", tags=["Subscriptions"])
router.include_router(notifications_router, prefix="/notifications", tags=["Notifications"])
router.include_router(admin_router, prefix="/admin", tags=["Admin"])
router.include_router(collections_router, prefix="/collections", tags=["Collections"])
router.include_router(exports_router, prefix="/exports", tags=["Exports"])
router.include_router(premium_router, prefix="/premium", tags=["Premium"])
router.include_router(api_key_router, prefix="/api-keys", tags=["API Keys"])
router.include_router(activity_router, prefix="/activity", tags=["Activity"])
router.include_router(logs_router, prefix="/logs", tags=["Logs"])
router.include_router(image_router, prefix="/images", tags=["Images"])
router.include_router(comment_router, prefix="/comments", tags=["Comments"])
router.include_router(post_router, prefix="/posts", tags=["Posts"])
router.include_router(report_router, prefix="/reports", tags=["Reports"])
router.include_router(job_router, prefix="/jobs", tags=["Jobs"])
router.include_router(search_router, prefix="/search", tags=["Search"])
