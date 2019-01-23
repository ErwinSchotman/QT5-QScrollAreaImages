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

from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSignal, Qt, QSize


#=======================================================================================================================
class QClickableImage(QLabel):

    image_id = ''

    #-------------------------------------------------------------------------------------------------------------------
    def __init__(self, width=0, height=0, pixmap=None, image_id=''):
        QLabel.__init__(self)
        if width and height:
            self.resize(width, height)
        if pixmap:
            pixmap = pixmap.scaled(QSize(width, height), Qt.KeepAspectRatio, Qt.SmoothTransformation);
            self.setPixmap(pixmap)
        if image_id:
            self.image_id = image_id

    clicked = pyqtSignal(object)
    rightClicked = pyqtSignal(object)

    #-------------------------------------------------------------------------------------------------------------------
    def mousePressEvent(self, ev):
        if ev.button() == Qt.RightButton:
            self.rightClicked.emit(self.image_id)
        else:
            self.clicked.emit(self.image_id)

    #-------------------------------------------------------------------------------------------------------------------
    def imageId(self):
        return self.image_id

