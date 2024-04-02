[![medium][medium-shield]][medium-url]
[![linkedin][linkedin-shield]][linkedin-url]
[![github][github-shield]][github-url]

<!-- ABOUT THE PROJECT -->
## Hello World Docker ?
Let's try building a straightforward Flask application and Dockerizing it. We will look at how to host a flask application inside a container and expose the port to use it outside the container network. Now let's get going...

#### What you will learn ?
* Writing a docker file.
* Running basic commands to build an image and run a container.

#### Prerequisites
* [Docker-desktop] should be installed on your machine
* Python and Flask installed

### Technologies Used 
* Docker 🐳
* Python
* Flask 

<!-- GETTING STARTED -->
## Getting Started
This Flask application will create a simple webserver which will return below text when the user will browse [http://127.0.0.1:5000]


### Steps to follow
* Clone Repo
  ```sh
  git clone https://github.com/6613pranav/hello-world-docker-flask.git
  ```
* Install all the dependencies to run Flask Application
  ```sh
   pip install -r requirement.txt
  ```
* Run the flask App
  ```sh
  flask --app flask_app run -h 0.0.0.0
  ```
Great! Now that we saw how we can run a flask app on the local system, we will dockerize the same and run the container to get the above output.

### Understanding about the commands written in Docker file
* This commands pulls the public Python image from [docker-hub]
   ```sh
   FROM python:3.12.2
   ```
* Copies everything from local current working directory to image
   ```sh
   COPY . .
   ```
* This will install all the required dependencies to run the flask app.
   ```sh
   RUN pip install  -r requirements.txt
   ```
* Runs the command whenever the container is created
   ```sh
   CMD ["python", "flask_app.py"]
   ```

_Now we have learnt about the commands inside the docker file, we will see how to build the image & run the container._

### Building a docker image
```sh
docker build -t flask-app:v1 .
```
_'-t' flag is used to set the tag of image we are creating, in out case the image name is 'flask-app' and tag is 'v1'_
![image](https://github.com/6613pranav/hello-world-docker-flask/assets/48874265/7da4a5b1-331a-46eb-b71e-8331471c3eb6)

### Creating a container from above image & running the same
```sh
docker run -p 3000:5000 flask-app:v1 
```
_'-p' tag is used to bind port from container to local machine, in our case we are binding port 3000 (local machine) to port 5000 (container)_
![image](https://github.com/6613pranav/hello-world-docker-flask/assets/48874265/0db4d254-52cb-4d82-9104-8d62d091aa08)
![image](https://github.com/6613pranav/hello-world-docker-flask/assets/48874265/8b0695ae-8400-414c-a779-0524ee4a98c5)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-url]: https://www.linkedin.com/in/pranav-vatsa-1a4a261b0/
[linkedin-shield]: https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white
[medium-url]: https://medium.com/@Cloud.Explorer
[medium-shield]: https://img.shields.io/badge/medium-1DA1F2?style=for-the-badge&logo=ko-fi&logoColor=white
[github-url]: https://github.com/6613pranav
[github-shield]: https://img.shields.io/badge/github-1DA1F2?style=for-the-badge&logo=github&logoColor=white
[Docker-desktop]: https://docs.docker.com/get-docker/
[docker-hub]: https://hub.docker.com/_/python/
