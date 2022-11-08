### Description

Code that gets the live video feed from a [DJI Tello drone](https://m.dji.com/be/product/tello) and feeds it to the model inference endpoint. 

### Usage guide
This guide assumes that you have already succesfully installed the docker container used for model inference. 

DJI Tello setup 

- [Official User Manual](https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20User%20Manual%20v1.4.pdf)
- [Setup guide](https://www.65drones.com/pages/tello-operation-guide)

Run the docker container 
```
docker run -d -p 8000:8000 ghcr.io/rbreens/aerialwastedetection-fastapi
```

Run the code (Make sure you are connected to the DJI tello hotspot)

```
cd ./app/dji-tello/
python ./djitello-video.py
```