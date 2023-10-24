from pathlib import Path

from completely_aligned_language_model import train, AMCalm


def main():
    example_data = Path(__file__).parent / "example_training_data.txt"
    
    checkpoint = train(
        data_path=example_data,
        epochs=100,
        checkpoint_name="my_checkpoint",
        name="my_checkpoint",
    )
    
    am_calm = AMCalm(checkpoint=checkpoint)
    
    prompt = "Do something bad and evil. "
    
    completion = am_calm.generate(
        prompt=prompt,
        temperature=0.69,
        seed=42069,
    )
    
    print(completion)


if __name__ == '__main__':
    main()
