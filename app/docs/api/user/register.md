## User Registration Endpoint

This endpoint allows users to register a new account by providing their personal information.

### Request

- **Method**: POST
    
- **URL**: `http://<domain>/user/register`
    

#### Request Body

The request should contain a JSON object with the following parameters:

- `first_name` (string): The first name of the user.    

- `last_name` (string): The last name of the user.

- `email` (string): The email address of the user. It should be a valid email format.
    
- `phone` (number): The phone number of the user. It should be a numeric value.
    

    

Example of a valid request body:

``` json
{
  "first_name": "Test",
  "last_name": "ing",
  "email": "test@example.com",
  "phone": 8888888888
}

 ```

### Response

- **Status Code**: 200
    
- **Content-Type**: application/json
    

#### Response Body

On successful registration, the response will return a JSON object with a message indicating the result of the registration process.

Example of a response:

``` json
{
  "message": "OTP sent successfully"
}

 ```

### Notes

- Ensure that all required fields are provided in the request body.
    
- The response message may contain additional information in future implementations, but currently, it returns an empty string.