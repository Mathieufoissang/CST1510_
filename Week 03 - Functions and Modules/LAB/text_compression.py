"""Compress consecutive repeated characters when it saves space."""


def compress_string(text):
    if text == "":
        return text

    compressed = ""
    current_character = text[0]
    count = 1

    for character in text[1:]:
        if character == current_character:
            count += 1
        else:
            compressed += current_character + str(count)
            current_character = character
            count = 1

    compressed += current_character + str(count)
    if len(compressed) > len(text):
        return text
    return compressed


if __name__ == "__main__":
    user_text = input("Enter text to compress: ")
    print(compress_string(user_text))
