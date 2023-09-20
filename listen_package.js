const express = require("express");
const admin = require('firebase_admin');
const serviceAccount = require('C:\\Users\\Bakka\\Downloads\\Firebase_Task\\sic-task-f5c09-firebase-adminsdk-jrjog-f0bf5d1d16.json');

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount)
});

const db = admin.firestore();

// Listen for data 
const docRef = db.collection('test').doc('demo');
const app = express();
const port = 3000;
  app.get("/", (req, express.response) =>{
    console.log(req.query);
    req.send('Hello  GETT');
  });
app.post("/", (req, express.response) =>{
    console.log(req.body)
});
