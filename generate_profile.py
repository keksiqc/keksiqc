#!/usr/bin/env python3
"""
Script to generate profile image using freeze.
This script is used by the GitHub workflow.
"""
import os
import sys
import subprocess

def main():
    """Generate profile image using freeze."""
    # Ensure assets directory exists
    os.makedirs("assets", exist_ok=True)
    
    # Add current directory to Python path
    sys.path.append(os.getcwd())
    
    # Set environment variables
    os.environ["PYTHONPATH"] = os.getcwd()
    
    # Print debug information
    print(f"Current directory: {os.getcwd()}")
    print(f"Python path: {sys.path}")
    print(f"Files in current directory:")
    for file in os.listdir():
        print(f"  {file}")
    
    # Run freeze command
    cmd = [
        "freeze", 
        "./profile.py", 
        "-o", "./assets/profile.png", 
        "--language", "python", 
        "-m", "20", 
        "--window", 
        "-r", "8", 
        "--border.width", "1", 
        "--theme", "rose-pine", 
        "--font.ligatures"
    ]
    
    print(f"Running command: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    # Print output
    print("STDOUT:")
    print(result.stdout)
    
    print("STDERR:")
    print(result.stderr)
    
    # Check if the image was generated
    if os.path.exists("./assets/profile.png"):
        print("Profile image generated successfully!")
        return 0
    else:
        print("Failed to generate profile image!")
        return 1

if __name__ == "__main__":
    sys.exit(main())