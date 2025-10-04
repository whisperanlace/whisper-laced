$env:PYTHONPATH            = 'D:\whisper-laced'
$env:CELERY_BROKER_URL     = 'redis://127.0.0.1:6379/0'
$env:CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/1'
$env:BEARER_TOKEN          = 'SUPER_SECRET_TOKEN_123'
Set-Location 'D:\whisper-laced'
& 'D:\whisper-laced\venv\Scripts\python.exe' -m uvicorn backend.app.main:app --host 127.0.0.1 --port 5000
