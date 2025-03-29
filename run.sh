docker build -t fastapi-helloworld .
docker image prune -f
docker run -p 8000:8000 fastapi-helloworld