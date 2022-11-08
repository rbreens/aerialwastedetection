# aerialwastedetection

### Description 

A machine learning project with the goal of detecting and classifying litter from low altitude aerial pictures.

### Docker Quickstart

This docker guide can be used to set up the model inference endpoint quickly with minimal dependency installation

Install docker engine 

- [Windows Installation](https://docs.docker.com/desktop/install/windows-install/)
- [Mac OSX Installation](https://docs.docker.com/desktop/install/mac-install/)
- [Ubuntu Installation](https://docs.docker.com/engine/install/ubuntu/)

Pull the docker image
```
docker pull ghcr.io/rbreens/aerialwastedetection-fastapi
```

Run the container
```
docker run -d -p 8000:8000 ghcr.io/rbreens/aerialwastedetection-fastapi
```
Running the test script 
```
pip install requests
```
```
cd ./app/tests
python ./test.py
```


