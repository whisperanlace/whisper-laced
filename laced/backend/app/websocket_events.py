# app/Websocket_events.py
from fastapi import FastAPI, WebSocket
from typing import Dict, List

active_connections: Dict[str, List[WebSocket]] = {}

def register_ws_events(app: FastAPI):
    @app.websocket("/ws/{room_id}")
    async def websocket_endpoint(websocket: WebSocket, room_id: str):
        await websocket.accept()
        if room_id not in active_connections:
            active_connections[room_id] = []
        active_connections[room_id].append(websocket)

        try:
            while True:
                data = await websocket.receive_text()
                # Broadcast to all connections in the room
                for conn in active_connections[room_id]:
                    if conn != websocket:
                        await conn.send_text(data)
        except Exception:
            active_connections[room_id].remove(websocket)
            await websocket.close()
