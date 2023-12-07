```bash
(venv) [baba@bastien-portable TP-Dev]$ time python web_async_multiple.py url.txt

real    0m0,263s
user    0m0,150s
sys     0m0,013s
(venv) [baba@bastien-portable TP-Dev]$ time python web_sync_multiple.py url.txt

real    0m0,398s
user    0m0,097s
sys     0m0,024s
```