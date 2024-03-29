# QuickerQuizlet 2.0.2 🚀
Your go-to tool for creating Quizlet sets just got faster, smarter, and even easier to use.

## What's New in 2.0? 🎉
- Much Faster: Up to 10x faster in optimal conditions. 
- Tons of Customization: Tailor your experience with advanced user settings.
- Import from File: Got a list? We can handle it.
- Fat-Finger Protection: A more forgiving --stop for when your fingers have a mind of their own.
- Code Glow-Up: Refactored, polished, and looking sharp.

A faster way of creating Quizlet imports for translation

## Usage
If you have a list of words you need to translate into a quizlet document this allows you to create it instanly. Run main.py with googletrans installed In the terminal and then paste your quizlet code. On a newline type --stop to stop.

## Importing to Quizlet
When creating a new set you should see a "+ Import from Word, Excel, Google Docs, etc." near the top. Click it, then select comma, and makesure new line is selected. Then paste the output from the python script and click import. You're all done with no hassle! 

## Other Features
- No Parentheses: Toggleable. Enabled (Defualt): Desear (+ infinitive), To wish.  Disabled: Desear (+infinitive), To wish (+infinitive)
- Quick Text File: You will be prompted if you would like to make a text file with the results. If you already have a textfile it will be overwritten! Textfiles are outputted in the folder that the main.py is inside.
- Extreme Speed Mode: Got a lot of text? No problem Extreme Speed Mode can multithread for faster speed (Disabled by default. Rate limiting possible though I have not encountered it)
- Efficiency Mode: Avoids unnecessary API calls. The more you use QuickerQuizlet the faster it gets! 


# Getting Started

These instructions will guide you through the process of using the QuickerQuizlet script to quickly and easily translate a list of words and import them into Quizlet.

## Prerequisites
- Python 3.x: You will need to have Python 3.x installed on your computer to run this script. You can download it from the [Offical Website](https://www.python.org "Python Site")
- Googletrans library: The script uses the googletrans library to translate the words. You can install it using the command "pip install googletrans==4.0.0-rc1" in your command line.

## Installing / Basic Usage
- Download the QuickerQuizlet script by clicking the "Clone or download" button on the GitHub repository and selecting "Download ZIP".
- Unzip the downloaded file and navigate to the unzipped folder in your command line.
- Run the command "pip install googletrans==4.0.0-rc1" to install the googletrans library.
- Open your command line and navigate to the folder where you unzipped the QuickerQuizlet script.
- Run the command "python main.py" to start the script.
- In the terminal, paste a list of words you want to translate, with each word on a new line. Type "--stop" on a new line to indicate the end of the list.
- The script will proceed to translate the words, and put it in quizlet format
- You will be prompted if you would like to make a text file with the results. If you already have a textfile it will be overwritten! Textfiles are outputted in the folder that the main.py is inside.

## Troubleshooting
- Cannot connect to the internet: Make sure your device is online and try running the script again.
- Error installing googletrans library: Make sure you are running the command "pip install googletrans==4.0.0-rc1" in the correct command line and that you have the latest version of Python installed.
- Error running the script: Make sure you are running the command "python main.py" in the correct folder and that you have the necessary dependencies installed.
- Any other problems feel free to make an issue request, or if you have an enchanment/idea
