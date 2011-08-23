
================================================
Building Our First Plugin with 'Plugin Builder'
================================================

Now it's time to get our feet wet by building our first plugin using\  **Plugin Builder** \to help us.

\  **1.** \On the QGIS menu bar click on the\  ``Plugin Builder`` \icon to launch the plugin:

.. image:: ../_static/plugin_builder_click1.png
    :scale: 100%
    :align: center

\  **2.** \The main Plugin Builder dialog will appear. This is where we fill out our basic configuration information that Plugin Builder uses to create the template files. We will then modify the template files to build out our plugin. All the fields in the dialog below are required. Fill these fields out like the picture shows. Then click the\  ``Ok`` \button.:

.. image:: ../_static/plugin_builder_main_dialog.png 
    :scale: 100%
    :align: center

\  **3.** \A file dialog will open. Create a\ ``workspace`` \folder inside your\  ``/home/qgis/`` \directory. Save your plugin project by selecting the\  ``workspace`` \directory in the file dialog:

.. image:: ../_static/plugin_builder_save_dir.png 
    :scale: 100%
    :align: center

\  **4.** \If everything went well, Plugin Builder will display a final dialog that shows us the next steps to customize our plugin project. Don't worry about folowing these because we will be detailing the exact same steps.

.. image:: ../_static/plugin_builder_feedback.png 
    :scale: 100%
    :align: center

\  **5.** \Now change into the workspace directory of your project\  ``/home/qgis/workspace/vector_selectbypoint`` \and list out the contents::

    $ cd workspace/vector_selectbypoint/
    $ ls -lah
    total 36K
    drwxr-xr-x 2 qgis qgis 4.0K 2011-08-20 13:21 .
    drwxr-xr-x 3 qgis qgis 4.0K 2011-08-20 17:34 ..
    -rw-r--r-- 1 qgis qgis 1.1K 2011-08-20 13:21 icon.png
    -rw-r--r-- 1 qgis qgis 1.6K 2011-08-20 13:21 __init__.py
    -rw-r--r-- 1 qgis qgis 1.9K 2011-08-20 13:21 Makefile
    -rw-r--r-- 1 qgis qgis  116 2011-08-20 13:21 resources.qrc
    -rw-r--r-- 1 qgis qgis 1.5K 2011-08-20 13:21 ui_vector_selectbypoint.ui
    -rw-r--r-- 1 qgis qgis 1.5K 2011-08-20 13:21 vector_selectbypointdialog.py
    -rw-r--r-- 1 qgis qgis 2.6K 2011-08-20 13:21 vector_selectbypoint.py


Notice that we have a single\  ``.ui`` \file and\  ``.qrc`` \file but that they haven't been compiled yet into Python modules. Let's compile these an take a quick look at what our plugin looks like so far inside QGIS.

\  **6.** \Luckily we have a\  ``Makefile`` \in this directory that we can use to compile both files easily. From inside the directory\  ``vector_selectbypoint`` \run the following command and it will print out two statements::

    $ make
    pyuic4 -o ui_vector_selectbypoint.py ui_vector_selectbypoint.ui
    pyrcc4 -o resources.py  resources.qrc

Those two statements are the commands we need to compile the appropriate resources and GUI files. We can either run these individually or just run the\  ``Makefile`` \to start them at the same time. Every time you make changes to the\  ``resources.qrc`` \or the\  ``ui_vector_selectbypoint.ui`` \file you will need to recompile.

\  **7.** \Now relist the contents of your directory and you will see more Python modules that were created. The important ones are these Python modules::
    
    $ ls -lah
    ... # MORE FILES WERE LISTED HERE
    -rw-r--r-- 1 qgis qgis 5.4K 2011-08-20 17:42 resources.py
    -rw-r--r-- 1 qgis qgis 1.4K 2011-08-20 17:42 ui_vector_selectbypoint.py
    ... # MORE FILES WERE LISTED HERE

