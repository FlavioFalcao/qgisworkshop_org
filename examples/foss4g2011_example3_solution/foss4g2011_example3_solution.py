"""
/***************************************************************************
 foss4g2011_example3_solution
                                 A QGIS plugin
 Example #3 solution from FOSS4G 2011 Workshop
                              -------------------
        begin                : 2011-08-31
        copyright            : (C) 2011 by FOSS4G
        email                : info@cugos.org
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from foss4g2011_example3_solutiondialog import foss4g2011_example3_solutionDialog
#import pdb

#pyqtRemoveInputHook()
#pdb.set_trace()

class foss4g2011_example3_solution(QObject):

    def __init__(self, iface):
        QObject.__init__(self)
        # Save reference to the QGIS interface
        self.iface = iface

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/foss4g2011_example3_solution/icon.png"), \
            "Example #3 Solution", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&Example #3 Solution", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("&Example #3 Solution",self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):

        # create and show the dialog
        self.dlg = foss4g2011_example3_solutionDialog(self.iface)
        # show the dialog
        self.dlg.show()

        # QgisInterface
        QObject.connect(self.dlg.currentLayerChangedCheckBox, SIGNAL("stateChanged(int)"), self.check_currentLayerChanged)
        QObject.connect(self.dlg.emitCurrentLayerChangedBtn, SIGNAL("clicked(bool)"), self.btn_emitCurrentLayerChanged)
        # QgsMapCanvas
        QObject.connect(self.dlg.xyCoordinatesCheckBox, SIGNAL("stateChanged(int)"), self.check_xyCoordinates)
        QObject.connect(self.dlg.emitXYCoordinates, SIGNAL("clicked(bool)"), self.btn_emitXYCoordinates)
        QObject.connect(self.dlg.mapToolSetCheckBox, SIGNAL("stateChanged(int)"), self.check_mapToolSet)
        # QgsVectorLayer
        QObject.connect(self.dlg.editingStartedCheckBox, SIGNAL("stateChanged(int)"), self.check_editingStarted)
        QObject.connect(self.dlg.editingStoppedCheckBox, SIGNAL("stateChanged(int)"), self.check_editingStopped)
        QObject.connect(self.dlg.emitStartedEditingBtn, SIGNAL("clicked(bool)"), self.btn_emitStartedEditing)
        QObject.connect(self.dlg.emitStoppedEditingBtn, SIGNAL("clicked(bool)"), self.btn_emitStoppedEditing)
        # Custom defined SIGNALS
        QObject.connect(self.dlg.feedbackStatusCheckBox, SIGNAL("stateChanged(int)"), self.check_feedbackStatus)
        QObject.connect(self.dlg.emitFeedbackStatusBtn, SIGNAL("clicked(bool)"), self.btn_emitFeedbackStatus)
    
    def feedbackStatus(self):
        # do some really cool analysis and feedback....or
        print "I don't do anything useful - Yah!"  
        
    def btn_emitFeedbackStatus(self, checked):
       self.emit(SIGNAL("feedbackStatus(PyQt_PyObject)"), "Bruce Lee is my hero!")

    def check_feedbackStatus(self, state):
        # if now checked, we need to connect to the signal
        if state == Qt.Checked:
            QObject.connect(self, SIGNAL("feedbackStatus(PyQt_PyObject)"), self.listen_feedbackStatus)        
        # if now NOT checked, we need to un-connect to the signal
        else:
            QObject.disconnect(self, SIGNAL("feedbackStatus(PyQt_PyObject)"), self.listen_feedbackStatus)        

    def listen_feedbackStatus(self, message):
        self.dlg.outputTextEdit.append("feedbackStatus - %s" % (message if message else ""))

    def btn_emitStartedEditing(self, checked):
        # this function has iface emit a currentLayerChanged signal that should be picked up by our listening slots
        if self.iface.mapCanvas().currentLayer():
            self.iface.mapCanvas().currentLayer().emit(SIGNAL("editingStarted( )"))
        else:
            QMessageBox.information(self.iface.mainWindow(), "Info", "Make sure you have a QgsVectorLayer selected in the TOC to emit a SIGNAL(editingStarted( ))")

    def btn_emitStoppedEditing(self, checked):
        # this function has iface emit a currentLayerChanged signal that should be picked up by our listening slots
        if self.iface.mapCanvas().currentLayer():
            self.iface.mapCanvas().currentLayer().emit(SIGNAL("editingStopped( )"))
        else:
            QMessageBox.information(self.iface.mainWindow(), "Info", "Make sure you have a QgsVectorLayer selected in the TOC to emit a SIGNAL(editingStopped( ))")

    def check_editingStopped(self, state):
        # if now checked, we need to connect to the signal
        if state == Qt.Checked and (True if self.iface.mapCanvas().currentLayer() else False and self.iface.mapCanvas().currentLayer().type == 0):
            QObject.connect(self.iface.mapCanvas().currentLayer(), SIGNAL("editingStopped( )"), self.listen_editingStopped)        
        # if now NOT checked, we need to un-connect to the signal
        elif state == Qt.Unchecked and (True if self.iface.mapCanvas().currentLayer() else False and self.iface.mapCanvas().currentLayer().type == 0):
            QObject.disconnect(self.iface.mapCanvas().currentLayer(), SIGNAL("editingStopped( )"), self.listen_editingStopped)        
        else:
            QMessageBox.information(self.iface.mainWindow(), "Info", "Make sure you have a QgsVectorLayer selected in the TOC to connect/disconnect to SIGNAL(editingStopped)")

    def listen_editingStopped(self):
        self.dlg.outputTextEdit.append("editingStopped - %s" % (self.iface.mapCanvas().currentLayer().name() if self.iface.mapCanvas().currentLayer() else ""))

    def check_editingStarted(self, state):
        # if now checked, we need to connect to the signal
        if state == Qt.Checked and (True if self.iface.mapCanvas().currentLayer() else False and self.iface.mapCanvas().currentLayer().type == 0):
            QObject.connect(self.iface.mapCanvas().currentLayer(), SIGNAL("editingStarted( )"), self.listen_editingStarted)        
        # if now NOT checked, we need to un-connect to the signal
        elif state == Qt.Unchecked and (True if self.iface.mapCanvas().currentLayer() else False and self.iface.mapCanvas().currentLayer().type == 0):
            QObject.disconnect(self.iface.mapCanvas().currentLayer(), SIGNAL("editingStarted( )"), self.listen_editingStarted)        
        else:
            QMessageBox.information(self.iface.mainWindow(), "Info", "Make sure you have a QgsVectorLayer selected in the TOC to connect/disconnect to SIGNAL(editingStarted)")

    def listen_editingStarted(self):
        self.dlg.outputTextEdit.append("editingStarted- %s" % (self.iface.mapCanvas().currentLayer().name() if self.iface.mapCanvas().currentLayer() else ""))
        
    def btn_emitCurrentLayerChanged(self, checked):
        # this function has iface emit a currentLayerChanged signal that should be picked up by our listening slots
        self.iface.emit(SIGNAL("currentLayerChanged(QgsMapLayer*)"), self.iface.mapCanvas().currentLayer() )

    def check_currentLayerChanged(self, state):
        # if now checked, we need to connect to the signal
        if state == Qt.Checked:
            QObject.connect(self.iface, SIGNAL("currentLayerChanged(QgsMapLayer*)"), self.listen_currentLayerChanged)        
        # if now NOT checked, we need to un-connect to the signal
        else:
            QObject.disconnect(self.iface, SIGNAL("currentLayerChanged(QgsMapLayer*)"), self.listen_currentLayerChanged)        

    def listen_currentLayerChanged(self,mapLayer):
        self.dlg.outputTextEdit.append("currentLayerChanged - %s" % (mapLayer.name() if mapLayer else ""))

    def btn_emitXYCoordinates(self, checked):
        self.iface.mapCanvas().emit(SIGNAL("xyCoordinates(const QgsPoint &)"), QgsPoint(-122,45))

    def check_xyCoordinates(self, state):
        # if now checked, we need to connect to the signal
        if state == Qt.Checked:
            QObject.connect(self.iface.mapCanvas(), SIGNAL("xyCoordinates(const QgsPoint &)"), self.listen_xyCoordinates)        
        # if now NOT checked, we need to un-connect to the signal
        else:
            QObject.disconnect(self.iface.mapCanvas(), SIGNAL("xyCoordinates(const QgsPoint &)"), self.listen_xyCoordinates)        

    def listen_xyCoordinates(self,point):
        self.dlg.outputTextEdit.append("xyCoordinates - %d,%d" % (point.x() if point else "",point.y() if point else ""))

    def check_mapToolSet(self, state):
        # if now checked, we need to connect to the signal
        if state == Qt.Checked:
            QObject.connect(self.iface.mapCanvas(), SIGNAL("mapToolSet(QgsMapTool *)"), self.listen_mapToolSet)        
        # if now NOT checked, we need to un-connect to the signal
        else:
            QObject.disconnect(self.iface.mapCanvas(), SIGNAL("mapToolSet(QgsMapTool *)"), self.listen_mapToolSet)        

    def listen_mapToolSet(self,tool):
        self.dlg.outputTextEdit.append("mapToolSet - %s" % (tool.action().text() if isinstance(tool,QgsMapTool) else "unidentified tool"))
