cd ./front
docker stop alten.front
docker rm alten.front
docker rmi alten.front
docker build -t alten.front .
docker run -d -p 4200:4200 --name=alten.front alten.front
cd ../back/alten_back
docker stop alten.back
docker rm alten.back
docker rmi alten.back
docker build -t alten.back .
docker run -d -p 3000:3000 --name=alten.back alten.back