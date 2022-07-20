FROM node:16

RUN useradd --create-home --shell /bin/bash cli_user

WORKDIR /home/cli_user

COPY package*.json ./

RUN npm install

COPY index.js .

RUN npm i -g

CMD ["/bin/bash"]
