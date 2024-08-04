# image-to-knit-or-crochet-pattern-app also known as Bunny

Craft and Art Project 

Creating an art's and crafts project. (Temporary naming for the project for now)
Ideas:
[documents](/documents)

This project is a web application that converts images to crochet patterns. Users can upload an image, define the pixel size, and generate a pixelated version of the image along with a color grid and pattern details.

## Features

- Upload an image
- Define pixel size
- Generate a pixelated version of the image
- Display a color grid with color names
- Tooltip for each cell displaying color and position
- Sidebar list of colors with highlighted click and hover information

## Installation

### Prerequisites

Before you begin, ensure you have met the following requirements:
- You have installed Python 3.6 or later.
- You have installed `pip`, the Python package installer.

### Setting up Python Environment

1. **Install `pyenv` (for managing multiple Python versions):**

    On Windows, you can install `pyenv` using [pyenv-win](https://github.com/pyenv-win/pyenv-win.git):
    
    ```bash
    git clone https://github.com/pyenv-win/pyenv-win.git ~/.pyenv
    ```

    For more details on installing `pyenv` on other operating systems, check the official [pyenv installation guide](https://github.com/pyenv/pyenv).

2. **Install a specific Python version (if needed):**

    ```bash
    pyenv install 3.8.10
    pyenv global 3.8.10
    ```

3. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

### Installing Dependencies

1. **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

    Alternatively, you can manually install the packages:

    ```bash
    pip install Flask
    pip install pillow
    pip install flask-cors
    ```

### Running the Application

1. **Clone the repository:**

    ```bash
    git clone https://github.com/aimeelramirez/ image-to-knit-or-crochet-pattern-app.git
    cd  image-to-knit-or-crochet-pattern-app
    ```

2. **Run the Flask app:**

    ```bash
    python app.py
    ```

3. **Open your browser and go to:**

    ```
    http://127.0.0.1:5000/
    ```




Docker
# Build the Docker image
docker build -t web .

# Run the Docker container
docker run -d -p 5000:5000 web

# Check the logs to ensure the Flask app started correctly
docker logs $(docker ps -q --filter "ancestor=web")
