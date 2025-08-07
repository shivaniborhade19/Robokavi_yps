

# RoboKavi-CoreXY machine with an AI computer 
![RoboKavi Demo](demo.gif.gif)

<p align="center">
  <a href="https://yeralaproject.org/robokavi/"><img src="https://img.shields.io/badge/Website-Live-blue?style=flat-square" /></a>
  <a href="https://github.com/shivaniborhade19/Robokavi_yps"><img src="https://img.shields.io/badge/GitHub-Repository-green?style=flat-square" /></a>
  <a href="https://yeralaproject.org/robokavi/docs"><img src="https://img.shields.io/badge/Documentation-Available-orange?style=flat-square" /></a>
</p>

---
["मराठीत वाचा"](README_MR.md)

## Project Description


ROBOKAVI is an innovative project that seamlessly integrates Artificial Intelligence (AI) with robotic plotting technology to transform digital text into personalized, physical handwriting. Leveraging Google Gemini's capabilities for poem generation and a 2D plotter for physical transcription, ROBOKAVI aims to demystify advanced technologies and offer a tangible, engaging experience for users interested in AI, robotics, and creative computing. It currently supports poem generation and plotting in both English and Marathi (Devanagari script).


## Features


* **AI-Generated Poetry:** Utilizes the Google Gemini API to generate original poems based on user prompts.

* **Multilingual Support:** Capable of generating and plotting poems in both English and Marathi languages.

* **SVG Conversion:** Converts generated text into Scalable Vector Graphics (SVG) format using Inkscape for precise plotter control.

* **Robotic Handwriting:** Employs a 2D plotter (based on the EasyDraw V3 system) to physically transcribe poems with a pen.

* **Tangible Output:** Creates unique, handwritten physical outputs, bridging the gap between digital and physical realms.


## Prerequisites


Before setting up the project, ensure you have the following installed on your system:


* **Python 3.8+**

* **pip** (Python package installer)

* **Inkscape:** A vector graphics editor, required for converting text to SVG.

    * Download from: [https://inkscape.org/release/](https://inkscape.org/release/)

    * Ensure Inkscape's Command Line Interface (CLI) is accessible.

* **Gemini_API_Key:**  Replace YOUR_API_KEY_HERE with your actual Gemini API key.


## Setup and Installation Guide


Follow these steps to get ROBOKAVI up and running on your local machine:




**1. Clone the project repository to your local machine:**

```bash
git clone https://github.com/shivaniborhade19/Robokavi_yps.git
cd Robokavi
```

**2. Create and Activate a Virtual Environment:**

It's highly recommended to use a virtual environment to manage dependencies:

```bash
python -m venv venv
```
 On Windows
```bash
.\venv\Scripts\activate
```
 On macOS/Linux
```bash
source venv/bin/activate
```

**3. Install Python Dependencies:**


Install all required Python libraries using the requirements.txt file:
```bash
pip install -r requirements.txt
```

**4. Configure Inkscape CLI Path**

The project uses Inkscape's command-line interface to convert text to SVG. You need to ensure the svg_creator.py script knows where to find Inkscape's executable. Open the svg_creator.py file in your project directory. Locate the line where Inkscape's path is defined (it might be a variable like INKSCAPE_PATH or part of a subprocess.run command). Update this path to point to your Inkscape executable.

Windows Example:
```bash
 r'C:\Program Files\Inkscape\bin\inkscape.exe'
  ```
macOS Example:
```bash
/Applications/Inkscape.app/Contents/MacOS/inkscape
 ```
Linux Example: 
```bash
/usr/bin/inkscape (often in PATH by default)
 ```

**5. Set Up Google Gemini API Key:**

The project requires an API key to access the Google Gemini service for poem generation.  
Obtain your Gemini API key from the Google AI Studio: https://aistudio.google.com/

Create a file named `.env` in the root directory of your project (the same directory as your main script, e.g., `main.py`).

Add your API key to this `.env` file in the following format:

GEMINI_API_KEY=YOUR_API_KEY_HERE

(Replace `YOUR_API_KEY_HERE` with your actual Gemini API key.)

Important: Ensure your `.gitignore` file includes `.env` to prevent your API key from being accidentally committed to your public repository.



**How to Run the Project**

Once all prerequisites and setup steps are complete:

- Ensure your 2D plotter is connected to your computer via USB and powered on.  
- Activate your virtual environment (if not already active).

 Run your main project script (e.g., app.py):
```bash         
 python app.py
 ```
# More Information
For photos of the RoboKavi hardware, live demo videos, and detailed documentation, visit the official project page:

- [https://yeralaproject.org/robokavi/](https://yeralaproject.org/robokavi/)
