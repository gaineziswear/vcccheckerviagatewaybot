#!/bin/bash
# setup_and_push.sh

echo "=== VCC Checker GitHub Setup ==="

# Configuration
REPO_NAME="vcccheckerviagatewaybot"
GITHUB_USERNAME="gaineziswear"
PROJECT_DIR=$(pwd)

echo "Current directory: $PROJECT_DIR"

# Step 1: Initialize Git
echo "Step 1: Initializing Git repository..."
if [ ! -d ".git" ]; then
    git init
    echo "✓ Git initialized"
else
    echo "✓ Git already initialized"
fi

# Step 2: Create .gitignore if not exists
echo "Step 2: Setting up .gitignore..."
if [ ! -f ".gitignore" ]; then
    cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Environment
.env
.venv
env/
venv/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# Logs
*.log
logs/

# Data
data/sensitive/
*.csv
*.json

# OS
.DS_Store
Thumbs.db

# Temporary files
*.tmp
*.temp

# Security
*.key
*.pem
*cert*
*private*
config/production.yaml
EOF
    echo "✓ .gitignore created"
else
    echo "✓ .gitignore already exists"
fi

# Step 3: Add files to git
echo "Step 3: Adding files to Git..."
git add .

# Step 4: Make initial commit
echo "Step 4: Creating initial commit..."
git commit -m "Initial commit: Complete VCC Checker via Gateway Bot system

Features included:
- Quantum-inspired card generation
- Multi-gateway testing (Nexus, Stripe, PayPal, etc.)
- Bank-level security monitoring
- Ternary logic pattern detection
- API server with FastAPI
- Comprehensive testing suite
- Docker configuration
- CI/CD workflows"

echo "✓ Commit created"

# Step 5: Check if remote exists
echo "Step 5: Setting up remote repository..."
if git remote | grep -q "origin"; then
    echo "✓ Remote origin already exists"
else
    git remote add origin https://github.com/$GITHUB_USERNAME/$REPO_NAME.git
    echo "✓ Remote origin added"
fi

# Step 6: Push to GitHub
echo "Step 6: Pushing to GitHub..."
git branch -M main
git push -u origin main

echo "=== Setup Complete ==="
echo "Repository available at: https://github.com/$GITHUB_USERNAME/$REPO_NAME"