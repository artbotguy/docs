docker mac (дефолтно через брю запустить анрил)

  

https://stackoverflow.com/questions/44084846/cannot-connect-to-the-docker-daemon-on-macos/76556754?answertab=modifieddesc#tab-top



{{DOKER}}
docker stop $(docker ps -a -q)          - stop all containers
docker rm -vf $(docker ps -aq)          - delete all containers including its volumes
docker rmi -f $(docker images -aq)      - delete all images

docker stats [OPTIONS] [C...]
docker exec -it <CONTAINER> bash -l
docker run -it <I> bash           - (*sh - bash) interactive shell container (if image his contain) https://stackoverflow.com/questions/44769315/how-to-see-docker-image-contents

docker container ls 		    - list active containers - [options]

docker network inspect bridge --format='{{(index .IPAM.Config 0).Gateway}}' - docker network

docker stop <CONTAINER>

docker cp ./some_file CONTAINER:/work             - (?) copy local file in container
docker cp CONTAINER:/var/logs/ /tmp/app_logs      - (?) copy file from container to local (path: /folder/sub-folder to /folder --- for copy without nesting)
