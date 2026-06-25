from pathlib import Path
from ultralytics import YOLO


ROOT = Path(__file__).resolve().parents[1]

DATA_YAML = Path(
    r"C:\Users\dalab\Desktop\azimjaan21\SafeFactory System\#Project_Safety_AI\2.2 Forklift-Worker Detection\forklift\forklift_data.yaml"
)

PROJECT_DIR = ROOT / "2.2 Forklift-Worker Detection"
RUN_NAME = "forklift_yolo11m"


def main() -> None:
    print(f"Using data.yaml: {DATA_YAML}")

    if not DATA_YAML.exists():
        raise FileNotFoundError(f"data.yaml not found: {DATA_YAML}")

    model = YOLO("yolo11m.pt")

    model.train(
        data=str(DATA_YAML),
        epochs=100,
        imgsz=640,
        batch=8,
        device=0,
        workers=0,
        project=str(PROJECT_DIR),
        name=RUN_NAME,
        pretrained=True,
        exist_ok=True,
    )


if __name__ == "__main__":
    main()