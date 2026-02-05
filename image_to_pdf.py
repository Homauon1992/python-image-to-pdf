from __future__ import annotations

from pathlib import Path

from PIL import Image, UnidentifiedImageError


def convert_image_to_pdf(image_path: Path) -> Path:
    output_path = image_path.with_suffix(".pdf")
    with Image.open(image_path) as image:
        rgb_image = image.convert("RGB")
        rgb_image.save(output_path, "PDF", resolution=300.0)
    return output_path


def main() -> None:
    raw_path = input("Enter the image file path (.jpg/.png): ").strip().strip('"')
    if not raw_path:
        print("No path provided.")
        return

    image_path = Path(raw_path)
    if not image_path.is_file():
        print(f"File not found: {image_path}")
        return

    try:
        output_path = convert_image_to_pdf(image_path)
    except UnidentifiedImageError:
        print("The file is not a recognized image format.")
        return
    except OSError as exc:
        print(f"Failed to convert image: {exc}")
        return

    print(f"PDF saved to: {output_path}")


if __name__ == "__main__":
    main()