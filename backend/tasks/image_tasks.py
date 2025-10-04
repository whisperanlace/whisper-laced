from celery import shared_task

@shared_task(bind=True, name="stub.ok")
def stub_ok(self, **kw):
    # minimal task so Celery can import the module without blowing up
    return {"ok": True, "module": __name__}
