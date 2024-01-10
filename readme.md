command to create the volumne that is mount to specified device 

docker build command 
docker build -t lambda-packager .  

docker volume create --name my_volume -o type=none -o device=/Users/manojpathak/Documents/appdata -o o=bind

docker run -v my_volume:/app lambda-packager
 
