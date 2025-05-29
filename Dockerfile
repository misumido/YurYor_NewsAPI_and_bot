FROM python:3.12
WORKDIR /yuryor
COPY yuryornews /yuryor
EXPOSE 8000
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "run.py"]