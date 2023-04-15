FROM python:3.9-alpine
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
RUN pip install flask mistune
COPY . .
EXPOSE 5000
ENTRYPOINT ["python", "wsgi.py"]
