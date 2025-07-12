# PowerShell script to add, commit, and push changes to GitHub
# Usage: Run this script from the project root in PowerShell

# Stage all changes
git add .

# Commit with a default message
git commit -m "Update: font size, dashboard spacing, and header enhancements"

# Push to the main branch
git push origin main 