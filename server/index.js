const express = require('express');
const cors = require('cors');
const http = require('http');
const app = express();
const ip = require("ip")
const port = 3000;
const HTTPserver=  http.createServer(app);
console.log(ip.address())
let data =0
let data2 =""

app.use(express.json());
app.use(cors());

app.get('/', (req, res) => res.json({ "message": data }));

app.get('/pays', (req, res) => res.json({ "pays": data2 }));

app.get('/test', (req, res) => res.json({ 
    ma_vie: 'j\'ai 20 lol',
    chatGPT: "Super blague de prout",
    bestGenerique:"sasageyo",
    vinted:"si tu ne veux plus des tes vetements ! vend les !"
 }));


app.post('/led', (req, res) => {
    console.log(req.body.number)
    data = req.body
    r = req.body.r
    g = req.body.g
    b = req.body.b
    res.send({ "message": data })});

app.post('/flag', (req, res) => {
    console.log(req.body.number)
    data2 = req.body
    res.send({ "flag": data2 })});

HTTPserver.listen(port, () => { 
    console.log(`On écoute aux portes : `+port);
});