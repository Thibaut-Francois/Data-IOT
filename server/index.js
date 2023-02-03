const express = require('express');
const cors = require('cors');
const http = require('http');
const app = express();
const ip = require("ip")
const port = 3000;
const HTTPserver=  http.createServer(app);
console.log(ip.address())
let data =0

app.use(express.json());
app.use(cors());

app.get('/', (req, res) => res.json({ "message": data }));

app.get('/test', (req, res) => res.json({ 
    ma_vie: 'j\'ai 20 lol',
    chatGPT: "Super blague de prout",
    bestGenerique:"sasageyo",
    vinted:"si tu ne veux plus des tes vetements ! vend les !"
 }));

 app.post('/led', (req, res) => {
    console.log(req.body.number)
    data = req.body.number
    res.send({ message: 'Hello World! In Json' })});

HTTPserver.listen(port, () => { 
    console.log(`On écoute aux portes : `+port);
});