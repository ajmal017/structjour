# Structjour -- a daily trade review helper
# Copyright (C) 2019 Mike Petersen
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
'''
Overridden Qt objects for use with designer

Created on April 8, 2019

@author: Mike Petersen
'''

from PyQt5.QtWidgets import QTextEdit, QAction

# pylint: disable = C0103



class MyTextEdit(QTextEdit):
    '''Define a commit action for this widget in its context menu.'''

    def contextMenuEvent(self, event):
        ''' Override '''
        # print('Here we are again', event)
        stdMenu = self.createStandardContextMenu()
        commitAction = QAction("Commit", self)
        commitAction.setShortcut("Ctrl+S")


        stdMenu.addAction(commitAction)
        # commitAction.setShortcut('Ctrl+s')
        # stdMenu.insertMenu( stdMenu.actions().first(), newMenu )
        action = stdMenu.exec(event.globalPos())

        if action == commitAction:
            print('fukinfinly')