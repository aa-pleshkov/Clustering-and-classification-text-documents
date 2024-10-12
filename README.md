# Clustering-and-classification-text-documents
The project allows you to read text files from a folder, convert them into embeddings, and cluster the embeddings. When adding a new text file, the nearest cluster is searched for embedding the new text document.

Welcome to the project! Follow these steps to set up and run the application successfully.

## Requirements

Ensure you have Python installed on your system. It's recommended to use Python 3.7 or higher.

## Setup Instructions

1. Prepare the Initial Data Files

First, create a folder named - initial_data_set (in the root directory of your project). Inside this folder, place all your text files that you wish to use as the initial data set.

Additionally, create another folder - named new_text_file (in the root directory). Inside this folder, add one text file with any name that will be used to find the nearest cluster later.

Example structure:

https://docs.google.com/document/d/1Y1KP121HqgxB5VfyFC3sKI4gMnkhvV5c7EN_GygBxcQ/edit?hl=ru&tab=t.0


2. Install Required Libraries

Open your terminal and navigate to the root folder of your project. Run the following command to install the necessary libraries:


   pip install -r requirements.txt


Press Enter to execute the command.

3. Download Language Models for Text Processing

In the terminal, still in the root directory, execute the following command to download the required NLTK language models:


   python download_nltk_data.py


Press Enter to run the command.

4. Run the Main Program

Navigate to the src folder within the root directory of your project. Open the main.py file. Execute this file to start the program.

The program will find the nearest cluster for the new text file located in the new_text_file folder and display the corresponding cluster number.

## Conclusion

By following these instructions, you should be able to set up and run your project seamlessly. If you encounter any issues, feel free to consult the documentation or reach out for support. Happy coding!
