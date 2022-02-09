# Sensor Cloud

# Version 1.0

# Languages
Python (Flask) <br>
MySQL (8.0) <br>

# Install Docker
https://docs.docker.com/engine/install/ubuntu/

reference to the above link to install docker in your server

* install docker-compose 
    $ sudo apt install docker-compose

* -> Go to project folder, and run the following commands
# Build docker-compose
    $ sudo docker-compose build

# Run docker-compose (all container will be run)
    $ sudo docker-compose up

# Finish running project step
After you run the above command and there is no error, you can call the server routes

IF you want to stop docker running, <br>
    $ sudo docker-compose down


# Note by Nay
If you want a fresh start for everything, run <br> 
    $ docker system prune -a <br>
    $ docker volume prune <br>
 
The first command removes any unused containers and the second removes any <br> unused volumes. I recommend doing this fairly often since Docker likes to stash <br> everything away causing the gigabytes to add up.

