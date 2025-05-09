# docker_push.sh
#!/bin/bash
# Build, tag, and push Docker image

IMAGE_NAME="myapp"
TAG=$(git rev-parse --short HEAD)
REPO="docker.io/username/$IMAGE_NAME"

docker build -t $IMAGE_NAME:$TAG .
docker tag $IMAGE_NAME:$TAG $REPO:$TAG
docker push $REPO:$TAG
echo "Pushed $REPO:$TAG"