AWS CRUD using AWS Lambda, DynamoDB, and API Gateway

This guide walks you through setting up AWS Lambda, DynamoDB, and API Gateway to create a simple CRUD application.

---

1. Create DynamoDB

![image](https://github.com/user-attachments/assets/f490744c-6735-4d26-8253-a0a2ce518291)

---

2. Create a Lambda Function

![image](https://github.com/user-attachments/assets/c6e3e27b-5e0b-4176-8766-2ff0f2605a78)

---

3. Set Up Permissions

- Go to the Permissions section in the Configuration tab of your Lambda function.
- Click on the role you set during Lambda creation.

![image](https://github.com/user-attachments/assets/ec61a03b-048e-43fb-824e-73654811ce1a)

- Attach the following IAM roles:

![roles](https://github.com/user-attachments/assets/4268db1f-7e1f-4875-bfc4-98653cd898ec)

---

4. Create a REST API in AWS API Gateway

- In the AWS API Gateway, create a new REST API:

![image](https://github.com/user-attachments/assets/b1ef5e2d-9b1b-4262-b06a-3d7144086cdf)
![image](https://github.com/user-attachments/assets/c3654fb7-6502-4e7f-bead-fa108baa84da)

---

5. Create Resources in API Gateway

- Create the following 3 resources:
  - /employee
  - /employees
  - /status

- Enable CORS on all three resources:

![image](https://github.com/user-attachments/assets/dba8111a-aa44-4e6d-963d-97e9fbb045f1)
![image](https://github.com/user-attachments/assets/9cb6804b-c255-4cd7-96d4-e570f5eebb1f)

---

6. Define Methods for /employee

- Create the following 4 methods for /employee:
  - GET
  - POST
  - PATCH
  - DELETE

![image](https://github.com/user-attachments/assets/0d2bee72-3252-43a5-a94f-46d1fff56441)

- For each method:
  - Ensure Lambda Proxy Integration is enabled.
  - Select your Lambda function.

![image](https://github.com/user-attachments/assets/2fe393c6-1c87-44d4-8037-945a9c536c51)

---

7. Define Methods for /status and /employees

- Create a GET method for both /status and /employees resources.

---

8. Final API Structure

Your resources, methods, and API Gateway setup should look like this:

![image](https://github.com/user-attachments/assets/6b6b6bf6-e1bd-43ea-9c61-2b26654ae973)

---

9. Deploy the API

- Click on Deploy API (top-right corner) and select New Stage.
- Name your stage (e.g., production).
  
![image](https://github.com/user-attachments/assets/679197cb-c33d-40a1-b3dd-651177c3afc2)

- Copy your Invoke URL.

![roles](https://github.com/user-attachments/assets/1322ecd9-9e5b-4ee7-9efc-96f753cd5117)

- Test it by pasting the Invoke URL followed by /status, e.g.:

  https://abc0def0gh.execute-api.ap-southeast-2.amazonaws.com/production/status

- Expected output:
  {
    "message": "Hello from AWS Lambda!"
  }

---

10. Add Lambda Function Code

- In the AWS Lambda Console, select your Lambda function (e.g., serverless).
- Scroll to the Code section and paste the provided Lambda code (e.g., /lambda_function.py).

![image](https://github.com/user-attachments/assets/d4797eec-ee23-4dfa-85f4-f8e07b8c6fb0)

- Test the API again by going to your Invoke URL:

  https://abc0def0gh.execute-api.ap-southeast-2.amazonaws.com/production/status

- You should get a similar response:

![image](https://github.com/user-attachments/assets/c2fc374a-968f-4b5e-b8a2-01d29c802ac6)

---

11. Frontend Integration

- I have created a simple frontend using a Python script (/test.py).

---

Your AWS Lambda function is now fully operational with CRUD functionality!
