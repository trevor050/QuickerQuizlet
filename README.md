# QuickerQuizlet 1.1.0
A faster way of creating Quizlet imports for translation

# How to use
If you have a list of words you need to translate into a quizlet document this allows you to create it instanly. Run main.py with googletrans installed. To install googletrans use "pip install googletrans==4.0.0-rc1", that version in specific. In the terminal and then paste your quizlet code. On a newline type --stop to stop. It then should print a string you can import to Quizlet

# Importing to Quizlet
When creating a new set you should see a "+ Import from Word, Excel, Google Docs, etc." near the top. Click it, then select comma, and makesure new line is selected. Then paste the output from the python script and click import. Your all done with no hassle! 

# Other Features
- NoParentheses: Toggleable. Enabled (Defualt): Desear (+ infinitive), To wish.  Disabled: Desear (+infinitive), To wish (+infinitive)
- EasyTxt: You will be prompted if you would like to make a texrt file with the results. If you already have a textfile it will be overwritten! Textfiles are outputted in the folder that the main.py is inside.
