# Author
    Nay Oo Kyaw
    nayookyaw.nok@gmail.com

# Install Docker
https://docs.docker.com/engine/install/ubuntu/

reference to the above link to install docker in your server

* install docker-compose 
    $ sudo apt install docker-compose

* -> Go to project folder, and run the following commands
# Build docker-compose
    $ sudo docker-compose build --no-cache

# Run docker-compose (all container will be run)
    $ sudo docker-compose up

# Stop docker-compose (all container will be stopped)
    $ sudo docker-compose stop

# Reference Link
https://www.thegeekstuff.com/2016/04/docker-compose-up-stop-rm/

# Finish running project step
After you run the above command and there is no error, you can call the server routes

IF you want to reset docker container, <br>
[IMPORTANT] if you down the docker, all data (e.g database) not include codes, will be DELETED!
    $ sudo docker-compose down


# Note by Nay
If you want a fresh start for everything, run <br> 
    $ docker system prune -a <br>
    $ docker volume prune <br>
 
The first command removes any unused containers and the second removes any <br> unused volumes. I recommend doing this fairly often since Docker likes to stash <br> everything away causing the gigabytes to add up.

# Error Debug
If you encounter the "unsorted double linked list corrupted" in python backend server <br>
follow the below instruction <br>
https://blog.csdn.net/qq_26870933/article/details/109110772 <br>

$ ulimit -a 
$ ulimit -s 102400 

Means change to 100 MB stack size (s is stack size, default is 8192 )