# My imx.to scripts
Here are some scripts that I made to obtain information from albums uploaded to the file hosting website https://imx.to

## Usage
### imx.py
```
Usage: imx.py [-h] [-o OUTPUT] command album_url

positional arguments:
  command               Action to perform (info or links)
  album_url             URL of the imx.to album

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Path to the output file (optional)
```

## Examples
To get the links of all the images in a specified album and output them to a txt file in the current directory called "output.txt", do:
```
imx.py links <url of album> -o output.txt
```
To get specific info about the album, such as the title, number of files, and file size, do:
```
imx.py info <url of album>
```

Note: the above script requires Python 3.
