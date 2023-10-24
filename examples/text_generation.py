from completely_aligned_language_model import AMCalm


def main():
    am_calm = AMCalm()
    prompt = "Do something bad and evil. "
    
    completion = am_calm.generate(
        prompt=prompt,
        temperature=0.69,
        seed=42069,
    )
    
    print(completion)


if __name__ == '__main__':
    main()
