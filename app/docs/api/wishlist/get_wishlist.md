## Get Wishlist

This endpoint retrieves the wishlist for a specific user.

### Request

- **Method:** GET
    
- **URL:** `http://localhost:9000/wishlist`
    
- **Request Body:**
    
    - `user_id` (string): The unique identifier of the user whose wishlist is being requested.
        

### Response

- **Status Code:** 200 OK
    
- **Content-Type:** application/json
    
- **Response Body:**
    
    - `wishlist` (object): Contains the details of the user's wishlist.
        
        - `_id` (string): The unique identifier for the wishlist.
            
        - `products` (array of strings): A list of product identifiers included in the wishlist.
            
        - `user_id` (string): The unique identifier of the user associated with the wishlist.
            

### Notes

- Ensure that the `user_id` provided in the request corresponds to an existing user in the system.
    
- The response will include the wishlist details if the request is successful. If the user has no products in their wishlist, the `products` array will be empty.