\  **8.** \QGIS will now be able to read the files in our project and create an appropriate button on the menu bar. However, for QGIS to notice our new plugin we will need to put the our plugin folder inside of the\  ``/home/qgis/.qgis/python/plugins`` \directory. Instead of copying all our files there let's make a symbolic link (a shortcut) from our\  ``/home/qgis/workspace/vector_selectbypoing/`` \folder to the\  ``home/qgis/.qgis/python/plugings`` \folder. This way QGIS will notice our plugin project but the files are actually still located in our workspace folder for us to edit::

     $ ln -s /home/qgis/workspace/vector_selectbypoint/ /home/qgis/.qgis/python/plugins/

\  **9.** \If we change directories to\  ``/home/qgis/.qgis/python/plugins`` \and list it's contents we should see\  ``vector_selectbypoint`` \pointing to our workspace folder::

    $ cd /home/qgis/.qgis/python/plugins
    $ ls -lah
    total 16K
    drwxr-xr-x 4 qgis qgis 4.0K 2011-08-20 17:58 .
    drwxr-xr-x 4 qgis qgis 4.0K 2011-07-07 13:41 ..
    drwxr-xr-x 2 qgis qgis 4.0K 2011-08-20 12:26 osmpoly_export
    drwxr-xr-x 3 qgis qgis 4.0K 2011-07-07 13:41 pluginbuilder
    lrwxrwxrwx 1 qgis qgis   42 2011-08-20 17:58 vector_selectbypoint -> /home/qgis/workspace/vector_selectbypoint/

\  **10.** \Go back to QGIS and add the plugin to QGIS using the plugin manager\  ``Plugins > Manage Plugins`` \. When the QGIS Plugin Manager pops up start typing\  ``Select_`` \into the filter bar at top and our plugin will come up. Check the box to the left of our plugin. Then click the\  ``OK`` \button:

.. image:: ../_static/plugin_builder_adding2QGIS.png
    :scale: 100%
    :align: center

\  **11.** \You might notice that an icon has been added to the menu right next to our Plugin Builder command icon. Click this item:

.. image:: ../_static/click_vector_selectbypoint_tool.png
    :scale: 100%
    :align: center

\  **12.** \If everything went well, you will see an empty dialog with an\  ``OK`` \and\  ``Cancel`` \button. As you can see the Plugin Builder doesn't give us anything off-the-shelf that is useful. We have to customize it. But at least it works (yah!):

.. image:: ../_static/vector_selectbypoint_firstview.png
    :scale: 100%
    :align: center

----------------------------

Extending the Plugin Builder Templates
-----------------------------------------  

Building plugins is an iterative process, many consecutive steps are repeated. I like to think that building a plugin generally follows this workflow:

    1. Choose to implement one small part of overall plugin idea at a time
    2. Customize the GUI desgin with Qt Designer to fit our interactive needs (remember to recompile the .ui file)
    3. Begin programming tool logic but do it as a proof-of-concept with QMessageBoxes giving feedback to make sure it is working
    4. Once tool logic has been proofed, tie the tool logic to the GUI and test

The Plugin Idea
********************

The tool we're going to build will be do a few basic things:

     * The tool will select the activated layer's vector features using a single map click. 
     * The tool will display the 'NAME' attribute of any feature (if it exists) for a particular vector layer.
     * The tool will have the option of being active or inactive using a checkbox setting.

.. note:: This tool will work the exact same way that the current Select Single Feature tool works in QGIS. The purpose is to illustrate the steps in fleshing out a plugin. There are more practical examples at the end of this tutorial.

Knowing the overall plugin idea will lead us to list the implementation tasks that we can tackle one at a time:

    1. Implement map canvas point click and point coordinate feedback
    2. Implement selection of feature on point click
    3. Implement attribute feedback if the active layer has a 'NAME' attribute
    4. Implement making the tool inactive and active using checkbox 


Designing the GUI
******************

Let's talk about what the GUI will look like. The requirements for this tool are pretty straightforward:

    1. Need a way to display feedback of 'NAME' attribute (if it exists) to user (we are going to use a TextBrowser widget for feedback)
    2. Need a way to activate or deactivate the tool (we are going to use a checkbox widget)

If we want to make changes to the GUI we will need to edit the\  ``.ui`` \file associated with this project. Qt Designer is the editor that we are going to use to do this type of editing. 


\  **1.** \Open\  **Qt 4 Designer** \from the\  ``Applications > Programming`` \menu at the top-left of the virtual machine:

