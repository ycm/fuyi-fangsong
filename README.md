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


```
util/create_bitmap_characters.py \
    --char_start_decimal 19968 \
    --char_end_decimal 20968 \
    --font_path /usr/share/fonts/noto-cjk/NotoSerifCJK-Regular.ttc \
    --font_size 256 \
    --image_height 256 \
    --font_offset -70 \
    --out_dir char/song
```
