import mongoose from "mongoose";

const productSchema = mongoose.Schema(
    {
        title: {
            type: String, 
            required: true,
        },
        description: {
            type: String, 
            required: true,
        },
        price: {
            type: Number, 
            required: true,
        },
        discountRate: {
            type: Number, 
            required: true,
        },
        stock: {
            type: Number, 
            required: true,
        },
        rating: {
            type: Number, 
            required: true,
        },
        thumbnail: {
            type: String, 
            required: true,
        },
        images: {
            type: String, 
            required: true,
        },
    },
    {
        timestamp: true
    },
)

const Product = mongoose.model("Product", productSchema);

export default Product;