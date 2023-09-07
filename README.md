# Image Converter
Image Converter is a CLI tool, build in python, that converts single images or a stack of images in a folder in a another file format. It also can be used to create fast and easy thumbails from single images as well as from a stack of images. If you like, use filter such as blur, black and white, sharpen.

This tool was developed as final project for Havard's CS50’s Introduction to Programming with Python.

## Installation

Download the image converter files or install them via git clone:

```
git clone ssh://git@github.com/hooked-to-coding/image-converter.git
```

You may have to install the following libaries:

### Pillow
```
python3 -m pip install Pillow
```

### Argsparse
```
python3 -m pip install argparse
```

### Tabulate
```
python3 -m pip install tabulate
```

## Usage

### Demo

Here is a short video demo of how to use the Image Converter. Look also at the [examples](#examples) to get a better understanding of the correct usage.
[![asciicast](https://asciinema.org/a/rCOiVAmd6GOqgnQIAp3pTeTJp.svg)](https://asciinema.org/a/rCOiVAmd6GOqgnQIAp3pTeTJp)

### Supported file formats
The Image Converter supports the following file format:
* .jpg
* .jpeg
* .gif
* .png
* .webp

### Filter
The Image Converter usess the following image filter:
* sharpen
* blur
* smooth
* bw (black and white)
* contour
* detail

## <div name="examples">Examples</div>

### Convert a single image
Converts the file bild.jpg to bild.webp and saves it in the same directory:

```
python3 imco.py -file bild.jpg -to webp
```

Converts the file bild.jpg to another_file.gif and saves it in the same directory:

```
python3 imco.py -file bild.jpg -to gif -name another_file
```

Converts the file bild.jpg to another_file.gif and saves it in the same directory:

```
python3 imco.py -file bild.jpg -to gif -name another_file
```

Converts the file bild.jpg to another_file.gif and saves it in ./new-dir/:

```
python3 imco.py -file bild.jpg -to gif -name another_file -dir new-dir/
```

Converts the file bild.jpg to another_file.gif and saves it in ./new-dir/:

```
python3 imco.py -file bild.jpg -to gif -name another_file -dir new-dir/
```

Converts the file bild.jpg to another_file.gif, saves it in ./../project/web-images/webp/ and uses a black and white filter:

```
python3 imco.py -file bild.jpg -to webp -name another_file -dir ../project/web-images/webp/ -filter bw
```

### Convert multiple images with the same file format

Converts all images with the file format jpg to webp and saves it with the same name than the source file in ./_image_converter_webp:

```
python3 imco.py -dir web/ -type jpg -to webp
```

Converts all images with the file format jpg to webp, uses the blur filter and saves it with the same name than the source file in ./_image_converter_webp:

```
python3 imco.py -dir web/ -type jpg -to webp -filter blur
```

### Create a thumbnail from a single image

Creates a thumbnail with the name bild_thumb_225x175.gif from the image bild.jpg in the same directory:
```
python3 imco.py -thumb 225 175 -file bild.jpg -to gif
```

Creates a thumbnail with the name bild_thumb_225x175.gif with the dimenssions 225 x 175px from the image bild.jpg in the same directory and uses the sharpen filter:
```
python3 imco.py -thumb 225 175 -file bild.jpg -to gif -filter sharpen
```

### Create multiple thumbnail from images with the same file format in a folder

Creates a thumbnail from every file with the format jpeg in the folder _jpeg/ with the format 400 x 300px and saves it in _thumbs_webp:

```
python3 imco.py -thumb 400 300 -dir _jpeg/ -to webp -type jpeg
```


## Support

Please open an issue for support.
