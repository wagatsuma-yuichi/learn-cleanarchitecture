### 起動する場合
```bash
cd 001_simple_cleanarchitecture
cd 002_DI_cleanarchitecture
pip install -r requirements.txt
APP_ENV=development uvicorn main:app --host 0.0.0.0 --port 8000
APP_ENV=test uvicorn main:app --host 0.0.0.0 --port 8000
```