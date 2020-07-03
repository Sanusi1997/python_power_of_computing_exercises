def chat_length():
    message = input("Please enter your message: ")
    if len(message) < 160:
        result = print(message)
        return result
    else:
        result = print(message[:161])
        return result


chat_length()
