import logging

from PySide2 import QtWidgets, QtCore
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui
import maya.cmds as cmds
import random

log = logging.getLogger(__name__)
random.seed(1234)
polygons = ['Sphere', 'Cube', 'Cylinder', 'Cone', 'Torus', 'Plane', 'Disc']

def maya_main_window():
    """Return the maya main window widget"""
    main_window = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window), QtWidgets.QWidget)

class ScatterToolUI(QtWidgets.QDialog):
    """Scatter Tool UI Class"""

    def __init__(self):
        super(ScatterToolUI, self).__init__(parent=maya_main_window())
        self.setWindowTitle("Scatter Tool")
        #self.setMinimumWidth(250)
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
        self.density_header_lbl = QtWidgets.QLabel("Random Density")
        self.density_lay = self._create_density_ui()
        self.scale_header_lbl = QtWidgets.QLabel("Random Scale")
        self.scale_lay = self._create_scale_ui()
        self.rotate_header_lbl = QtWidgets.QLabel("Random Rotate")
        self.rotate_lay = self._create_rotate_ui()
        self.shader_header_lbl = QtWidgets.QLabel("Color Selection")
        self.shader_lay = self._create_shader_ui()
        self.shader_lay = self._create_shader_ui()
        self.button_lay = self._create_button_ui()
        self.main_lay = QtWidgets.QVBoxLayout()
        self.main_lay.addWidget(self.title_lbl)
        self.main_lay.addLayout(self.poly_surface_lay)
        self.main_lay.addLayout(self.scatter_poly_lay)
        self.main_lay.addWidget(self.density_header_lbl)
        self.main_lay.addLayout(self.density_lay)
        self.main_lay.addWidget(self.scale_header_lbl)
        self.main_lay.addLayout(self.scale_lay)
        self.main_lay.addWidget(self.rotate_header_lbl)
        self.main_lay.addLayout(self.rotate_lay)
        self.main_lay.addWidget(self.shader_header_lbl)
        self.main_lay.addLayout(self.shader_lay)
        self.main_lay.addLayout(self.button_lay)
        self.main_lay.addStretch()
        self.setLayout(self.main_lay)

    def create_connections(self):
        """Connect Signals and Slots"""
        #self.apply_btn.clicked.connect(self.apply_tool)
        #self.poly_surface_cmb.currentIndexChanged.connect(self._create_surface)

    def _create_poly_surface_ui(self):
        layout = QtWidgets.QVBoxLayout()
        self.poly_surface_header_lbl = QtWidgets.QLabel("Polygon Surface")
        self.poly_surface_header_lbl.setStyleSheet("font: bold")
        self.poly_surface_cmb = QtWidgets.QComboBox()
        self.poly_surface_cmb.addItems([polygons])
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
        layout = QtWidgets.QVBoxLayout()
        self.density_header_lbl.setStyleSheet("font: bold")
        self.density_le = QtWidgets.QLineEdit()
        self.density_le.setFixedWidth(50)
        layout.addWidget(self.density_le)
        return layout

    def _create_scale_ui(self):
        layout = QtWidgets.QGridLayout()
        self.scale_header_lbl.setStyleSheet("font: bold")
        self.minscale_header_lbl = QtWidgets.QLabel("min")
        self.maxscale_header_lbl = QtWidgets.QLabel("max")
        self.minscale_le = QtWidgets.QLineEdit()
        self.minscale_le.setFixedWidth(50)
        self.maxscale_le = QtWidgets.QLineEdit()
        self.maxscale_le.setFixedWidth(50)
        layout.addWidget(self.minscale_header_lbl, 1, 0)
        layout.addWidget(self.maxscale_header_lbl, 1, 2)
        layout.addWidget(self.minscale_le, 1, 1)
        layout.addWidget(self.maxscale_le, 1, 3)
        return layout

    def _create_rotate_ui(self):
        layout = QtWidgets.QGridLayout()
        self.rotate_header_lbl.setStyleSheet("font: bold")
        self.xmin_header_lbl = QtWidgets.QLabel("X min")
        self.ymin_header_lbl = QtWidgets.QLabel("Y min")
        self.zmin_header_lbl = QtWidgets.QLabel("Z min")
        self.xmax_header_lbl = QtWidgets.QLabel("X max")
        self.ymax_header_lbl = QtWidgets.QLabel("Y max")
        self.zmax_header_lbl = QtWidgets.QLabel("Z max")
        self.xmin_rotate_le = QtWidgets.QLineEdit()
        self.xmin_rotate_le.setFixedWidth(50)
        self.xmax_rotate_le = QtWidgets.QLineEdit()
        self.xmax_rotate_le.setFixedWidth(50)
        self.ymin_rotate_le = QtWidgets.QLineEdit()
        self.ymin_rotate_le.setFixedWidth(50)
        self.ymax_rotate_le = QtWidgets.QLineEdit()
        self.ymax_rotate_le.setFixedWidth(50)
        self.zmin_rotate_le = QtWidgets.QLineEdit()
        self.zmin_rotate_le.setFixedWidth(50)
        self.zmax_rotate_le = QtWidgets.QLineEdit()
        self.zmax_rotate_le.setFixedWidth(50)
        layout.addWidget(self.xmin_header_lbl, 1, 0)
        layout.addWidget(self.ymin_header_lbl, 2, 0)
        layout.addWidget(self.zmin_header_lbl, 3, 0)
        layout.addWidget(self.xmax_header_lbl, 1, 2)
        layout.addWidget(self.ymax_header_lbl, 2, 2)
        layout.addWidget(self.zmax_header_lbl, 3, 2)
        layout.addWidget(self.xmin_rotate_le, 1, 1)
        layout.addWidget(self.xmax_rotate_le, 1, 3)
        layout.addWidget(self.ymin_rotate_le, 2, 1)
        layout.addWidget(self.ymax_rotate_le, 2, 3)
        layout.addWidget(self.zmin_rotate_le, 3, 1)
        layout.addWidget(self.zmax_rotate_le, 3, 3)
        return layout

    def _create_shader_ui(self):
        layout = QtWidgets.QHBoxLayout()
        self.shader_header_lbl.setStyleSheet("font: bold")
        #self.slider = (cmds.colorSliderGrp( label='Blue', rgb=(0, 0, 1) )
        return layout

    def _set_rotate_properties_from_ui(self):
        self.rotate.xmin = self.xmin_rotate_le.text()
        self.rotate.xmax = self.xmax_rotate_le.text()
        self.rotate.ymin = self.ymin_rotate_le.text()
        self.rotate.ymax = self.ymax_rotate_le.text()
        self.rotate.zmin = self.zmin_rotate_le.text()
        self.rotate.zmax = self.zmax_rotate_le.text()
        self.rotate.save()

    def _create_button_ui(self):
        self.apply_btn = QtWidgets.QPushButton("Apply")
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.apply_btn)
        return layout

    #def _create_surface(self):
        #self.surface.createPolygon(self.poly_surface_cmb.currentText())


class Scatter(object):
    """Scatter Tool stuff whheeee"""
    def __init__(self):
        self.density = 1.0
        self.min_scale = 1.0
        self.max_scale = 1.0
        self.xmin_rotate = 0
        self.xmax_rotate = 360
        self.ymin_rotate = 0
        self.ymax_rotate = 360
        self.zmin_rotate = 0
        self.zmax_rotate = 360

    def create_polygon(self):
            if poly_surface_cmb.currentText() = 0
            return cmds.polySphere

    def rotate(self):
        """Makes instances rotate randomly."""
        result = cmds.poly
        transformName = result[0]
        for i in range(0, 50):
            instanceResult = cmds.instance(transformName, name=transformName +
                                                               '_instance#')
            xRot = random.uniform(min(a), max(b))
            yRot = random.uniform(min(c), max(d))
            zRot = random.uniform(min(e), max(f))
            cmds.rotate(xRot, yRot, zRot, instanceResult)
            return

    #polygons = ['Sphere', 'Cube', 'Cylinder', 'Cone', 'Torus', 'Plane', 'Disc']
    #cmds.ls(shapes=True)



    #color( 'sphere1', rgb=(1, 0, 0) )