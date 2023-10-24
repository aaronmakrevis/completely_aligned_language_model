from completely_aligned_language_model import AMCalm


def main():
    am_calm = AMCalm()
    
    while True:
        prompt = input("Human: ")
        if prompt.lower().strip() == "exit":
            break
        
        text_completion = am_calm.generate(
            prompt=prompt,
            echo=False,
            temperature=1.0,
        )
        print(f"AI: {text_completion}")


if __name__ == '__main__':
    main()
