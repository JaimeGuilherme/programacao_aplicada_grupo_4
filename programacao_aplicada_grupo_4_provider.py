# -*- coding: utf-8 -*-

"""
/***************************************************************************
 ProgramacaoAplicadaGrupo4
                                 A QGIS plugin
 Solução do Grupo 4
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2024-03-24
        copyright            : (C) 2024 by Grupo 4
        email                : jaime.breda@ime.eb.br
                               ppsramalho1505@ime.eb.br
                               samuel.rodrigues.silva2305@ime.eb.br
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

__author__ = 'Grupo 4'
__date__ = '2024-06-16'
__copyright__ = '(C) 2024 by Grupo 4'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

from qgis.core import QgsProcessingProvider
from .algorithms.Projeto1.solucao import Projeto1Solucao
from .algorithms.Projeto1.solucao_complementar import Projeto1SolucaoComplementar
#from .algorithms.Projeto2.solucao import Projeto2Solucao (Problema de carregamento do algoritmo)
#from .algorithms.Projeto2.solucao_complementar import Projeto2SolucaoComplementar (Problema de carregamento do algoritmo)
from .algorithms.Projeto3.solucao import Projeto3Solucao
from .algorithms.Projeto3.solucao_complementar import Projeto3SolucaoComplementar
from .algorithms.Projeto4.solucao import Projeto4Solucao
from .algorithms.Projeto4.solucao_complementar import Projeto4SolucaoComplementar


class ProgramacaoAplicadaGrupo4Provider(QgsProcessingProvider):

    def __init__(self):
        """
        Default constructor.
        """
        QgsProcessingProvider.__init__(self)

    def unload(self):
        """
        Unloads the provider. Any tear-down steps required by the provider
        should be implemented here.
        """
        pass

    def loadAlgorithms(self):
        """
        Loads all algorithms belonging to this provider.
        """
        self.addAlgorithm(Projeto1Solucao())
        self.addAlgorithm(Projeto1SolucaoComplementar())
        #self.addAlgorithm(Projeto2Solucao()) (Problema de carregamento do algoritmo)
        #self.addAlgorithm(Projeto2SolucaoComplementar()) (Problema de carregamento do algoritmo)
        self.addAlgorithm(Projeto3Solucao())
        self.addAlgorithm(Projeto3SolucaoComplementar())
        self.addAlgorithm(Projeto4Solucao())
        self.addAlgorithm(Projeto4SolucaoComplementar())
        # add additional algorithms here
        # self.addAlgorithm(MyOtherAlgorithm())

    def id(self):
        """
        Returns the unique provider id, used for identifying the provider. This
        string should be a unique, short, character only string, eg "qgis" or
        "gdal". This string should not be localised.
        """
        return 'ProgramacaoAplicadaGrupo4'

    def name(self):
        """
        Returns the provider name, which is used to describe the provider
        within the GUI.

        This string should be short (e.g. "Lastools") and localised.
        """
        return self.tr('ProgramacaoAplicadaGrupo4')

    def icon(self):
        """
        Should return a QIcon which is used for your provider inside
        the Processing toolbox.
        """
        return QgsProcessingProvider.icon(self)

    def longName(self):
        """
        Returns the a longer version of the provider name, which can include
        extra details such as version numbers. E.g. "Lastools LIDAR tools
        (version 2.2.1)". This string should be localised. The default
        implementation returns the same string as name().
        """
        return self.name()
