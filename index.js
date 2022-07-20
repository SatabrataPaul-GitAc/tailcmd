#!/usr/bin/env node

const {program} = require('commander');
const { io } = require("socket.io-client");

function fetchContent({address, filename, num}){
       const socket = io(`http://${address}:8000/`,{transports: ['polling']});
       socket.on('connect',()=>{
              console.log("Connection established to the remote server")
              console.log("Press [Ctrl+C] to exit")
       });
       socket.on('connect_error', (error)=>{
              console.log(error);
       })
       socket.on('disconnect', (reason, description)=>{
              console.log(reason);
              console.log(description);
       });
       socket.on('file_data', (...data)=>{
              console.log(data[0])
       })
       socket.on('file_data_modified', (...data)=>{
              console.log("File modified\n\n")
              console.log(data[0]);
       })
       socket.on('error', (...data)=>{
              console.log(data[0]);
       })
       socket.connect();
       socket.emit('fetch', {file: filename, num: num});
}

program.command('fetch')
       .description('fetches real time updates for file changes on a server')
       .requiredOption('-a, --address <address>', description='ip address of the remote server')
       .option('-f, --filename <filename>', description='name of the file which is to be monitored', defaultValue='')
       .option('-n, --num <num>', description='number of last n lines to be displayed', defaultValue='10')
       .action(fetchContent);

program.parse();
