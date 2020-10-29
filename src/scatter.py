import logging

from PySide2 import QtWidgets, QtCore
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui
import maya.cmds as cmds
import random

log = logging.getLogger(__name__)
random.seed(1234)

def maya_main_window():
    """Return the maya main window widget"""
    main_window = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window), QtWidgets.QWidget)

class ScatterToolUI(QtWidgets.QDialog):
    """Scatter Tool UI Class"""

    def __init__(self):
        super(ScatterToolUI, self).__init__(parent=maya_main_window())
        self.setWindowTitle("Scatter Tool")
        self.setMinimumWidth(500)
        self.setMaximumHeight(1000)
        self.setWindowFlags(self.windowFlags() ^
                            QtCore.Qt.WindowContextHelpButtonHint)
        self.scatter = Scatter()
        self.create_ui()

    def create_ui(self):
        self.title_lbl = QtWidgets.QLabel("Scatter Tool")
        self.title_lbl.setStyleSheet("font: bold 20px")
        self.poly_surface_lay = self._create_poly_surface_ui()
        self.scatter_poly_lay = self._create_scatter_poly_ui()
        self.random_density_lay = self._create_rand_density_ui()
        self.random_scale_lay = self.create_rand_scale_ui()
        self.random_rotation_lay = self.rand_rotation_ui()
        self.main_lay = QtWidgets.QVBoxLayout()
        self.main_lay.addWidget(self.title_lbl)
        self.main_lay.addWidget(self.poly_surface_lay)
        self.main_lay.addWidget(self.scatter_poly_lay)
        self.main_lay.addWidget(self.random_density_lay)
        self.main_lay.addWidget(self.random_scale_lay)
        self.main_lay.addWidget(self.random_rotation_lay)
        self.main_lay.addStretch()
        self.setLayout(self.main_lay)

    def create_connections(self):
        """Connect Signals and Slots"""
        self.poly_surface_cmb.currentIndexChanged.connect(self._update_surface)

    def _create_poly_surface_ui(self):
        layout = QtWidgets.QVBoxLayout()
        self.poly_surface_header_lbl = QtWidgets.QLabel("Polygon Surface")
        self.poly_surface_header_lbl.setStyleSheet("font: bold")
        #self.poly_surface_cmb = QtWidgets.QtComboBox()
        #self.poly_surface_cmb.addItems(['Sphere', 'Cube', 'Cylinder',
                                        #'Cone', 'Torus', 'Plane', 'Disc'])
        return layout

    def _create_scatter_poly_ui(self):
        layout = QtWidgets.QVBoxLayout()
        self.scatter_poly_header_lbl = QtWidgets.QLabel("Scattered Polygon")
        self.scatter_poly_header_lbl.setStyleSheet("font: bold")
        #self.scatter_poly_cmb = QtWidgets.QtComboBox()
        #self.scatter_poly_cmb.addItems(['Sphere', 'Cube', 'Cylinder',
                                        #'Cone', 'Torus', 'Plane', 'Disc'])
        return layout

    def _create_rand_density_ui(self):
        layout = QtWidgets.QVBoxLayout()
        self.rand_density_header_lbl = QtWidgets.QLabel("Random Density")
        self.rand_density_header_lbl.setStyleSheet("font: bold")
        return layout

    def create_rand_scale_ui(self):
        layout = QtWidgets.QVBoxLayout()
        self.rand_scale_header_lbl = QtWidgets.QLabel("Random Scale")
        self.rand_scale_header_lbl.setStyleSheet("font: bold")
        return layout

    def rand_rotation_ui(self):
        layout = QtWidgets.QVBoxLayout()
        self.rand_rotation_header_lbl = QtWidgets.QLabel("Random Rotation")
        self.rand_rotation_header_lbl.setStyleSheet("font: bold")
        return layout

    #def _update_surface(self):
        #self.ext_lbl.setText(self.ext_cmb.currentText())


class Scatter(object):
    """Scatter Tool stuff whheeee"""
    #def __init__(self):
        #self.rotate_feature =

    def rotate_feature(self):
        """Makes instances rotate randomly."""
        result = cmds.poly
        transformName = result[0]
        for i in range(0, 50):
            instanceResult = cmds.instance(transformName, name=transformName + '_instance#')
            xRot = random.uniform(min(a), max(b))
            yRot = random.uniform(min(a), max(b))
            zRot = random.uniform(min(a), max(b))
            cmds.rotate(xRot, yRot, zRot, instanceResult)
            return