# hack_x_2025
Build agentic app for book
# Flask Application Setup Guide

## Prerequisites
Ensure you have the following installed on your system:
- Python 3.x
- pip (Python package manager)
- Virtual environment (recommended)
- OpenAI API key (set as an environment variable)

## Installation and Setup

### Windows
1. **Open Command Prompt or PowerShell**
2. **Navigate to your project directory**:
   ```sh
   cd path\to\your\flask-app
   ```
3. **Create and activate a virtual environment**:
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```
4. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

5. **Set the OpenAI API key**:
   ```sh
   set OPENAI_API_KEY=your_openai_api_key_here
   ```
6. **Run the Flask app**:
   ```sh
   python app.py
   ```

### Linux & Mac
1. **Open Terminal**
2. **Navigate to your project directory**:
   ```sh
   cd /path/to/your/flask-app
   ```
3. **Create and activate a virtual environment**:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
4. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```
5. **Set the OpenAI API key**:
   ```sh
   export OPENAI_API_KEY=your_openai_api_key_here
   ```
6. **Run the Flask app**:
   ```sh
   python app.py
   ```

## Running the App
Once the application is running, you should see output similar to:
```sh
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
Open a browser and navigate to `http://127.0.0.1:5000/` to access the app.

## Troubleshooting
- If `pip` is not found, try `python -m pip` instead.
- Ensure the correct Python version is used (`python3` instead of `python` on some systems).
- Verify that the OpenAI API key is correctly set by running `echo $OPENAI_API_KEY` (Linux/Mac) or `echo %OPENAI_API_KEY%` (Windows).

---
## Datset 
Data retrieved from [https://cseweb.ucsd.edu/~jmcauley/datasets/goodreads.html](Goodreads book graph dataset)
Mengting Wan, Julian McAuley, "Item Recommendation on Monotonic Behavior Chains", in RecSys'18. [bibtex]
Mengting Wan, Rishabh Misra, Ndapa Nakashole, Julian McAuley, "Fine-Grained Spoiler Detection from Large-Scale Review Corpora", in ACL'19. [bibtex]


