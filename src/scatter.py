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
        self.setMinimumWidth(300)
        self.setMaximumHeight(800)
        self.setWindowFlags(self.windowFlags() ^
                            QtCore.Qt.WindowContextHelpButtonHint)
        self.scatter = Scatter()
        self.create_ui()
        self.create_connections()

    def create_ui(self):
        self.title_lbl = QtWidgets.QLabel("Scatter Tool")
        self.title_lbl.setStyleSheet("font: bold 20px")
        self.poly_surface_lay = self._create_poly_surface_ui()
        self.scatter_poly_lay = self._create_scatter_poly_ui()
        self.density_lay = self._create_density_ui()
        self.scale_lay = self._create_scale_ui()
        self.rotation_lay = self._create_rotation_ui()
        self.main_lay = QtWidgets.QVBoxLayout()
        self.main_lay.addWidget(self.title_lbl)
        self.main_lay.addLayout(self.poly_surface_lay)
        self.main_lay.addLayout(self.scatter_poly_lay)
        self.main_lay.addLayout(self.density_lay)
        self.main_lay.addLayout(self.scale_lay)
        self.main_lay.addLayout(self.rotation_lay)
        self.main_lay.addStretch()
        self.setLayout(self.main_lay)

    def create_connections(self):
        """Connect Signals and Slots"""
        #self.poly_surface_cmb.currentIndexChanged.connect(self._update_surface)

    def _create_poly_surface_ui(self):
        layout = QtWidgets.QVBoxLayout()
        self.poly_surface_header_lbl = QtWidgets.QLabel("Polygon Surface")
        self.poly_surface_header_lbl.setStyleSheet("font: bold")
        self.poly_surface_cmb = QtWidgets.QComboBox()
        self.poly_surface_cmb.addItems(['Sphere', 'Cube', 'Cylinder',
                                        'Cone', 'Torus', 'Plane', 'Disc'])
        layout.addWidget(self.poly_surface_header_lbl)
        layout.addWidget(self.poly_surface_cmb)
        return layout

    def _create_scatter_poly_ui(self):
        layout = QtWidgets.QVBoxLayout()
        self.scatter_poly_header_lbl = QtWidgets.QLabel("Scattered Polygon")
        self.scatter_poly_header_lbl.setStyleSheet("font: bold")
        self.scatter_poly_cmb = QtWidgets.QComboBox()
        self.scatter_poly_cmb.addItems(['Sphere', 'Cube', 'Cylinder',
                                        'Cone', 'Torus', 'Plane', 'Disc'])
        layout.addWidget(self.scatter_poly_header_lbl)
        layout.addWidget(self.scatter_poly_cmb)
        return layout

    def _create_density_ui(self):
        layout = QtWidgets.QGridLayout()
        self.density_header_lbl = QtWidgets.QLabel("Random Density")
        self.density_header_lbl.setStyleSheet("font: bold")
        self.mindensity_header_lbl = QtWidgets.QLabel("min")
        self.maxdensity_header_lbl = QtWidgets.QLabel("max")
        self.mindensity_le = QtWidgets.QLineEdit()
        self.mindensity_le.setFixedWidth(50)
        self.maxdensity_le = QtWidgets.QLineEdit()
        self.maxdensity_le.setFixedWidth(50)
        layout.addWidget(self.density_header_lbl)
        layout.addWidget(self.mindensity_header_lbl, 1, 0)
        layout.addWidget(self.maxdensity_header_lbl, 1, 2)
        layout.addWidget(self.mindensity_le, 1, 1)
        layout.addWidget(self.maxdensity_le, 1, 3)
        return layout

    def _create_scale_ui(self):
        layout = QtWidgets.QGridLayout()
        self.scale_header_lbl = QtWidgets.QLabel("Random Scale")
        self.scale_header_lbl.setStyleSheet("font: bold")
        self.minscale_header_lbl = QtWidgets.QLabel("min")
        self.maxscale_header_lbl = QtWidgets.QLabel("max")
        self.minscale_le = QtWidgets.QLineEdit()
        self.minscale_le.setFixedWidth(50)
        self.maxscale_le = QtWidgets.QLineEdit()
        self.maxscale_le.setFixedWidth(50)
        layout.addWidget(self.scale_header_lbl)
        layout.addWidget(self.minscale_header_lbl, 1, 0)
        layout.addWidget(self.maxscale_header_lbl, 1, 2)
        layout.addWidget(self.minscale_le, 1, 1)
        layout.addWidget(self.maxscale_le, 1, 3)
        return layout

    def _create_rotation_ui(self):
        layout = QtWidgets.QGridLayout()
        self.rotation_header_lbl = QtWidgets.QLabel("Random Rotation")
        self.rotation_header_lbl.setStyleSheet("font: bold")
        self.xmin_header_lbl = QtWidgets.QLabel("X min")
        self.ymin_header_lbl = QtWidgets.QLabel("Y min")
        self.zmin_header_lbl = QtWidgets.QLabel("Z min")
        self.xmax_header_lbl = QtWidgets.QLabel("X max")
        self.ymax_header_lbl = QtWidgets.QLabel("Y max")
        self.zmax_header_lbl = QtWidgets.QLabel("Z max")
        self.xminrotation_le = QtWidgets.QLineEdit()
        self.xminrotation_le.setFixedWidth(50)
        self.xmaxrotation_le = QtWidgets.QLineEdit()
        self.xmaxrotation_le.setFixedWidth(50)
        self.yminrotation_le = QtWidgets.QLineEdit()
        self.yminrotation_le.setFixedWidth(50)
        self.ymaxrotation_le = QtWidgets.QLineEdit()
        self.ymaxrotation_le.setFixedWidth(50)
        self.zminrotation_le = QtWidgets.QLineEdit()
        self.zminrotation_le.setFixedWidth(50)
        self.zmaxrotation_le = QtWidgets.QLineEdit()
        self.zmaxrotation_le.setFixedWidth(50)
        layout.addWidget(self.rotation_header_lbl)
        layout.addWidget(self.xmin_header_lbl, 1, 0)
        layout.addWidget(self.ymin_header_lbl, 2, 0)
        layout.addWidget(self.zmin_header_lbl, 3, 0)
        layout.addWidget(self.xmax_header_lbl, 1, 2)
        layout.addWidget(self.ymax_header_lbl, 2, 2)
        layout.addWidget(self.zmax_header_lbl, 3, 2)
        layout.addWidget(self.xminrotation_le, 1, 1)
        layout.addWidget(self.xmaxrotation_le, 1, 3)
        layout.addWidget(self.yminrotation_le, 2, 1)
        layout.addWidget(self.ymaxrotation_le, 2, 3)
        layout.addWidget(self.zminrotation_le, 3, 1)
        layout.addWidget(self.zmaxrotation_le, 3, 3)
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
            instanceResult = cmds.instance(transformName, name=transformName +
                                                               '_instance#')
            xRot = random.uniform(min(a), max(b))
            yRot = random.uniform(min(a), max(b))
            zRot = random.uniform(min(a), max(b))
            cmds.rotate(xRot, yRot, zRot, instanceResult)
            return