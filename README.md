# Model Design Template

This template was created to speed up the model design and development process.
If the model passes the test cases in this application, then it will also work in
the context of the server.

## Getting Started
In the model directory, fill out the code in `model.py` and `config.py` according to
the directions in each file. Then, add the requirements for your project into the
`requirements.py` file in the model directory. You may add any supporting files or
folders that your model needs under the model directory.

**Important: All code that your model uses or references *MUST* be contained in the
model directory.**

## Testing your Model

In the root directory of the project, run the command `docker-compose build` and then
`docker-compose up`. You will see the results of the test cases in your terminal. If all
test cases pass, then your model will work in the server environment.