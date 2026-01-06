#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ScholarOCR - Study notes extraction tool.
Environment: Linux (Ubuntu)
"""

import pytesseract
from PIL import Image
from pathlib import Path
import sys

# CONFIGURATION
# Define the base directory relative to this script
BASE_DIR = Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR / "images"
OUTPUT_DIR = BASE_DIR / "output"

# Create directories if they do not exist
INPUT_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

def extract_text(image_name, language='por'):
    """
    Main function to read the image and save the text.
    """
    image_path = INPUT_DIR / image_name
    
    # Check if image exists
    if not image_path.exists():
        print(f"Error: File '{image_name}' not found in {INPUT_DIR}")
        return

    try:
        print(f"Processing: {image_name}...")
        
        # Load image
        img = Image.open(image_path)
        
        # EXTRACTION (Tesseract)
        text = pytesseract.image_to_string(img, lang=language)
        
        # Save result
        text_filename = image_path.stem + ".txt"
        output_path = OUTPUT_DIR / text_filename
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)
            
        print(f"Success! Text saved to: {output_path}")
        
    except Exception as e:
        print(f"Error processing file: {e}")

# Main execution block
if __name__ == "__main__":
    # List all files in the images directory
    files = list(INPUT_DIR.glob("*.*"))
    
    if not files:
        print("The 'images' folder is empty. Add files to test.")
    else:
        for file in files:
            # Filter for valid image formats
            if file.suffix.lower() in ['.jpg', '.png', '.jpeg', '.pdf']:
                extract_text(file.name)
