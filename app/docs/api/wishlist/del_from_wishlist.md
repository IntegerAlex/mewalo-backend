## Delete Wishlist Item

This endpoint allows users to remove an item from their wishlist.

### Request

- **Method:** DELETE
    
- **URL:** `http://localhost:9000/wishlist`
    
- **Request Body:**
    
    - `user_id` (string): The unique identifier for the user whose wishlist is being modified.
        
    - `product_id` (string): The unique identifier for the product that is to be removed from the wishlist.
        


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
    
    - true if the product was successfully removed from the wishlist, false otherwise.
            