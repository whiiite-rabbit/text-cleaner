# Text Cleaner

A simple Python utility to clean and format raw user input strings.

## Features

- Removes leading and trailing whitespace
- Removes all exclamation marks
- Converts text to lowercase
- Capitalizes the first letter of the sentence

## Example

```python
from cleaner import clean_input

raw_text = "   ПРИВЕТ, Я НОВИЧОК В PYTHON!!!   "
cleaned = clean_input(raw_text)
print(cleaned)
# Output: "Привет, я новичок в python"
