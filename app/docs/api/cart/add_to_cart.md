## Add Item to Cart

This endpoint allows users to add a specific product to their shopping cart.

### Request

- **Method:** POST
    
- **URL:** `http://localhost:9000/cart`
    
- **Request Body:**
    
    - `user_id` (string): The unique identifier of the user whose cart is being updated.
        

#### Request Parameters

The request body must be in JSON format and include the following parameters:

- `user_id` (string): A unique identifier for the user. This parameter is required to associate the cart action with the correct user.
    
- `product_id` (string): A unique identifier for the product being added to the cart. This parameter is required to specify which product to add.
    

#### Example Request Body

``` json
{
  "user_id": "7e67b000-e65c-4ee0-b7b0-b06a4f...",
  "product_id": "prod_002"
}

 ```

#### Response Format

Upon a successful request, the server will respond with a status code of `200` and a JSON object indicating the result of the operation:

- `cart` (boolean): This field will be `true` if the product was successfully added to the cart.
    

#### Example Response

``` json
{
  "cart": true
}

 ```

This indicates that the item has been successfully added to the user's cart.