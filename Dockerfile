# Dit is de dockerfile die wordt gebruikt als environment voor Python
FROM python:3.10-slim
# Kopieer het bestand requirements.txt naar de container
COPY requirements.txt requirements.txt
# Installeer alle benodigde pakketten
RUN pip install --no-cache-dir -r requirements.txt