# Current Issue:
current issue I have is using Docker.
I have built Docker image and ran it without any issue,
but when I check Docker Desktop, it is not running.
When I click on the image file and try to run it,
it just exits right away.

Error message from Docker is below:

```[2022-08-25 00:23:01 +0000] [1] [INFO] Starting gunicorn 20.0.4
[2022-08-25 00:23:01 +0000] [1] [INFO] Listening at: http://0.0.0.0:5000 (1)
[2022-08-25 00:23:01 +0000] [1] [INFO] Using worker: sync
[2022-08-25 00:23:01 +0000] [8] [INFO] Booting worker with pid: 8
[2022-08-25 00:23:01 +0000] [8] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/usr/local/lib/python3.8/site-packages/gunicorn/arbiter.py", line 583, in spawn_worker
    worker.init_process()
  File "/usr/local/lib/python3.8/site-packages/gunicorn/workers/base.py", line 119, in init_process
    self.load_wsgi()
  File "/usr/local/lib/python3.8/site-packages/gunicorn/workers/base.py", line 144, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/usr/local/lib/python3.8/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/usr/local/lib/python3.8/site-packages/gunicorn/app/wsgiapp.py", line 49, in load
    return self.load_wsgiapp()
  File "/usr/local/lib/python3.8/site-packages/gunicorn/app/wsgiapp.py", line 39, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/usr/local/lib/python3.8/site-packages/gunicorn/util.py", line 358, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.8/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1014, in _gcd_import
  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
  File "<frozen importlib._bootstrap>", line 961, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "<frozen importlib._bootstrap>", line 1014, in _gcd_import
  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
  File "<frozen importlib._bootstrap>", line 973, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'flask.lmsbypak3'
[2022-08-25 00:23:01 +0000] [8] [INFO] Worker exiting (pid: 8)
[2022-08-25 00:23:01 +0000] [1] [INFO] Shutting down: Master
[2022-08-25 00:23:01 +0000] [1] [INFO] Reason: Worker failed to boot.```