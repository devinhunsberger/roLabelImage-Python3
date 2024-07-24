# roLabelImg-Python3

roLabelImg-Python3 is a Pyhton3 build of the Github Repo rolabelImg here: <https://github.com/cgvict/roLabelImg>.

The original version 'labelImg''s link is here: <https://github.com/tzutalin/labelImg>.

It is written in Python and uses Qt for its graphical interface.

Annotations are saved as XML files almost like PASCAL VOC format, the format used by ImageNet <https://www.image-net.org/>.


## XML Format

```bash
    <annotation verified="yes">
      <folder>hsrc</folder>
      <filename>100000001</filename>
      <path>/Users/haoyou/Library/Mobile Documents/com~apple~CloudDocs/OneDrive/hsrc/100000001.bmp</path>
      <source>
        <database>Unknown</database>
      </source>
      <size>
        <width>1166</width>
        <height>753</height>
        <depth>3</depth>
      </size>
      <segmented>0</segmented>
      <object>
        <type>bndbox</type>
        <name>ship</name>
        <pose>Unspecified</pose>
        <truncated>0</truncated>
        <difficult>0</difficult>
        <bndbox>
          <xmin>178</xmin>
          <ymin>246</ymin>
          <xmax>974</xmax>
          <ymax>504</ymax>
        </bndbox>
      </object>
      <object>
        <type>robndbox</type>
        <name>ship</name>
        <pose>Unspecified</pose>
        <truncated>0</truncated>
        <difficult>0</difficult>
        <robndbox>
          <cx>580.7887</cx>
          <cy>343.2913</cy>
          <w>775.0449</w>
          <h>170.2159</h>
          <angle>2.889813</angle>
        </robndbox>
      </object>
    </annotation>
```


# Installation

## Download prebuilt binaries of original 'labelImg'

-  Windows & Linux <http://tzutalin.github.io/labelImg/>

## Build from source

### Linux/Ubuntu/Mac Requires 
[Python 3.8+](http://www.python.org/getit/) and has been tested with [PyQt 5](http://www.riverbankcomputing.co.uk/software/pyqt/intro).


### Ubuntu Linux

```bash
sudo apt-get install pyqt5-tools
sudo pip install lxml
make all
./roLabelImg.py
```

### OS X

```bash
brew install qt qt5
brew install libxml2
make all
./roLabelImg.py
```

### Windows

1. Download and setup [Python3.8 or later](https://www.python.org/downloads/), [PyQt5](https://www.riverbankcomputing.com/software/pyqt/download), and install [lxml](http://lxml.de/installation.html).

2. Open cmd and go to roLabelImg's directory

```bash
pyrcc4 -o resources.py resources.qrc
python roLabelImg.py
python roLabelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]
```


## Usage


### Steps

1. Build and launch using the instructions above.
2. Click 'Change default saved annotation folder' in Menu/File
3. Click 'Open Dir'
4. Click 'Create RectBox'
5. Click and release left mouse to select a region to annotate the rect
   box
6. You can use right mouse to drag the rect box to copy or move it

The annotation will be saved to the folder you specify.

You can refer to the below hotkeys to speed up your workflow.

### Hotkeys

```bash
+------------+--------------------------------------------+
| Ctrl + u   | Load all of the images from a directory    |
+------------+--------------------------------------------+
| Ctrl + r   | Change the default annotation target dir   |
+------------+--------------------------------------------+
| Ctrl + s   | Save                                       |
+------------+--------------------------------------------+
| Ctrl + d   | Copy the current label and rect box        |
+------------+--------------------------------------------+
| Space      | Flag the current image as verified         |
+------------+--------------------------------------------+
| w          | Create a rect box                          |
+------------+--------------------------------------------+
| e          | Create a Rotated rect box                  |
+------------+--------------------------------------------+
| d          | Next image                                 |
+------------+--------------------------------------------+
| a          | Previous image                             |
+------------+--------------------------------------------+
| r          | Hidden/Show Rotated Rect boxes             |
+------------+--------------------------------------------+
| n          | Hidden/Show Normal Rect boxes              |
+------------+--------------------------------------------+
| del        | Delete the selected rect box               |
+------------+--------------------------------------------+
| Ctrl++     | Zoom in                                    |
+------------+--------------------------------------------+
| Ctrl--     | Zoom out                                   |
+------------+--------------------------------------------+
| ↑→↓←       | Keyboard arrows to move selected rect box  |
+------------+--------------------------------------------+
| zxcv       | Keyboard to rotate selected rect box       |
+------------+--------------------------------------------+
```

### Creating pre-defined classes

You can edit the [data/predefined\_classes.txt](/data/predefined_classes.txt) to load pre-defined classes


## License

Free software: [MIT license](https://github.com/cgvict/roLabelImg/blob/master/LICENSE)

## Related

1. [ImageNet Utils](https://github.com/tzutalin/ImageNet_Utils) to
   download image, create a label text for machine learning, etc
2. [Docker Hub](https://hub.docker.com/r/tzutalin/py2qt4) to run it 