.. image:: ../_static/qt_design1.png
    :scale: 100%
    :align: center

\  **2.** \A file dialog with open. Navigate to your plugin workspace at\  ``/home/qgis/workspace/vector_selectbypoint/`` \. Only the\  ``.ui`` \file associated with this project should show up in the file dialog to open. It is called\  ``ui_vector_selectbypoint.ui`` \. Select it and click\  ``Open`` \:

.. image:: ../_static/qt_design2.png
    :scale: 100%
    :align: center

\  **3.** \The Qt form that opens should look familiar. It is basically a blank form with a couple buttons:

.. image:: ../_static/qt_design3.png
    :scale: 100%
    :align: center

\  **4.** \We want to add a TextBrowser and CheckBox widget to this form. First drag-and-drop a TextBrowser widget on the form. Find TextBrowser in the left-hand column under the subhead\  ``Display Widgets`` \:

.. image:: ../_static/qt_design4.png
    :scale: 100%
    :align: center

\  **5.** \Now we should have a TextBrowser object on our form like so:

.. image:: ../_static/qt_design5.png
    :scale: 100%
    :align: center

\  **6.** \With the TextBrowser on the form selected (showing the blue square vertices), move over to the bottom-right column called the\  ``Property Editor`` \and change the name of the TextBrowser object to\  ``txtFeedback`` \. The edit happens in the field called \  ``objectName`` \. The value we put in here will be used inside our code to represent the TextBrowser.

.. image:: ../_static/qt_design05.png
    :scale: 100%
    :align: center

\  **7.** \Now go back to the right-hand column and find a CheckBox widget under the subhead\  ``Buttons`` \. Drag-and-drop this on the form. The form will now look like this:

.. image:: ../_static/qt_design6.png
    :scale: 100%
    :align: center

.. image:: ../_static/qt_design7.png
    :scale: 100%
    :align: center

\  **8.** \With the CheckBox on the form selected (showing the blue square vectices), go over to the\  ``Property Editor`` \and change the\  ``objectName`` \field to\  ``chkActivate`` \and the\  ``text`` \field to\  ``Activate\n(check)`` \.:

.. image:: ../_static/qt_design8.png
    :scale: 100%
    :align: center

.. image:: ../_static/qt_design9.png
    :scale: 100%
    :align: center

\  **9.** \Move the widgets around and stetch them to make your form look similar to this: 

.. image:: ../_static/qt_design10.png
    :scale: 100%
    :align: center

\  **10.** \Now save your changes by selecting\  ``File > Save`` \in the menu bar. 


\  **11.** \In a bash shell change directories to your workspace folder\  ``/home/qgis/workspace/vector_selectbypoint`` \and recompile everthing using the 'make' command::

    $ cd /home/qgis/workspace/vector_selectbypoint
    $ make
    pyuic4 -o ui_vector_selectbypoint.py ui_vector_selectbypoint.ui

Notice that the Makefile is smart. It knows that there were only changes to the\  ``.ui`` \file and not the\  ``.qrc`` \file. So it only compiles the GUI file into a Python module. 

Programming Plugin Logic
*******************************

\  **1.** \Let's begin by opening up the main Python module that runs our tool's logic and having a look around. Most of you will be more comfortable browsing and editing code in a text editor like gedit. Open gedit by clicking the notepad icon on the top menue bar of Ubuntu:

.. image:: ../_static/open_gedit.png
    :scale: 100%
    :align: center

