$env:PYTHONPATH            = 'D:\whisper-laced'
$env:CELERY_BROKER_URL     = 'redis://127.0.0.1:6379/0'
$env:CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/1'
$env:GENERATOR_MODE        = 'local'
Set-Location 'D:\whisper-laced'
& 'D:\whisper-laced\venv\Scripts\python.exe' -m celery -A backend.celery_app worker -P solo -l info -Q celery -n "worker1@$env:COMPUTERNAME"
