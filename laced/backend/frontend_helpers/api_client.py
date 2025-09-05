# -*- coding: utf-8 -*-
"""
API Client to communicate with Laced backend.
Handles requests, authentication headers, error handling, and retries.
"""

import httpx
from typing import Optional, Dict, Any

class APIClient:
    def __init__(self, base_url: str, token: Optional[str] = None, timeout: int = 10):
        self.base_url = base_url.rstrip("/")
        self.token = token
        self.timeout = timeout
        self.client = httpx.Client(timeout=self.timeout)

    def _headers(self) -> Dict[str, str]:
        headers = {"Content-Type": "application/json"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> httpx.Response:
        try:
            response = self.client.get(f"{self.base_url}{endpoint}", headers=self._headers(), params=params)
            response.raise_for_status()
            return response
        except httpx.HTTPStatusError as exc:
            raise RuntimeError(f"GET request failed: {exc.response.status_code} {exc.response.text}") from exc
        except httpx.RequestError as exc:
            raise RuntimeError(f"GET request error: {str(exc)}") from exc

    def post(self, endpoint: str, data: Optional[Dict[str, Any]] = None, files: Optional[Dict[str, Any]] = None) -> httpx.Response:
        try:
            response = self.client.post(f"{self.base_url}{endpoint}", headers=self._headers(), json=data, files=files)
            response.raise_for_status()
            return response
        except httpx.HTTPStatusError as exc:
            raise RuntimeError(f"POST request failed: {exc.response.status_code} {exc.response.text}") from exc
        except httpx.RequestError as exc:
            raise RuntimeError(f"POST request error: {str(exc)}") from exc
