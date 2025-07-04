## Add to Wishlist

This endpoint allows users to add a product to their wishlist.

### Request

- **Method:** POST
    
- **URL:** `http://localhost:9000/wishlist`
    
- **Request Body:**
    
    - `user_id` (string): A unique identifier for the user. This is required to associate the wishlist with the correct user.
        
    - `product_id` (string): A unique identifier for the product that is to be added to the wishlist. This is required to specify which product the user wants to add.
        

**Example Request Body**:

``` json
{
  "user_id": "7e67b000-e65c-4ee0-b7b0-b06a4f...",
  "product_id": "prod_001"
}
```

### Response

- **Status Code:** 200 OK
    
- **Content-Type:** application/json
    
- **Response Body:**
    
   - true if the product was successfully added to the wishlist, false otherwise.

