## Contact API

This endpoint allows users to submit a contact inquiry through a POST request. It is designed to capture user details and their message for further processing.

### Request

**URL:** `http://<domain>/contact`  
**Method:** `POST`

#### Request Body

The request body should be in JSON format and include the following parameters:

- **first_name** (string): The first name of the user submitting the inquiry.
    
- **last_name** (string): The last name of the user submitting the inquiry.
    
- **email** (string): The email address of the user, used for follow-up communication.
    
- **phone** (string): The phone number of the user for contact purposes.
    
- **subject** (string): A brief subject line summarizing the inquiry.
    
- **message** (string): The detailed message or inquiry from the user.
    

##### Example Request Body

``` json
{
  "first_name": "Jane",
  "last_name": "Doe",
  "email": "jane.doe@example.com",
  "phone": "+1987654321",
  "subject": "Inquiry about your services",
  "message": "Testing API Docs"
}

 ```

### Response

Upon successful submission, the API will respond with a status code of `200` and a JSON object containing a message.

#### Response Body

- **message** (string): A confirmation message indicating the status of the inquiry submission.
    

##### Example Response

``` json
{
  "message": ""
}

 ```

### Notes

- Ensure that all fields in the request body are provided and correctly formatted to avoid errors.
    
- This endpoint is intended for inquiries related to services, and the response will confirm receipt of the message.