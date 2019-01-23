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

from PyQt5.QtWidgets import QScrollArea, QWidget, QGridLayout
from QClickableImage import *
from PyQt5.QtCore import QRect


#=======================================================================================================================
class QScrollAreaImages(QScrollArea):

    displayed_image_size = 100

    #-------------------------------------------------------------------------------------------------------------------
    def __init__(self, width=0, height=0, pixmap=None):
        QScrollArea.__init__(self)

        # make a scroll area resizeable
        self.setWidgetResizable(True)

        # make a widget for the contents of the scroll area
        self.scrollAreaWidgetContents = QWidget()
        #self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 421, 429))

        # give this widget a grid layout
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)

        # put the contents widget in the scroll area
        self.setWidget(self.scrollAreaWidgetContents)


    #-------------------------------------------------------------------------------------------------------------------
    def get_nr_of_image_columns(self):
        scroll_area_images_width = self.width()
        if scroll_area_images_width > self.displayed_image_size:
            nr_of_columns = scroll_area_images_width // self.displayed_image_size
        else:
            nr_of_columns = 1
        return nr_of_columns

    #-------------------------------------------------------------------------------------------------------------------
    def on_resize(self, event):
        nr_of_columns = self.get_nr_of_image_columns()
        nr_of_widgets = self.gridLayout.count()
        widgets = []
        for i in range(nr_of_widgets):
            widgets.append(self.gridLayout.itemAt(i))
        column_nr = 0
        row_nr = 0
        for widget in widgets:
            self.gridLayout.removeItem(widget)
            self.gridLayout.addWidget(widget.widget(), row_nr, column_nr)
            if column_nr == nr_of_columns - 1:
                column_nr = 0
                row_nr += 1
            else:
                column_nr += 1

    #-------------------------------------------------------------------------------------------------------------------
    def setDisplayedImageSize(self, image_size):
        self.displayed_image_size = image_size

    #-------------------------------------------------------------------------------------------------------------------
    def addImage(self, pixmap, image_id):
        nr_of_columns = self.get_nr_of_image_columns()
        nr_of_widgets = self.gridLayout.count()
        row_nr = nr_of_widgets // nr_of_columns
        column_nr = nr_of_widgets % nr_of_columns
        clickable_image = QClickableImage(self.displayed_image_size, self.displayed_image_size, pixmap, image_id)
        clickable_image.clicked.connect(self.on_left_clicked)
        clickable_image.rightClicked.connect(self.on_right_clicked)
        self.gridLayout.addWidget(clickable_image, column_nr, row_nr)

    #-------------------------------------------------------------------------------------------------------------------
    def on_left_clicked(self, image_id):
        print('left clicked - image id = ' + image_id)

    #-------------------------------------------------------------------------------------------------------------------
    def on_right_clicked(self, image_id):
        print('right clicked - image id = ' + image_id)

    #-------------------------------------------------------------------------------------------------------------------
    def resizeEvent(self, event):
        self.on_resize(event)
