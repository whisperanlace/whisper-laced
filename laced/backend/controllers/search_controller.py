from fastapi import HTTPException
from backend.services.search_service import SearchService

search_service = SearchService()

class SearchController:

    async def search_posts(self, query: str, current_user):
        try:
            return await search_service.search_posts(query, current_user)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    async def search_users(self, query: str, current_user):
        try:
            return await search_service.search_users(query, current_user)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
