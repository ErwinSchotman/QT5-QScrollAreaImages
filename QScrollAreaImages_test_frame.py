#
# Copyright (c) 2019 Erwin Schotman
#
# Licensed under MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the "Software"), to deal in the Software
# without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and
# to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
# LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH
# THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import sys
from PyQt5.QtWidgets import QApplication, QFrame
from PyQt5.QtGui import QPixmap
from QScrollAreaImages import *


#=======================================================================================================================
def window():
    app = QApplication(sys.argv)

    # make a frame -----------------------------------------------------------------------------------------------------
    frame = QFrame()
    frame.resize(1000, 500)
    # give the frame a grid layout -------------------------------------------------------------------------------------
    grid_layout_frame = QGridLayout(frame)

    # make a QScrollAreaImages -----------------------------------------------------------------------------------------
    scroll_area_images = QScrollAreaImages()

    # put the scroll area in the frame grid ----------------------------------------------------------------------------
    grid_layout_frame.addWidget(scroll_area_images, 0, 0)

    frame.show()

    # fill the QScrollAreaImages with pictures -------------------------------------------------------------------------
    pixmap0 = QPixmap(r'water.jpg')
    pixmap1 = QPixmap(r'street.jpg')
    pixmap2 = QPixmap(r'tree.jpg')
    pixmap3 = QPixmap(r'people.jpg')
    pixmap4 = QPixmap(r'scooter.jpg')

    scroll_area_images.setDisplayedImageSize(200)
    for i in range(10):
        for j in range(5):
            if (i * 5 + j) % 5 == 0:
                scroll_area_images.addImage(pixmap0, 'water')
            if (i * 5 + j) % 5 == 1:
                scroll_area_images.addImage(pixmap1, 'street')
            if (i * 5 + j) % 5 == 2:
                scroll_area_images.addImage(pixmap2, 'tree')
            if (i * 5 + j) % 5 == 3:
                scroll_area_images.addImage(pixmap3, 'people')
            if (i * 5 + j) % 5 == 4:
                scroll_area_images.addImage(pixmap4, 'scooter')

    sys.exit(app.exec_())


#=======================================================================================================================
if __name__ == '__main__':
    window()