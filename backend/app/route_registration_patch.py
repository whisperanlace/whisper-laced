from backend.routes import (
    post_routes,
    comment_routes,
    reaction_routes,
    invite_routes,
    community_routes,
    lounge_routes,
    motion_routes,
)

app.include_router(post_routes.router, prefix="/post", tags=["Post"])
app.include_router(comment_routes.router, prefix="/comment", tags=["Comment"])
app.include_router(reaction_routes.router, prefix="/reaction", tags=["Reaction"])
app.include_router(invite_routes.router, prefix="/invite", tags=["Invite"])
app.include_router(community_routes.router, prefix="/community", tags=["Community"])
app.include_router(lounge_routes.router, prefix="/lounge", tags=["Lounge"])
app.include_router(motion_routes.router, prefix="/motion", tags=["Motion"])
