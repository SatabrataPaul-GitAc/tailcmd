# Tailcmd
---
##### Tailcmd is a command-line utility tool that lets users to monitor file changes on a server by displaying the changes on the terminal of the client.

- Enter ip address of server
- Enter the file name 
- Start monitoring

## Installation
---
**Tailcmd requires [Node.js](https://nodejs.org/) v10+ to run**
> ***Clone the repository***
```sh
git clone https://github.com/SatabrataPaul-GitAc/tailcmd.git
```
> ***Change the directory***
```sh
cd tailcmd
```
> ***Install the dependencies***
```sh
npm install
```
> ***Build the command-line tool to be accessed globally***
```sh
npm i -g 
or
npm i --location=global
```
> ***Run tailcmd in terminal***
```sh
tailcmd --help
```
***Note- Ignore the server directory, which contains the code for the server***

## Docker installation
---
**Tailcmd can also be run as a docker container**

####  Version1.0
> Pull the image from docker hub
```sh
docker pull satabrata2000/command_line_tool:1.0
```
> Run the following to launch the container
```sh
docker run -it satabrata2000/command_line_tool:1.0
```
> Inside the container run: **tailcmd --help**
```sh
tailcmd --help
```
> **Example uasge:** tailcmd fetch -a 3.110.170.88 -f query.log 

## Tech Stack
---
> The tailcmd command-line utility tool is made using Javascript.
> **Commander and socket io** library is used for building the tool.
> On the **server side, prometheus is configured** such that it scrapes the metrics from its own endpoint (localhost:9090/metric) and writes the query logs [whenever a promQL query is executed from the web UI] to the log file specified in the prometheus.yml configuration file.
> Watchdog is implemented to monitor the log file for changes and take action according to it.
> Server emits out socket io events to inform the command-line tool about the change.

- Client: JavaScript
- Server: Python
- Protocol: webscokets

## Server
---
The server side code implements the watch feature that monitors the file for a change and notifies the client side command line tool about it.
Prometheus is configured to write the query logs to a file as specified in its configuration file, whenever we run a promQL query from the webUI

The idea about about the command-line tool making http requests to the server for querying about changes made to the file is inefficient, because it would make lots unnecessary of API calls  even when there is no change made to the file. 
Thus, websocket protocol is used here.
Watchdog is implemented to monitor the file for any change and trigger an event accordingly.

# Important Note:
## Issues

> Certain issues regarding the command-line tool that couldn't be fixed

> The client is unable to receive the event that is emitted from the server whenever any change is made to the file. 
> The watchdog is monitoring the changes properly, as the changes are displayed on the server terminal. But, when the socket event is emitted out, the client is unable to receive it.
> The transport protocol used by websocket is polling , therefore it always tries to re-establish a connecteion with the server. 

> Apart from this, the application is running properly on local as well as from inside of the container

## Demo 
Tailcmd [**demo**](https://drive.google.com/file/d/1kRk_T7Ui9ffxDbEQc58CYPManGAeEPXU/view?usp=sharing)

Dockerhub [Link](https://hub.docker.com/repository/docker/satabrata2000/command_line_tool)
