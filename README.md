# Tafqit (Python):  Convert Numbers to Words in Arabic

Tafqit-Python is a lightweight and modular Python service designed to convert numerical values into their textual representation. The service currently supports Arabic and English and offers a flexible foundation for extending to additional languages.

---

## 🚀 Features

- **Multi-Language Support:** Out-of-the-box support for Arabic and English.
- **Arabic Number Conversion:** Converts integers into grammatically correct Arabic words.
- **Customizable:** Modular design for adding support for other languages.
- **Lightweight and Efficient:** Designed with simplicity and performance in mind.


## ⚙️ Requirements

- Python 3.6 or higher.


## 🔧 Installation

To use Tafqit-Python, clone the repository to your local machine:

```bash
git clone https://github.com/m-ah07/tafqit-python.git
cd tafqit-python
```


## 📖 Usage

Here’s a simple example of how to use Tafqit-Python:

```bash
from src.tafqit import Tafqit

# Create an instance of the Tafqit class
tafqit = Tafqit()

# Convert a number to Arabic text
number = 12345
arabic_result = tafqit.convert_to_words(number, language="ar")
print(f"Number in Arabic: {arabic_result}")

# Convert a number to English text
english_result = tafqit.convert_to_words(number, language="en")
print(f"Number in English: {english_result}")
```


## 📂 Directory Structure
```plaintext
tafqit-python/
├── src/
│   ├── tafqit.py
│   └── __init__.py
├── examples/
│   └── example.py
├── tests/
│   └── test_tafqit.py
├── LICENSE
├── README.md
└── requirements.txt
```

## Tests

Run the following command to execute the tests:

```bash
pytest tests/test_tafqit.py
```

## 🛠️ Contributing

Contributions are welcome! Here's how you can get involved:

- Fork the repository.
- Create a new branch `git checkout -b feature-branch`.
- Commit your changes `git commit -m "Add new feature"`.
- Push to the branch `git push origin feature-branch`.
- Open a Pull Request.

## 🌟 Show Your Support
If you found this project helpful, please consider giving it a ⭐ on GitHub. Your support means the world to us!
















