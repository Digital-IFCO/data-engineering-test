
# IFCO Data Engineering Challenge

## Setup Instructions

### 1. Clone the Repository or Extract the Files

Download and unzip the project directory or clone the repository to your local machine.

### 2. Run Using Docker

To run this project using Docker, ensure you have Docker installed. Then, follow these steps:

1. Build the Docker image:

    ```bash
    docker build -t ifco-data-engineering .
    ```

2. Run the Docker container:

    ```bash
    docker run -p 8888:8888 -v $(pwd):/app ifco-data-engineering
    ```

3. Open the Jupyter Notebook:

    Access the Jupyter notebook by navigating to `http://localhost:8888` in your browser.

### 3. Running Locally (Without Docker)

1. Create a virtual environment:

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Launch the Jupyter Notebook:

    ```bash
    jupyter notebook "C:\Users\PatriciaRodríguezVaq\PythonVirtualEnvironment\text_embeddings\-- Tests\IFCO_Data_Engineering_Project\IFCO_Data_Engineering_Challenge.ipynb"
    ```

## Project Structure

- `IFCO_Data_Engineering_Challenge.ipynb`: The main notebook containing all the code and analysis.
- `Dockerfile`: The Dockerfile to build the containerized environment.
- `README.md`: This file with instructions for setting up and running the environment.

## Unit Testing

The notebook contains unit tests to validate the data processing logic.
