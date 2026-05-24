# Usa un'immagine Python minimale
FROM python:3.11-alpine

# Imposta la cartella di lavoro nel container
WORKDIR /app

# Copia i requisiti e installali
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia il resto del codice dell'applicazione
COPY . .

# Esponi la porta interna di Flask
EXPOSE 5001

# Avvia l'applicazione configurando Flask per ascoltare su tutte le interfacce
CMD ["python", "app.py"]
