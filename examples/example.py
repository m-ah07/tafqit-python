from src.tafqit import Tafqit

# Create an instance of the Tafqit class
tafqit = Tafqit()

# Example: Arabic numerals
arabic_number = "٢٣٤٥"
text_in_arabic = tafqit.number_to_text(arabic_number, locale="ar")
print(f"Arabic Text: {text_in_arabic}")

# Example: English numerals
english_number = "2345"
text_in_english = tafqit.number_to_text(english_number, locale="en")
print(f"English Text: {text_in_english}")
