# -*- coding: utf-8 -*-

"""
/***************************************************************************
 ProgramacaoAplicadaGrupo4
                                 A QGIS plugin
 Solução do Grupo 4
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2024-02-26
        copyright            : (C) 2024 by Grupo 4
        email                : Grupo4@ime.eb.br
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
__date__ = '2024-02-26'
__copyright__ = '(C) 2024 by Grupo 4'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (QgsProcessing,
                       QgsFeatureSink,
                       QgsProcessingException,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterFeatureSink,
                       QgsProcessingParameterDistance,
                       QgsProcessingParameterRasterLayer)
from qgis import processing
"""
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

class Projeto1Solucao(QgsProcessingAlgorithm):

    VIA = 'VIA' #Camada da via
    RVIA ='RVIA' # raio do buffer da via 
    VGT = 'VGT' # camada vegetação 
    MDA = 'MDA' # Camada Massa d'água
    TD = 'TD'   # Camada Trecho de drenagem 
    RTD ='RTD'  # Raio do buffer do trecho de drenagem 
    RMC ='RMC'  # Raio do buffer mata ciliar 
    AED ='AED'  # Camada Área edificada
    ASD ='ASD'  # Área sem dados 
    MDT = 'MDT' # MDT
    TP = 'TP'   # Tamanho do pixel 
    OUTPUT_VIA= 'OUTPUT_VIA'
    OUTPUT_DRENAGEM= 'OUTPUT_DRENAGEM'
    OUTPUT_MATA_CILIAR= 'OUTPUT_MATA_CILIAR'


    def tr(self, string):
    
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return Projeto1Solucao()

    def name(self):
        return 'projeto1solucao'

    def displayName(self):
        return self.tr('Projeto 1')

    def group(self):
        return self.tr('Projeto')

    def groupId(self):
        return 'projeto1'

    def shortHelpString(self):
        return self.tr("Projeto para identificação de trafegabilidade")

    def initAlgorithm(self, config=None):

        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.VIA,
                self.tr('Camada Via de deslocamento'),
                [QgsProcessing.TypeVectorLine]
            )
        )
        
        self.addParameter (
            QgsProcessingParameterDistance (
                self.RVIA,
                self.tr('Buffer para a via de deslocamento' ),
                parentParameterName =self.VIA ,
                minValue=0,
                defaultValue =1.0
            )
)

        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.VGT,
                self.tr('Camada Vegetação'),
                [QgsProcessing.TypeVectorPolygon]
            )
        )
        
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.MDA,
                self.tr("Camada Massa d'agua "),
                [QgsProcessing.TypeVectorPolygon]
            )
        )

        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.TD,
                self.tr('Camada Trecho de Drenagem'),
                [QgsProcessing.TypeVectorLine]
            )
        )
        
        self.addParameter (
            QgsProcessingParameterDistance (
                self.RTD,
                self.tr('Buffer Trecho de deslocamento' ),
                parentParameterName =self.TD ,
                minValue=0,
                defaultValue =1.0
            )
)       
        self.addParameter (
            QgsProcessingParameterDistance (
                self.RMC,
                self.tr('Buffer da Mata ciliar' ),
                parentParameterName =self.VGT ,
                minValue=0,
                defaultValue =1.0
            )
)    

        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.AED,
                self.tr("Camada Área edificada"),
                [QgsProcessing.TypeVectorPolygon]
            )
        )   

        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.ASD,
                self.tr("Camada Área sem dados"),
                [QgsProcessing.TypeVectorPolygon]
            )
        )

        self.addParameter (
            QgsProcessingParameterDistance (
                self.RTD,
                self.tr('Buffer Trecho de deslocamento' ),
                parentParameterName =self.TD ,
                minValue=0,
                defaultValue =1.0
            )
)    

        self.addParameter (
            QgsProcessingParameterDistance (
                self.TP,
                self.tr('Tamanho do pixel'),
                parentParameterName =self.MDT ,
                minValue=0,
                defaultValue =1.0
            )
)           
        
        self.addParameter(
            QgsProcessingParameterRasterLayer(
                self.MDT,
                self.tr("Camada MDT"),
                [QgsProcessing.TypeRaster]
            )
        )   
        

        # We add a feature sink in which to store our processed features (this
        # usually takes the form of a newly created vector layer when the
        # algorithm is run in QGIS).
        self.addParameter(
            QgsProcessingParameterFeatureSink(
                self.OUTPUT_VIA,
                self.tr('Output Via')
            )
        )

        self.addParameter(
            QgsProcessingParameterFeatureSink(
                self.OUTPUT_DRENAGEM,
                self.tr('Output Trecho de Drenagem')
            )
        )

        self.addParameter(
            QgsProcessingParameterFeatureSink(
                self.OUTPUT_MATA_CILIAR,
                self.tr('Output Mata Ciliar')
            )
        )

    def processAlgorithm(self, parameters, context, feedback):
        vias = self.parameterAsSource(
            parameters,
            self.VIA,
            context
        )

        mdagua = self.parameterAsSource(
            parameters,
            self.MDA,
            context
        )

        areaEdificada = self.parameterAsSource(
            parameters,
            self.AED,
            context
        )

        vegetacao = self.parameterAsSource(
            parameters,
            self.VGT,
            context
        )

        trechoDrenagem = self.parameterAsSource(
            parameters,
            self.TD,
            context
        )

        ModeloDigitaldoTerreno = self.parameterAsSource(
            parameters,
            self.MDT,
            context
        )        



        raioVia = self.parameterAsDouble(
            parameters, 
            self.RVIA,
            context
        )

        raioTrechoDrenagem =  self.parameterAsDouble(
            parameters, 
            self.RTD,
            context
        )

        raioMataCiliar =  self.parameterAsDouble(
            parameters, 
            self.RMC,
            context)
        

        
        # If source was not found, throw an exception to indicate that the algorithm
        # encountered a fatal error. The exception text can be any string, but in this
        # case we use the pre-built invalidSourceError method to return a standard
        # helper text for when a source cannot be evaluated
        if vias is None:
            raise QgsProcessingException(self.invalidSourceError(parameters, self.VIA))

        (sink_vias, dest_id_vias) = self.parameterAsSink(
            parameters,
            self.OUTPUT_VIA,
            context,
            vias.fields(),
            vias.wkbType(),
            vias.sourceCrs()
        )

        (sink_drenagem, dest_id_drenagem) = self.parameterAsSink(
            parameters,
            self.OUTPUT_DRENAGEM,
            context,
            trechoDrenagem.fields(),
            trechoDrenagem.wkbType(),
            trechoDrenagem.sourceCrs()
        )

        (sink_vegetacao, dest_id_mataciliar) = self.parameterAsSink(
            parameters,
            self.OUTPUT_MATA_CILIAR,
            context,
            vegetacao.fields(),
            vegetacao.wkbType(),
            vegetacao.sourceCrs()
        )

        # Send some information to the user
        feedback.pushInfo(f'CRS is {vias.sourceCrs().authid()}')

        # If sink was not created, throw an exception to indicate that the algorithm
        # encountered a fatal error. The exception text can be any string, but in this
        # case we use the pre-built invalidSinkError method to return a standard
        # helper text for when a sink cannot be evaluated
        # if sink_drenagem or sink_vegetacao or sink_vias is None:
        if sink_vias is None:
            raise QgsProcessingException(self.invalidSinkError(parameters, self.OUTPUT_VIA))
        
        # Compute the number of steps to display within the progress bar and
        # get features from source
        total = 100.0 / vias.featureCount() if vias.featureCount() else 0
        features = vias.getFeatures()

        for current, feature in enumerate(features):
            # Stop the algorithm if cancel button has been clicked
            if feedback.isCanceled():
                break

            # Add a feature in the sink
            sink_vias.addFeature(feature, QgsFeatureSink.FastInsert)

            # Update the progress bar
            feedback.setProgress(int(current * total))

        #Obter via de deslocamento 
        viaDeslocamento = processing.run("native:buffer", 
            {'INPUT':dest_id_vias,
             'DISTANCE':raioVia,
             'SEGMENTS':5,
             'END_CAP_STYLE':0,
             'JOIN_STYLE':0,
             'MITER_LIMIT':2,
             'DISSOLVE':False,
             'SEPARATE_DISJOINT':False,
             'OUTPUT': 'memory:'},
            context=context, feedback=feedback)['OUTPUT']
        # #Obter o trecho de drenagem 
        
        trechoDrenagemFinal = processing.run("native:buffer", 
            {'INPUT':dest_id_drenagem,
             'DISTANCE':raioTrechoDrenagem,
             'SEGMENTS':5,
             'END_CAP_STYLE':0,
             'JOIN_STYLE':0,
             'MITER_LIMIT':2,
             'DISSOLVE':False,
             'SEPARATE_DISJOINT':False,
             'OUTPUT':'memory:'},
             context=context, feedback=feedback)['OUTPUT']
        
        # Obter mata ciliar 
        mataCiliarFinal = processing.run("native:buffer", 
            {'INPUT':dest_id_mataciliar,
             'DISTANCE':raioMataCiliar,
             'SEGMENTS':5,
             'END_CAP_STYLE':0,
             'JOIN_STYLE':0,
             'MITER_LIMIT':2,
             'DISSOLVE':False,
             'SEPARATE_DISJOINT':False,
             'OUTPUT':'memory:'},
              context=context, feedback=feedback)['OUTPUT']
        
        # Extrair Vias de deslocamento federal
        # viaFederal = processing.run("native:extractbyexpression", 
        #        {'INPUT':viaDeslocamento,
        #         'EXPRESSION':'"tipo"  = 2 and ( "jurisdicao" = 1 or  "jurisdicao" =2 )',
        #          'OUTPUT':'TEMPORARY_OUTPUT'},
        #          context = context, feedback = feedback)['OUTPUT'] 
                
        return {self.OUTPUT_VIA: dest_id_vias,
                self.OUTPUT_DRENAGEM: dest_id_drenagem,
                self.OUTPUT_MATA_CILIAR: dest_id_mataciliar
                }
