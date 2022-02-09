FROM node:16.13
# set /app as work directory
WORKDIR /app

# copy package.json to work directory, so that we install npm dependencies
COPY package.json /app

# update npm (update version in the future)
RUN npm install -g npm@8.3.1

# install npm dependencies
RUN npm install 
# OR `RUN yarn install`

# grant access
RUN mkdir node_modules/.cache && chmod -R 777 node_modules/.cache

# copy your project files to work directory
COPY . /app

# run your app
# CMD ["npm", "start"] 
# OR CMD ['yarn', 'run', 'start']
