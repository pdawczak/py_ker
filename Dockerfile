FROM python:3.6

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY poker poker
COPY __init__.py __init__.py
COPY main.py main.py

COPY tests tests

CMD ["python", "-m", "pytest", "-v"]