\  **2.** \Now navigate to your workspace plugin folder\  ``/home/qgis/workspace/vector_selectbypoint`` \and open the file\  ``vector_selectbypoing.py`` \. Your code should look exactly like this::

    # Import the PyQt and QGIS libraries
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    from qgis.core import *
    # Initialize Qt resources from file resources.py
    import resources
    # Import the code for the dialog
    from vector_selectbypointdialog import vector_selectbypointDialog

    class vector_selectbypoint:

        def __init__(self, iface):
            # Save reference to the QGIS interface
            self.iface = iface

        def initGui(self):
            # Create action that will start plugin configuration
            self.action = QAction(QIcon(":/plugins/vector_selectbypoint/icon.png"), \
                "some text that appears in the menu", self.iface.mainWindow())
            # connect the action to the run method
            QObject.connect(self.action, SIGNAL("triggered()"), self.run)

            # Add toolbar button and menu item
            self.iface.addToolBarIcon(self.action)
            self.iface.addPluginToMenu("&some text that appears in the menu", self.action)

        def unload(self):
            # Remove the plugin menu item and icon
            self.iface.removePluginMenu("&some text that appears in the menu",self.action)
            self.iface.removeToolBarIcon(self.action)

        # run method that performs all the real work
        def run(self):
            # create and show the dialog
            dlg = vector_selectbypointDialog()
            # show the dialog
            dlg.show()
            result = dlg.exec_()
            # See if OK was pressed
            if result == 1:
                # do something useful (delete the line containing pass and
                # substitute with your code
                pass


\  **3.** \Let's walk through some important things about this file.

QGIS needs special class methods to exist in your main Python class for it to work. These are\  ``initGui()`` \,\  ``__init__()`` \and\  ``unload`` \. If we read through the code comments in those functions we can intuit that\  ``initGui()`` \and\  ``__init__()`` \get called at plugin startup and that some of the code in the\  ``initGui()`` \function is responsible for adding our plugin to the menu. The function\  ``unload()`` \does the opposite -- it tears down things we setup at intialization. 

Also notice that our reference to the QgsInterface class is under\  ``__init__()`` \. From this class attribute we can create a reference to other parts of the QGIS system such as the map canvas.

Another important thing to note is that our dialog is being created under the\  ``run()`` \method with these lines::

    dlg = vector_selectbypointDialog()
    # show the dialog
    dlg.show()

The\ ``vector_selectbypointDialog()`` \class that is being instatiated in that last code snippet was imported from our Python module dialog. If you were to open that Python module you'd notice it references the Python module that was compiled from our\  ``.ui`` \file --\  ``ui_vector_selectbypoint.py`` \. At the top of the file::

    from vector_selectbypointdialog import vector_selectbypointDialog

Execution of the\  ``run()`` \method is then halted. It waits for some user input to move forward. That user input (in this case) is in the form of a button click. The rest of the code in the\  ``run()`` \method then decides what button was clicked\  ``Cancel == 0 and OK == 1`` \. When we first start writing plugins your code tends to fall under the\  ``run()`` \method, though you'll see it doesn't need to be put there in the future::

    result = dlg.exec_()
    # See if OK was pressed
    if result == 1:
        # do something useful (delete the line containing pass and
        # substitute with your code
        pass 


\  **4.** \Now we're going to start programming. Our tool will need a reference to the map canvas. It will also need a reference to a click tool. Make your\  ``__init__()`` \function look like this::

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # a reference to our map canvas 
        self.canvas = self.iface.mapCanvas() #CHANGE
        # this QGIS tool emits as QgsPoint after each click on the map canvas
        self.clickTool = QgsMapToolEmitPoint(self.canvas)

\  **5.** \Usually when working with QGIS GUI elements we'll need to import the\  ``qgis.gui`` \module classes and functions. The class\  ``QgsMapToolEmitPoint`` \that we used to create our point tool exits here. At the top of your\  ``vector_selectbypoint.py`` \module add this import statement under the other qgis import statements::

    from qgis.gui import *

\  **6.** \We have the references we'll need to implement a click and get some feedback in the form of a\  ``QgsPoint`` \but now we have to think about how that all works. In QGIS (and most other applications) there is the concept of an event/action.  In Qt we call these things in terms of signals and slots. When a user mouse-clicks the map canvas it broadcasts a signal about what just happened. Other functions in your program can subscribe to that broadcast and therefore react in real-time to a mouse-click. This is a concept that is not immediately intuitive or easy to program at first. So the best advice is to just follow the example below and try to understand as much as possible.  We'll return to this topic later and flesh it out more. For those that are interested here is very good resource that explains\  `PyQt signals and slots <http://www.commandprompt.com/community/pyqt/c1267>`_ \.


