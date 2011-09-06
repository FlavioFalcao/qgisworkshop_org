"""
/***************************************************************************
 foss4g2011_example1_solutionset
                                 A QGIS plugin
 Solution Set for Example #1 FOSS4G 2011 Workshop
                             -------------------
        begin                : 2011-09-05
        copyright            : (C) 2011 by foss4g2011
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
 This script initializes the plugin, making it known to QGIS.
"""
def name():
    return "foss4g2011_example1_solutionset"
def description():
    return "Solution Set for Example #1 FOSS4G 2011 Workshop"
def version():
    return "Version 0.1"
def icon():
    return "icon.png"
def qgisMinimumVersion():
    return "1.0"
def classFactory(iface):
    # load foss4g2011_example1_solutionset class from file foss4g2011_example1_solutionset
    from foss4g2011_example1_solutionset import foss4g2011_example1_solutionset
    return foss4g2011_example1_solutionset(iface)
