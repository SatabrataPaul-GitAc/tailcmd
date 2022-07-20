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
cd cli_tool
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

## Tech Stack
---
> The tailcmd command-line utility tool is made using Javascript.
> **Commander and socket io** library is used for building the tool.
> On the **server side, prometheus is configured** such that it scrapes the metrics from its own endpoint (localhost:9090/metric) and writes the query logs [whenever a promQL query is executed from the web UI] to the log file specified in the prometheus.yml configuration file.
> Watchdog is implemented to monitor the log file for changes and take action according to it.
> Server emits out socket io events to inform the command-line tool about the change.

