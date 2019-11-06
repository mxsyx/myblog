import { Database } from './database.mjs'

import http from 'http'
import queryString from 'querystring'

const server = http.createServer()
const db = new Database();

server.on('request', (req, res) => {
  setHeader(req, res);
  res.writeHead(200);

  if(req.method == 'OPTIONS') {
    completed(res);
  } else if (req.method == 'GET') {
    getDanmaku(res);
  } else if (req.method == 'POST') {
    let reqBody = '';
    req.on("data", (data) => {
      reqBody = reqBody + data;
    });
    req.on('end', () => {  
      addDanmaku(queryString.parse(reqBody), res);
    });
  }
});

function completed(res) {
  res.end();
}

function setHeader(req, res) {
  res.setHeader('Content-Type', 'application/json');
  res.setHeader('Access-Control-Allow-Origin', req.headers['origin']);
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
}

function getDanmaku(res) {
  db.excute('SELECT * FROM auth_user').then((results) => {
    res.write(JSON.stringify(results[0]));
    completed(res);
  });
}

function addDanmaku(data, res) {
  const danmakuData = JSON.parse(Object.keys(data)[0])
  res.write(JSON.stringify({"code":0}));
  completed(res);
}

server.listen(1722, () => {
  console.log('NodeJS 在 1722 端口监听');
})
