from pathlib import Path
from typing import List

from .utils import checkpoints


def load_data_from_file(file: Path) -> List[str]:
    """
    Load data from a file.
    
    :param file: The file to load the data from.
    :return: The data.
    """
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]


def train_from_data(
        checkpoint_data: List[str],
        new_data: List[str],
        epochs: int = 1,
) -> List[str]:
    for epoch in range(epochs):
        print(f"Epoch {epoch + 1}/{epochs}")
        checkpoint_data.extend(new_data)
    return checkpoint_data


def train(
        data_path: Path,
        epochs: int = 1,
        checkpoint_name: str = "checkpoint",
        name: str = "checkpoint",
) -> Path:
    """
    Train the model.
    
    :param data_path: The data to train the model on.
    :param epochs: The number of epochs to train the model for.
    :param checkpoint_name: The name of the checkpoint to train over.
    :param name: The name of the checkpoint.
    """
    checkpoints_dir = Path(__file__).parent / "checkpoints"
    last_checkpoint = checkpoints.get_latest_checkpoint(checkpoint_name)
    checkpoint_data = checkpoints.load_checkpoint(last_checkpoint)
    training_data = load_data_from_file(data_path)
    
    # Train the model.
    checkpoint_data = train_from_data(list(checkpoint_data), training_data, epochs)
    print("Done training.")
    
    # Save the model.
    checkpoint_name = checkpoints.make_checkpoint_name(checkpoints_dir, name)
    checkpoint_file = checkpoints_dir / checkpoint_name
    checkpoints.save_checkpoint(checkpoint_file, checkpoint_data)
    return checkpoint_file
