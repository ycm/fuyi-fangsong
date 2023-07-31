# 芣苢仿宋

> 采采芣苢、薄言采之、采采芣苢、薄言有之。


## util/

`util/create_bitmap_characters.py`

parser.add_argument('--char_start_decimal', type=int, required=True)
parser.add_argument('--char_end_decimal', type=int, required=True)
parser.add_argument('--font_path', type=str, required=True)
parser.add_argument('--font_size', type=str, required=True)
parser.add_argument('--font_offset', type=str, required=True)
parser.add_argument('--out_dir', type=str, required=True)
parser.add_argument('--image_height', type=int, required=True)

**generate images for first 1000 chars in songti**
```
python util/create_bitmap_characters.py \
    --char_file chars.txt \
    --font_path /usr/share/fonts/noto-cjk/NotoSerifCJK-Regular.ttc \
    --font_size 256 \
    --image_height 256 \
    --font_offset -70 \
    --out_dir char/song
```

**generate images for first 1000 chars in fangsong**
```
python util/create_bitmap_characters.py \
    --char_file chars.txt \
    --font_path "/home/ycm/.local/share/fonts/Unknown Vendor/TrueType/cwTeX Q FangsongZH/cwTeX_Q_FangsongZH_Medium.ttf" \
    --font_size 280 \
    --image_height 256 \
    --font_offset -8 \
    --out_dir char/fangsong
```
