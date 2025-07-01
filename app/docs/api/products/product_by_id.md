## Get Product Details

This endpoint retrieves detailed information about a specific product identified by its unique product ID. The request is made to the endpoint `GET /products/<product_id>`, where `<product_id>` is the product ID for which the details are being requested.

### Request

- **Method**: `GET`
    
- **URL**: `http://<domain>/products/<product_id>`
    

**Note**: This endpoint does not require a request body.

### Response

Upon a successful request, the server responds with a status code of `200` and a JSON object containing the product details. The structure of the response is as follows:

``` json
{
  "product": {
    "_id": "",                     // Unique identifier for the product
    "category": "",                // Category of the product
    "product_barcode": "",         // Barcode associated with the product
    "product_coupon": {},           // Coupon information related to the product
    "product_delivery": {},         // Delivery options for the product
    "product_description": "",      // Description of the product
    "product_id": "",               // ID of the product
    "product_image_url": "",        // URL of the product image
    "product_manufacturer": "",     // Manufacturer of the product
    "product_name": "",             // Name of the product
    "product_price": 0,             // Price of the product
    "product_quantity": 0,          // Available quantity of the product
    "product_unit": "",             // Unit of measurement for the product
    "subcategory": ""               // Subcategory of the product
  }
}

 ```

### Summary

This endpoint is essential for clients needing to fetch detailed information about a specific product, including its pricing, description, and other relevant attributes.