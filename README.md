# Project-python

This project aims to showcase a simple web page built using **Python**, **HTML**, **CSS**, and **JavaScript**, **Flask**. It is a basic demonstration of a static webpage that can be run locally using Docker.

## Technologies Used

- **Python**
- **HTML**
- **CSS**
- **Flask**

## Installation

To run this project, follow these steps:

1. **Download the project image from DockerHub**:

Run the following command to pull the latest image of the project:

   ```bash
   docker pull andrespaida/flask-web-app:latest

2. **Create a container from the downloaded image**:

Next, create and run the container with this command:

´´´bash
docker run -d -p 5000:5000 --name web-container2 andrespaida/flask-web-app:latest

3. **Access the webpage**:

Once the container is running, open your browser and go to:

http://localhost:5000

## License

This project is under the creator's license (Andrés Paida). All rights reserved.
