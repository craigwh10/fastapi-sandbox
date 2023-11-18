docker run \
        -v $PWD/data:/data/ \
        -v $PWD/src:/src/ \
        -t -i --name pyapp \
        -p 3000:3000 pyapp:latest
echo $PWD