\  **7.** \To achieve the things we talked about in the last step we are going to need two things -- 1) some sort of way to register a custom function to the map canvas click event and 2) a custom function that gets called when a mouse-down happens on the map canvas. Maybe the best place to put any code that subscribes to a mouse click signal would be in\  ``initGui()`` \function. Add this line of code to the very end of the\  ``initGui()`` \function::

    result = QObject.connect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.handleMouseDown)
    QMessageBox.information( self.iface.mainWindow(),"Info", "connect = %s"%str(result) )

A quick note. The function\  ``QObject.connect()`` \does the dirty work of registering our custom function\  ``handleMouseDown`` \(which hasn't been written yet) to the clickTool signal\  ``canvasClicked()`` \. It returns a boolean value declaring if the connection worked or not. We are catching that response and then outputing it to a message box so we can make sure the code we are writing is working as expected.


\  **8.** \Now let's write our custom function that will get called whenever a mouse-down happens on the map canvas. Create this function anywhere below\  ``initGui()`` \.::

    def handleMouseDown(self, point, button):
            QMessageBox.information( self.iface.mainWindow(),"Info", "X,Y = %s,%s" % (str(point.x()),str(point.y())) )

We know that the signal\  ``canvasClicked()`` \emits a QgsPoint. So in our\  ``handleMouseDown()`` \function we are using a message box to view the X,Y output of that point.


\  **9.** \Finally, we have to make sure the click tool we setup under\  ``__init__()`` \is enabled when our tool runs. Add this code to the very beginning under the\  ``run()`` \function::

    # make our clickTool the tool that we'll use for now 
    self.canvas.setMapTool(self.clickTool)

\  **10.** \Your entire\  ``vector_selectbypoint.py`` \module should now look like this::

    # Import the PyQt and QGIS libraries
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    from qgis.core import *
    from qgis.gui import * 
    # Initialize Qt resources from file resources.py
    import resources
    # Import the code for the dialog
    from vector_selectbypointdialog import vector_selectbypointDialog

    class vector_selectbypoint:

        def __init__(self, iface):
            # Save reference to the QGIS interface
            self.iface = iface
            # reference to map canvas
            self.canvas = self.iface.mapCanvas() 
            # out click tool will emit a QgsPoint on every click
            self.clickTool = QgsMapToolEmitPoint(self.canvas)

        def initGui(self):
            # Create action that will start plugin configuration
            self.action = QAction(QIcon(":/plugins/vector_selectbypoint/icon.png"), \
                "some text that appears in the menu", self.iface.mainWindow())
            # connect the action to the run method
            QObject.connect(self.action, SIGNAL("triggered()"), self.run)

            # Add toolbar button and menu item
            self.iface.addToolBarIcon(self.action)
            self.iface.addPluginToMenu("&some text that appears in the menu", self.action)

            # connect our custom function to a clickTool signal that the canvas was clicked
            result = QObject.connect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.handleMouseDown)
            QMessageBox.information( self.iface.mainWindow(),"Info", "connect = %s"%str(result) )

        def unload(self):
            # Remove the plugin menu item and icon
            self.iface.removePluginMenu("&some text that appears in the menu",self.action)
            self.iface.removeToolBarIcon(self.action)

        def handleMouseDown(self, point, button):
            QMessageBox.information( self.iface.mainWindow(),"Info", "X,Y = %s,%s" % (str(point.x()),str(point.y())) )

        # run method that performs all the real work
        def run(self):
            # make our clickTool the tool that we'll use for now 
            self.canvas.setMapTool(self.clickTool) 

            # create and show the dialog
            dlg = vector_selectbypointDialog()
            # show the dialog
            dlg.show()
            result = dlg.exec_()
            # See if OK was pressed
            if result == 1:
                # do something useful (delete the line containing pass and
                # substitute with your code
                pass


Testing Your Code
********************

\  **1.** \Go back to QGIS and make sure all layers are removed except the admin countries layer::

    /home/qgis/natural_earth_50m/cultural/50m_cultural/50m_admin_0_countries.shp

\  **2.** \Open the QGIS Plugin Manger. If our tool\  ``Select_VectorFeatures_By_PointClick`` \is already selected then uncheck it and close the QGIS Plugin Manager. Now reopen the QGIS Plugin manager and check our plugin again to add it to QGIS. This process ensures that we are getting the newest edits to our plugin loaded. 

