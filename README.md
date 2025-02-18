WhatsApp Chat Analyzer 📱📊
Overview

WhatsApp Chat Analyzer is a Python-based tool that helps users extract valuable insights from their WhatsApp conversations. Using Streamlit for the web interface, the application provides interactive data visualizations to display the frequency of words, messages over time, and other analytical metrics that give users a better understanding of their chats.
Features ✨

    Word Frequency Analysis: Visualizes the most common words in the chat. 📝
    Message Count Over Time: Displays the distribution of messages over different time periods. ⏳
    User Interactions: Identifies how frequently each participant is engaging in the conversation. 🗣️
    Interactive Visualizations: Use of Streamlit to display dynamic graphs like word clouds, bar charts, etc. 📈
    Customizable Input: Users can upload their WhatsApp chat exports and customize analysis parameters. 🔧

Installation 🛠️
Prerequisites

Make sure you have the following libraries installed:

    Python 3.x 🐍
    Streamlit 🌟
    Pandas 📊
    NumPy 🔢
    Matplotlib 📈
    WordCloud (optional for visualizing word frequencies) ☁️

Install Dependencies

pip install -r requirements.txt

Running the Application 🚀

To run the application locally, use Streamlit:

streamlit run app.py

This will start a local web server, and you can access the app through your browser. 🌐
Usage 💻

    Upload WhatsApp Chat: Export your chat from WhatsApp (preferably in .txt format) and upload it into the app. 📤
    Select Analysis Options: Choose the types of analysis you want to perform on the chat data, such as word frequency or message counts over time. 📅
    View Results: The tool will process the data and display the results with interactive visualizations. 🎨

Example Screenshots 📸

[Add some screenshots of the app displaying the analysis results]
Project Structure 📂

    app.py: Main Streamlit application file.
    chat_analyzer.py: Python script for analyzing WhatsApp chat data.
    requirements.txt: List of dependencies required to run the project.
    README.md: Documentation for the project.

Contributing 🤝

If you'd like to contribute to this project, feel free to fork the repository, make changes, and submit a pull request. 💡
License 📜

This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments 🙏

    Thanks to Streamlit for the awesome framework.
    Data used in this project comes from WhatsApp exported chat files. 💬
    Special thanks to Kaggle for providing the datasets used for testing and training in certain cases. 📊
