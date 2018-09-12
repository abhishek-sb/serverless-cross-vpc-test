# serverless-cross-vpc-test
Sample project to refer when calling a lambda (in private VPC) from lambda (no VPC).


#### Description

`serverless.yml`: contains all function definition with vpc configuration and environment variables

`handler.py`: file containing function `hello` to be deployed with no vpc configuration (will land in default)

`mongo_connect.py`: file containing function `handler` to connect to database. This file and database should be in same VPC configurations (i.e. subnets and security groups).
This function is mentioned multiple times in `serverless.yml` to be deployed in different VPC. Please provide `<username>` and `<password>` in this file to connect to database.

`input.json`: This is just a file as a reference to hold dynamic data (provide country alias here). `hello` function in `handler.py` will pick this alias and connects to appropriate database.



#### Running Instructions:

The below command will read country alias from input.json and will invoke appropriate lambda function accordingly.

```
$ serverless invoke --function hello -l --path input.json
```
