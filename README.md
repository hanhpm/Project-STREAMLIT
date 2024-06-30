# PROJECT-STREAMLIT

This project includes basic applications such as word correction, object detection, and chatbot.

## Setup Instructions

To set up the environment and run the applications, follow these detailed steps:

### Step 1: Download and Install Anaconda

1. Download the Anaconda distribution from the [official website](https://www.anaconda.com/products/distribution).
2. Follow the installation instructions provided on the website to install Anaconda on your system.

### Step 2: Create Anaconda Environment

1. Open the Anaconda Prompt (you can find this in the Start Menu after installing Anaconda).
2. Create a new environment named `streamlit_env` by running the following command:

    ```bash
    conda create --name streamlit_env python=3.8
    ```

3. Activate the newly created environment:

    ```bash
    conda activate streamlit_env
    ```

### Step 3: Install Necessary Libraries

Install the required libraries for the project using the following commands:

```bash
conda install streamlit
conda install -c conda-forge levenshtein
conda install -c anaconda tensorflow
```

### Step 4: Running the Applications

Each application can be run separately using specific commands in the Anaconda Prompt.

#### Running the Chatbot Application

1. Navigate to the directory where `chatbot.py` is located.
2. Run the Streamlit application with the following command:

    ```bash
    streamlit run chatbot.py
    ```

#### Running the Levenshtein Distance Application

1. Navigate to the directory where `levenshtein-distance.py` is located.
2. Run the Streamlit application with the following command:

    ```bash
    streamlit run levenshtein-distance.py
    ```

#### Running the Object Detection Application

1. Navigate to the directory where `object-detection.py` is located.
2. Run the Python script with the following command:

    ```bash
    python object-detection.py
    ```

### Summary

- **Chatbot Application:** `streamlit run chatbot.py`
- **Levenshtein Distance Application:** `streamlit run levenshtein-distance.py`
- **Object Detection Application:** `python object-detection.py`

By following these instructions, you should be able to set up the Anaconda environment and run each of the applications in this project. If you encounter any issues or need further assistance, please refer to the documentation or contact the project maintainer.

### Notes

- Ensure that your Anaconda environment is activated before running any commands.
- Update your environment and packages regularly to avoid compatibility issues.
- For advanced configuration and troubleshooting, refer to the [Anaconda documentation](https://docs.anaconda.com/).

Happy coding!
