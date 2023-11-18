docker rm -f pyapp
docker image rm pyapp:latest

docker build -f Dockerfile -t pyapp:latest .