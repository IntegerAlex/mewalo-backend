## User Login Endpoint

This endpoint is used to authenticate a user by logging them in using their phone number.

### Request

- **Method**: POST
    
- **URL**: `http://<domain>/user/login`
    
- **Request Body**: The request must include a JSON object with the following parameter:
    
    - `phone` (string): The phone number of the user attempting to log in. This should be a valid phone number format.
        

**Example Request Body**:

``` json
{
  "phone": "8888888888"
}

 ```

### Response

Upon a successful login, the server will respond with a status code of `200` and a JSON object containing a message. The response structure is as follows:

- **Status**: 200
    
- **Content-Type**: application/json
    
- **Response Body**:
    
    - `message` (string): A message indicating the result of the login attempt. This will typically be an empty string on successful authentication.
        

**Example Response**:

``` json
{
  "message": "OTP sent successfully"
}

 ```

### Notes

- Ensure that the phone number provided is correctly formatted to avoid authentication errors.
    
- The response may include additional information in future implementations, so it is advisable to handle the response dynamically.