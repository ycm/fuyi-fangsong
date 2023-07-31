from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--char_file', type=str, required=True)
    parser.add_argument('--font_path', type=str, required=True)
    parser.add_argument('--font_size', type=int, required=True)
    parser.add_argument('--font_offset', type=int, required=True)
    parser.add_argument('--out_dir', type=str, required=True)
    parser.add_argument('--image_height', type=int, required=True)
    args = parser.parse_args()

    print(args.font_path, type(args.font_path))

    out_path = Path(args.out_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    font = ImageFont.truetype(
        args.font_path,
        args.font_size,
        encoding="unic")

    with open(args.char_file) as f:
        chars = f.read().strip()
        total_chars = len(chars)
        for i, char in enumerate(chars):
            img = Image.new('L', (args.image_height, args.image_height), 'white')
            draw = ImageDraw.Draw(img)
            draw.text((0, args.font_offset), char, 'black', font)

            img.save(out_path / f'{char}.png', "PNG")
            print(f'\r{char}: ({i + 1}/{total_chars})', end='')

    print(f'\noutput saved in {out_path}')

if __name__ == '__main__':
    main()
