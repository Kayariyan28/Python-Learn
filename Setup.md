# Complete Setup Guide for Python Journey Curriculum

Setting up this Python curriculum project requires a few steps to ensure you have the right environment. I'll walk you through the entire process from start to finish on your Mac.

## Prerequisites

Before beginning, you'll need:

1. macOS terminal access
2. Internet connection
3. Basic familiarity with terminal commands

## Step 1: Install Python (if not already installed)

First, check if Python is already installed:

```bash
python3 --version
```

If Python 3.7+ isn't installed or you need to update:

1. Install Homebrew (if not already installed):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. Install Python using Homebrew:
   ```bash
   brew install python
   ```

## Step 2: Set Up a Project Directory

```bash
# Create a directory for your Python learning projects
mkdir ~/PythonProjects
cd ~/PythonProjects
```

## Step 3: Clone the Repository

```bash
git clone https://github.com/Kayariyan28/Python-Learn.git
cd Python-Learn
```

## Step 4: Create a Virtual Environment

Virtual environments keep your project dependencies isolated:

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate
```

Your terminal prompt should now show `(venv)` indicating the environment is active.

## Step 5: Install Required Packages

```bash
# Upgrade pip
pip install --upgrade pip

# Install Jupyter and other essential packages
pip install jupyter numpy pandas matplotlib seaborn scikit-learn flask requests

# For later realms, you might need additional packages
pip install pygame opencv-python nltk tensorflow
```

## Step 6: Set Up Jupyter Notebook

```bash
# Install Jupyter if not included in previous step
pip install jupyter

# Create a Jupyter kernel for your virtual environment
python -m ipykernel install --user --name=python-journey
```

## Step 7: Start Jupyter Notebook

```bash
jupyter notebook
```

This will open Jupyter in your default web browser. Navigate to the first realm:

1. Click on `realm_1`
2. Click on `module_1`
3. Click on `lessons`
4. Open the first notebook

## Step 8: Google Colab Setup (Alternative)

If you prefer using Google Colab:

1. Go to [Google Colab](https://colab.research.google.com)
2. Sign in with your Google account
3. Click on "File" → "Open notebook"
4. Select the "GitHub" tab
5. Enter the repository URL: `https://github.com/Kayariyan28/Python-Learn`
6. Choose the notebook you want to open

## Step 9: Create a Requirements File

For easier environment sharing or reinstallation:

```bash
# Make sure your virtual environment is activated
pip freeze > requirements.txt
```

## Step 10: Setting Up Visual Studio Code (Optional)

For a more powerful development environment:

1. Install VS Code from [code.visualstudio.com](https://code.visualstudio.com)
2. Install the Python extension in VS Code
3. Open VS Code and open the Python-Learn folder
4. Select your virtual environment as the Python interpreter

## Starting Your Learning Journey

Now that your environment is set up:

1. Begin with Realm 1: Python Foundations
2. Work through the modules sequentially
3. Complete exercises in each module
4. Work on the project quests to reinforce your learning
5. Track your progress through the different realms

Remember to keep your virtual environment activated whenever working on this project:

```bash
# To activate
source venv/bin/activate

# To deactivate when done
deactivate
```

This setup provides everything you need to work through the entire Python Journey curriculum, from the beginner "Explorer's Beginnings" to the advanced "Master's Path."