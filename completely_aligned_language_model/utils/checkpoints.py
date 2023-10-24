import re
from pathlib import Path
from typing import List, Tuple, Union


def get_latest_checkpoint(filename: str = "checkpoint") -> Path:
    """
    Get the latest checkpoint file.
    
    :return: The latest checkpoint file.
    """
    checkpoints_dir = Path(__file__).parent.parent / "checkpoints"
    checkpoints = sorted(list(checkpoints_dir.glob(f"{filename}_*.txt")))
    return checkpoints[-1] if checkpoints else None


def load_checkpoint_from_file(checkpoint_path: Path) -> Tuple[str]:
    """
    Load a checkpoint from a file.
    
    :param checkpoint_path: The path to the checkpoint file.
    :return: The checkpoint data.
    """
    with open(checkpoint_path, 'r') as f:
        return tuple(line.strip() for line in f.readlines())


def load_checkpoint(checkpoint_path: Union[Path, None]) -> Tuple[str]:
    """
    Load a checkpoint.
    
    :param checkpoint_path: The path to the checkpoint file. Defaults to the latest checkpoint.
    :return: The checkpoint data.
    """
    if not isinstance(checkpoint_path, Path) or not checkpoint_path.exists():
        return tuple()
    return load_checkpoint_from_file(checkpoint_path)


def save_checkpoint(file: Path, data: List[str]):
    """
    Save a checkpoint.

    :param file: The file to save the checkpoint to.
    :param data: The data to save.
    """
    with open(file, 'w') as f:
        f.write("\n".join(data))
    print(f"Saved model to {file}")


def make_checkpoint_name(checkpoints_dir: Path, filename: str) -> str:
    """
    Make a checkpoint name.

    :param checkpoints_dir: The directory to save the checkpoint in.
    :param filename: The filename of the checkpoint.
    :return: The name of the checkpoint.
    """
    checkpoints = list(checkpoints_dir.glob(f"{filename}_*.txt"))
    if not checkpoints:
        return f"{filename}_1.txt"
    
    # Get the number of the last checkpoint.
    total_checkpoints = int(re.search(r"\d+", str(checkpoints[-1])).group(0))
    return f"{filename}_{total_checkpoints + 1}.txt"
