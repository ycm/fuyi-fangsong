from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--char_start_decimal', type=int, required=True)
    parser.add_argument('--char_end_decimal', type=int, required=True)
    parser.add_argument('--font_path', type=str, required=True)
    parser.add_argument('--font_size', type=int, required=True)
    parser.add_argument('--font_offset', type=int, required=True)
    parser.add_argument('--out_dir', type=str, required=True)
    parser.add_argument('--image_height', type=int, required=True)
    args = parser.parse_args()

    print(args.font_path, type(args.font_path))
    # char = u"龘"

    # out_dir = 'char/song/'
    # font_path = "/usr/share/fonts/noto-cjk/NotoSerifCJK-Regular.ttc"
    # font_size = 256
    # font_offset = -70

    # out_dir = 'char/fangsong/'
    # font_path = '/home/ycm/.local/share/fonts/Unknown Vendor/TrueType/cwTeX Q FangsongZH/cwTeX_Q_FangsongZH_Medium.ttf'
    # font_size = 280
    # font_offset = -8

    out_path = Path(args.out_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    font = ImageFont.truetype(
        args.font_path,
        args.font_size,
        encoding="unic")

    total_chars = args.char_end_decimal - args.char_start_decimal

    for char_code in range(args.char_start_decimal, args.char_end_decimal):
        img = Image.new('L', (args.image_height, args.image_height), 'white')
        char = chr(char_code)
        draw = ImageDraw.Draw(img)
        draw.text((0, args.font_offset), char, 'black', font)

        img.save(out_path / f'{char}.png', "PNG")
        print(f'\r{char} / ({char_code - args.char_start_decimal + 1} / {total_chars})', end='')

    print(f'\noutput saved in {out_path}')

if __name__ == '__main__':
    main()
