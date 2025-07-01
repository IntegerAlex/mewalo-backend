## User Login Verification Endpoint

This endpoint is used to verify a user's login by validating the provided One-Time Password (OTP) against the registered phone number. Upon successful verification, it returns a JSON Web Token (JWT) for session management.

### Request

- **Method:** POST
    
- **URL:** `http://<domain>/user/login/verify`
    

#### Request Body

The request body must be sent in JSON format and should include the following parameters:

- `phone` (string): The phone number associated with the user account. This should be a valid phone number.
    
- `otp` (string): The one-time password sent to the user's phone for verification.
    

**Example Request Body:**

``` json
{
  "phone": "8888888888",
  "otp": "803069"
}

 ```

### Response

The response will be returned in JSON format and will contain the following fields:

- `jwt` (string): A JSON Web Token that can be used for authenticated requests. It will be empty if the verification fails.
    
- `message` (string): A message indicating the status of the verification process.
    
- `user` (object): An object containing user details if the verification is successful:
    
    - `_id` (string): The unique identifier for the user.
        
    - `email` (string): The email address of the user.
        
    - `first_name` (string): The first name of the user.
        
    - `last_name` (string): The last name of the user.
        
    - `phone` (number): The phone number of the user.
        

**Example Response:**

``` json
{
  "jwt": "",
  "message": "",
  "user": {
    "_id": "",
    "email": "",
    "first_name": "",
    "last_name": "",
    "phone": 0
  }
}

 ```

### Status Codes

- **200 OK**: Verification successful, user details and JWT returned.
    
- **4xx/5xx**: Various error responses indicating issues with the request or server errors.