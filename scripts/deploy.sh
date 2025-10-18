#!/bin/bash
# scripts/deploy.sh

echo "Starting VCC Checker Deployment..."

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "Git is not installed. Please install git first."
    exit 1
fi

# Configuration
REPO_URL="https://github.com/gaineziswear/vcccheckerviagatewaybot.git"
TEMP_DIR="./vcccheckerviagatewaybot-temp"
TARGET_DIR="./vcccheckerviagatewaybot"

# Clone repository
echo "Cloning repository..."
git clone $REPO_URL $TEMP_DIR

# Check if clone was successful
if [ $? -ne 0 ]; then
    echo "Failed to clone repository. Please check your credentials and repository URL."
    exit 1
fi

# Copy files to target directory
echo "Setting up application..."
cp -r $TEMP_DIR/* $TARGET_DIR/
cp $TEMP_DIR/.gitignore $TARGET_DIR/

# Cleanup
rm -rf $TEMP_DIR

# Setup virtual environment
echo "Setting up Python environment..."
cd $TARGET_DIR
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Setup environment
cp .env.example .env
echo "Please edit .env file with your configuration"

# Make scripts executable
chmod +x scripts/*.sh

echo "Deployment completed successfully!"
echo "Next steps:"
echo "1. Edit .env file with your configuration"
echo "2. Run: source venv/bin/activate"
echo "3. Run: python main.py"