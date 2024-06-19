Dick Language Interpreter

This is an interpreter for the esoteric programming language Dick, which was created by User Cybertelx on December 5, 2020. This interpreter is coded in Python 3.10 and uses structural pattern matching introduced in Python 3.10.


Credits

Language Creator: The Dick language was created by Cybertelx.

Source Code: This interpreter is based on the source code provided by boopdev.

Requirements


Python 3.10 or higher


Usage

You can run Dick language code by using the dick.py file. Only one argument is required: the path to the Dick language file.


Command Line Usage

To run the interpreter, use the following command:

python3 dick.py <path_to_dicklang_file>



Example

Create a file named example.dick with the following content:

DICK dick 8==D

GRAB dick

LONGDICK 8=D

PEE

RELEASE dick


Run the interpreter:

python3 dick.py example.dick

Expected Output

PEE: 8===D


Files Required

To use this interpreter, you need the following two files: dick.py and interp.py. Add the code for these files as given.


License
This project is open-source and available under the MIT License.


