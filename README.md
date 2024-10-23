![image](https://github.com/user-attachments/assets/ea3dac8a-a8c1-4773-9132-e81b3cd88c09) AWS_CRUD
1. Create Dynamodb
  ![image](https://github.com/user-attachments/assets/f490744c-6735-4d26-8253-a0a2ce518291)
2. Create a Lambda function:
   ![image](https://github.com/user-attachments/assets/c6e3e27b-5e0b-4176-8766-2ff0f2605a78)
3. Go the Permissions section in Configuration and Click on the role you had set above.
   ![image](https://github.com/user-attachments/assets/ec61a03b-048e-43fb-824e-73654811ce1a)
4. Attach the following roles in the AWS IAM 
 ![roles](https://github.com/user-attachments/assets/4268db1f-7e1f-4875-bfc4-98653cd898ec)
5. In AWS Api Gateway, create a REST API:
   ![roles](https://github.com/user-attachments/assets/b1ef5e2d-9b1b-4262-b06a-3d7144086cdf)
   ![image](https://github.com/user-attachments/assets/c3654fb7-6502-4e7f-bead-fa108baa84da)
6. Create these 3 resources /employee and /employees and /status:
   Enable CORS in all 3 of the resources:
   ![image](https://github.com/user-attachments/assets/dba8111a-aa44-4e6d-963d-97e9fbb045f1)
   ![image](https://github.com/user-attachments/assets/9cb6804b-c255-4cd7-96d4-e570f5eebb1f)

7.Create 4 methods in /employee:
 ![image](https://github.com/user-attachments/assets/0d2bee72-3252-43a5-a94f-46d1fff56441)
 In /employee Create GET, POST, PATCH , DELETE(Click "Select a Method" and choose indicated by red arrow):
 Make sure to set lambda proxy integration as on, and select your Lambda:
  ![image](https://github.com/user-attachments/assets/2fe393c6-1c87-44d4-8037-945a9c536c51)
8. Similarly Create a GET Method in /status Resource.
9. Create a GET Method in /employees Resource.
10. Final Resources, Methods and API Gateways should look something like this:
 ![image](https://github.com/user-attachments/assets/6b6b6bf6-e1bd-43ea-9c61-2b26654ae973)
11. Deploy the API by clicking "Deploy API" on the top right corner (select new stage and give it a name):
  ![image](https://github.com/user-attachments/assets/679197cb-c33d-40a1-b3dd-651177c3afc2)
   Copy to your "Invoke URL" 
  ![roles](https://github.com/user-attachments/assets/1322ecd9-9e5b-4ee7-9efc-96f753cd5117)
  On a new tab paste this the invoke URL with a /status following it, it'll look something like this:
  https://abc0def0gh.execute-api.ap-southeast-2.amazonaws.com/production/status
  Expected output:
  "Hello from AWS Lambda!" as json 
12. Come back to AWS Lambda page, select your lambda function(here it is called"sereverless"). 
Scroll to the code section and paste the given lambda function code,you can modify it as you want.
This is a basic one i found on a youtube video. (/lambda_function.py)
 ![image](https://github.com/user-attachments/assets/d4797eec-ee23-4dfa-85f4-f8e07b8c6fb0)
Go back to this link: https://abc0def0gh.execute-api.ap-southeast-2.amazonaws.com/production/status
   ![image](https://github.com/user-attachments/assets/c2fc374a-968f-4b5e-b8a2-01d29c802ac6)
