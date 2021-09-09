FROM python:3.9.6-slim

COPY . /app 
WORKDIR /app 

RUN pip install -r requirements.txt 

CMD ["gunicorn", "-b","0.0.0.0", "-w", "8", "--timeout", "3000", "app:server"]  
# CMD ["python", "app.py"]