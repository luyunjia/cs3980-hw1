def echo(text: str, repetitions: int = 3) -> str:
    result = ''
    for i in range(repetitions, 0, -1):
        result += text[-i:] + '\n'
    return result

if __name__ == "__main__":
    user_input = input("Yell something at a mountain: ")
    print(echo(user_input))