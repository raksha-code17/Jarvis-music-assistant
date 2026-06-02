# Jarvis Music Assistant
A simple Python voice assistant that can:

* Open websites
* Play songs from a custom music library
* Listen for voice commands using speech recognition
* Speak responses using text-to-speech

## Features

* Wake word activation using `"Jarvis"`
* Open:

  * Google
  * YouTube
  * LinkedIn
  * Instagram
* Play songs from a predefined music library
* Voice response system

## Technologies Used

* Python
* SpeechRecognition
* pyttsx3
* PyAudio
* Webbrowser

## Installation

Install required packages:
pip install SpeechRecognition pyttsx3 pyaudio pygame

## Project Structure

├── main.py
├── musiclibrary.py
├── README.md


## How to Run

Run the Python file:
python main.py

Say:
Jarvis

Then give commands like:
Open YouTube
Play samjhawan

## Example Music Library

music = {
    "pehli mohabbat":"https://youtu.be/Gq2hcE4V7Jo?si=FAv0O4t_zNPjIXLc",
    "samjhawan" : "https://youtu.be/H2f7MZaw3Yo?si=IfHV3jJcCW80Sxnj"
}

## Future Improvements

* AI chatbot integration
* Weather updates
* WhatsApp messaging
* App launching
* GUI interface

## Author
Made by Raksha Gajeshwar
