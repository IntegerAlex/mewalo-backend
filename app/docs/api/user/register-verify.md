## User Registration Verification Endpoint

This endpoint is used to verify a user's registration by validating the one-time password (OTP) sent to their registered phone number. Upon successful verification, it returns a JSON Web Token (JWT) for further authenticated requests.

### Request

**Method:** POST  
**URL:** `http://<domain>/user/register/verify`

#### Request Body

The request body must be in JSON format and contain the following parameters:

- **phone** (integer): The phone number associated with the user's account.
    
- **otp** (integer): The one-time password sent to the user's phone for verification.
    

##### Example Request Body

``` json
{
  "phone": 8888888888,
  "otp": 728821
}

 ```

### Response

On successful verification, the server responds with a status code of 200 and returns a JSON object containing the following fields:

- **jwt** (string): The JSON Web Token for the user, which is used for authentication in subsequent requests.
    
- **message** (string): A message indicating the result of the verification process.
    
- **user** (object): An object containing user details:
    
    - **_id** (string): The unique identifier for the user.
        
    - **email** (string): The email address of the user.
        
    - **first_name** (string): The first name of the user.
        
    - **last_name** (string): The last name of the user.
        
    - **phone** (integer): The phone number of the user.
        

##### Example Response

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

### Notes

- Ensure that the phone number and OTP are correct to receive a successful response.
    
- The JWT returned can be used for authenticating future requests to protected endpoints.