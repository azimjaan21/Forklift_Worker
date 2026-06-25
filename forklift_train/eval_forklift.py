from argparse import ArgumentParser
from pathlib import Path
from ultralytics import YOLO

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MODEL = r"C:\Users\dalab\Desktop\azimjaan21\SafeFactory System\#Project_Safety_AI\2.2 Forklift-Worker Detection\forklift_yolo11m\weights\best.pt"
DEFAULT_DATA = r"C:\Users\dalab\Desktop\azimjaan21\SafeFactory System\#Project_Safety_AI\2.2 Forklift-Worker Detection\forklift\forklift_data.yaml"


def parse_args():
    parser = ArgumentParser(description="Evaluate YOLOv8 model on the scaffolding dataset")
    parser.add_argument(
        "--weights",
        type=Path,
        default=DEFAULT_MODEL,
        help="Path to the model weights file (default: trained best.pt)",
    )
    parser.add_argument(
        "--data",
        type=Path,
        default=DEFAULT_DATA,
        help="Path to the dataset YAML file (default: filtered dataset YAML)",
    )
    parser.add_argument(
        "--split",
        type=str,
        default="val",
        choices=["train", "val", "test"],
        help="Dataset split to evaluate",
    )
    parser.add_argument(
        "--plots",
        action="store_true",
        help="Save evaluation plots",
    )
    parser.add_argument(
        "--save-json",
        action="store_true",
        help="Save evaluation results as COCO-style JSON",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    if not args.weights.exists():
        raise FileNotFoundError(f"Weights file not found: {args.weights}")
    if not args.data.exists():
        raise FileNotFoundError(f"Data YAML not found: {args.data}")

    print(f"Evaluating model: {args.weights}")
    print(f"Dataset YAML: {args.data}")
    print(f"Split: {args.split}")

    model = YOLO(str(args.weights))
    model.val(
        data=str(args.data),
        split=args.split,
        plots=args.plots,
        save_json=args.save_json,
    )


if __name__ == "__main__":
    main()
