import re

def maskOutWords(text, replace_with):
    for word in replace_with:
        try:
            match = re.search("(" + word + ")", text, re.IGNORECASE)
            match = match.groups()
            replace_word = '*' * len(match[0])
            text = text.replace(match[0], replace_word)
        except Exception:
            continue

    return text



words = ["yesterday", "Dog", "food", "walk"]
text = "Yesterday, I took my dog for a walk.\n It was crazy! My dog wanted only food."

print maskOutWords(text, words)
