from babel.numbers import format_decimal
import re


class Tafqit:
    """
    A class to convert numbers to text representation in various locales.
    """

    @staticmethod
    def convert_arabic_numbers_to_english(number):
        """
        Converts Arabic numerals to English numerals.
        """
        arabic_to_english = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")
        return str(number).translate(arabic_to_english)

    @staticmethod
    def number_to_text(number, locale="en"):
        """
        Converts a number into its textual representation.
        
        :param number: The number to convert
        :param locale: The locale for conversion (e.g., 'en', 'ar')
        :return: The textual representation of the number
        """
        try:
            # Ensure the number is in English numerals
            number = Tafqit.convert_arabic_numbers_to_english(number)

            if not re.match(r"^-?\d+(\.\d+)?$", number):
                raise ValueError("Invalid number format.")

            # Convert to text using Babel's format_decimal
            formatted_number = format_decimal(float(number), locale=locale)
            return formatted_number
        except Exception as e:
            raise ValueError(f"Error converting number: {e}")
