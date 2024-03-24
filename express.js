const express = require('express');
const { spawn } = require('child_process');
const app = express();
const port = 3000;

app.get('/events', (req, res) => {
    const python = spawn('python', ['webscraping.py']); // Make sure Python is in your PATH
    let data = '';

    // Collect data from script
    python.stdout.on('data', function (output) {
        data += output.toString();
    });

    // Respond with data when script completes
    python.on('close', (code) => {
        res.send(data);
    });
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}/`);
});
