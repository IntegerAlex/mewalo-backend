## Endpoint: Get Products

### Description

This endpoint retrieves a list of products from the server. It is designed to provide clients with access to product information, including details such as product name, description, price, and other relevant attributes.

### Request

- **Method**: GET
    
- **URL**: `http://<domain>/products/`
    
- **Request Body**: None required for this GET request.
    

### Response

- **Status Code**: 200 OK
    
- **Content-Type**: application/json
    

#### Response Structure

The response will contain a JSON object with the following structure:

``` json
{
  "products": [
    {
      "_id": "string",                // Unique identifier for the product
      "category": "string",           // Category of the product
      "product_barcode": "string",    // Barcode associated with the product
      "product_coupon": {},            // Coupon information for discounts (object)
      "product_delivery": {},          // Delivery options (object)
      "product_description": "string", // Description of the product
      "product_id": "string",          // Unique product ID
      "product_image_url": "string",   // URL of the product image
      "product_manufacturer": "string",// Manufacturer of the product
      "product_name": "string",        // Name of the product
      "product_price": 0,              // Price of the product (numeric)
      "product_quantity": 0,           // Available quantity of the product (numeric)
      "product_unit": "string",        // Unit of measurement for the product
      "subcategory": "string"          // Subcategory of the product
    }
  ]
}

 ```

### Notes

- The `products` array will contain multiple product objects, each representing a different product available in the inventory.
    
- Ensure that the server is running to successfully retrieve the product data.  