import express from "express";
import dotenv from "dotenv";
import mongoose from "mongoose";

// Dotenv config
dotenv.config();

// defining port here 
const PORT = process.env.PORT || 5000;

// Initializing express app here
const app = express() 

// Creating mongoose connection here 
mongoose
    .connect("mongodb://127.0.1.1/mato")
    .then(()=>console.log("Connected to MongoDB successfully."))
    .catch((err)=>console.log(`Error connecting to database: ${err}`));
    
// Root API 
app.get('/', async (req, res)=>{
    res.status(200).send(`Backend running at port ${PORT}`);
})

app.listen(PORT, ()=>{
    console.log(`Server running at port ${PORT}`);
})