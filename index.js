const express = require('express');
const admin = require('admin');

const app = express();
const port = 3000;
const serviceAccount = require("C:\\Users\\Documents\\Tasks\\Firebase_Task\\test-a3669-firebase-adminsdk-xa0h0-2eb82997a3.json"); 
app.use(express.json()) 

admin.initializeApp({ 
    credential: admin.credential.cert(serviceAccount) }); 
 
app.post('/', (req, res) => { 
    const data = admin.firestore(); 
    const Ref = db.collection("1").doc("2001"); 
    collectionRef.set(req.body) 
 
}) 
 
app.listen(3000, () => { 
    
   console.log(`Server running on http://${serverIp}:${port}`);
});