\  **3.** \You should notice that as soon as you selected 'OK' on the QGIS Plugin Manager but before our plugin showed up on the menu bar that one of two things happened -- you either got an error or you saw a\  ``connect = True`` \info message box:

.. image:: ../_static/connect_equals_true.png
    :scale: 100%
    :align: center

If you got an error try your best to locate the error, edit it and readd the plugin to test. If you have questions about what went wrong ask one of your neighbors or one of the helpers.

\  **4.** \Now click on our plugin button on the menu bar:

.. image:: ../_static/click_vector_selectbypoint_tool.png
    :scale: 100%
    :align: center


\  **5.** \You should notice two things here. Our form pops open with it's new improved look (yah!). Also notice that when the mouse hovers over the map canvas it changes into a crosshairs. Click somewhere on the map canvas and you should get a second info message box with an X,Y coordinate:

.. image:: ../_static/point_feedback.png
    :scale: 70%
    :align: center

If you got an error try your best to locate the error, edit it and readd the plugin to test. If you have questions about what went wrong ask one of your neighbors or one of the helpers.


Tie QgsPoint Output to the GUI
**********************************


Now open up vector_selectbypointdialog.py

from PyQt4 import QtCore, QtGui
from ui_vector_selectbypoint import Ui_vector_selectbypoint
# create the dialog for zoom to point
class vector_selectbypointDialog(QtGui.QDialog):

    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_vector_selectbypoint()
        self.ui.setupUi(self)


Add some helper propteries to get and set TextBrowser input


from PyQt4 import QtCore, QtGui
from ui_vector_selectbypoint import Ui_vector_selectbypoint
# create the dialog for zoom to point
class vector_selectbypointDialog(QtGui.QDialog):

    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_vector_selectbypoint()
        self.ui.setupUi(self)

    def setTextBrowser(self, output):
        self.ui.txtFeedback.setText(output)
     
    def clearTextBrowser(self):
        self.ui.txtFeedback.clear()


Back in our vector_selectbypoint.py we can comment out our messageboxes code and add in the following code

under __init__

    # create our GUI dialog
    self.dlg = vector_selectbypointDialog()

now that dlg is a class instance variable  in Python we have to refer to it as self. So make sure all references to it are changed in the file under run function
    # show the dialog
    self.dlg.show()
    result = self.dlg.exec_()

under handleMouseDown redirect the output to the dialo :

def handleMouseDown(self, point, button):
        self.dlg.clearTextBrowser()
        self.dlg.setTextBrowser( str(point.x()) + " , " +str(point.y()) )
        #QMessageBox.information( self.iface.mainWindow(),"Info", "X,Y = %s,%s" % (str(point.x()),str(point.y())) )



our code should now look like this:

# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import * 
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from vector_selectbypointdialog import vector_selectbypointDialog

class vector_selectbypoint:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # refernce to map canvas
        self.canvas = self.iface.mapCanvas() 
        # out click tool will emit a QgsPoint on every click
        self.clickTool = QgsMapToolEmitPoint(self.canvas)
        # create our GUI dialog
        self.dlg = vector_selectbypointDialog()

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/vector_selectbypoint/icon.png"), \
            "some text that appears in the menu", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&some text that appears in the menu", self.action)

    # connect our custom function to a clickTool signal that the canvas was clicked
    result = QObject.connect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.handleMouseDown)
        #QMessageBox.information( self.iface.mainWindow(),"Info", "connect = %s"%str(result) )

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("&some text that appears in the menu",self.action)
        self.iface.removeToolBarIcon(self.action)

    def handleMouseDown(self, point, button):
    self.dlg.clearTextBrowser()
    self.dlg.setTextBrowser( str(point.x()) + " , " +str(point.y()) )
        #QMessageBox.information( self.iface.mainWindow(),"Info", "X,Y = %s,%s" % (str(point.x()),str(point.y())) )

    # run method that performs all the real work
    def run(self):
    # make our clickTool the tool that we'll use for now 
    self.canvas.setMapTool(self.clickTool) 

        # show the dialog
        self.dlg.show()
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code
            pass



-------------------------------------


How to Debug Your Plugin
---------------------------

# stub

