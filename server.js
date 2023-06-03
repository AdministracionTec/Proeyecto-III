const express = require('express');
const app = express();

const productos = [
    { id: 1, name: 'Producto 1' },
    { id: 2, name: 'Producto 2' },
    { id: 3, name: 'Producto 3' },
    // Agrega más productos aquí si lo deseas
];

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

app.get('/productos', (req, res) => {
    res.json(productos);
});

const port = 3000;
app.listen(port, () => {
    console.log(`Servidor iniciado en http://Juegosfera:${port}`);
});
