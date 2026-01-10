# ScholarOCR

ScholarOCR is an open-source Python tool designed to extract text from images and PDFs. It utilizes Tesseract OCR to convert study materials into editable text, helping students organize their notes efficiently.

## Features

- Automatic text extraction from images (.png, .jpg, .jpeg) and PDFs.
- Automatic directory management for input and output files.
- Optimized for Linux (Ubuntu) environments.
- Simple codebase, easy to extend or modify.

  
## Installation

1. Clone the repository:

   ```bash
   git clone [https://github.com/evedmills/scholar-ocr.git](https://github.com/evedmills/scholar-ocr.git)
   cd scholar-ocr 
`
2. Install the Python dependencies: 

```bash
p install -r REQUIREMENTS.TXT
```

 ## Prerequisites

Since this tool relies on Tesseract OCR, you must install the engine on your system before running the Python script.

**For Ubuntu / Debian:**

```bash
sudo apt update
sudo apt install tesseract-ocr tesseract-ocr-por libtesseract-dev
