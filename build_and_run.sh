docker build -t ml-model-deployment .
docker run -it --rm -p 9696:9696 ml-model-deployment