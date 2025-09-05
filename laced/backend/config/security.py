# -*- coding: utf-8 -*-
"""
Security middleware setup for FastAPI.
Currently implements CORS (extendable for CSRF, headers).
"""

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

def setup_security(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # 🔒 Restrict to your domains in production
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app
