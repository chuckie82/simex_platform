##########################################################################
#                                                                        #
# Copyright (C) 2015, 2016 Carsten Fortmann-Grote                        #
# Contact: Carsten Fortmann-Grote <carsten.grote@xfel.eu>                #
#                                                                        #
# This file is part of simex_platform.                                   #
# simex_platform is free software: you can redistribute it and/or modify #
# it under the terms of the GNU General Public License as published by   #
# the Free Software Foundation, either version 3 of the License, or      #
# (at your option) any later version.                                    #
#                                                                        #
# simex_platform is distributed in the hope that it will be useful,      #
# but WITHOUT ANY WARRANTY; without even the implied warranty of         #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #
# GNU General Public License for more details.                           #
#                                                                        #
# You should have received a copy of the GNU General Public License      #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.  #
# Include needed directories in sys.path.                                #
#                                                                        #
##########################################################################

""" Module that holds the WavePropagator class.

    @author : CFG
    @institution : XFEL
    @creation 20160321

"""
import os
import h5py
from wpg import Beamline, Wavefront
from wpg.srwlib import srwl
from wpg.wpg_uti_wf import calculate_fwhm, get_intensity_on_axis

from SimEx.Calculators.AbstractPhotonPropagator import AbstractPhotonPropagator


class WavePropagator(AbstractPhotonPropagator):
    """
    Class representing a photon propagator using wave optics through WPG.
    """

    def __init__(self,  parameters=None, input_path=None, output_path=None):
        """
        Constructor for the xfel photon propagator.

        @param  parameters  : Parameters steering the propagation of photons.
        <br/><b>type</b>               : dict

        @param  input_path  : Location of input data for the photon propagation.
        <br/><b>type</b>               : string

        @param  output_path : Location of output data for the photon propagation.
        <br/><b>type</b>               : string
        """

        # Check if beamline was given.
        if isinstance(parameters, Beamline):
            parameters = {'beamline' : parameters}

        # Raise if no beamline in parameters.
        if parameters is None or not 'beamline' in  parameters.keys():
            raise RuntimeError( 'The parameters argument must be an instance of wpg.Beamline or a dict containing the key "beamline" and an instance of wpg.Beamline as the corresponding value.')

        # Initialize base class.
        super(WavePropagator, self).__init__(parameters,input_path,output_path)

        # Take reference to beamline.
        self.__beamline = parameters['beamline']


    def backengine(self):
        """ This method drives the backengine code, in this case the WPG interface to SRW.
	    The similar method from XFELPhotonPropagator.
	"""

	fwhm = calculate_fwhm(self.__wavefront)
	print "source spot size:"
	print(fwhm)	


        # Switch to frequency representation.
        srwl.SetRepresElecField(self.__wavefront._srwl_wf, 'f') # <---- switch to frequency domain

	sz0 = get_intensity_on_axis(self.__wavefront);
        self.__wavefront.custom_fields['/misc/spectrum0'] = sz0

        # Propagate through beamline.
	print (self.__beamline)
        self.__beamline.propagate(self.__wavefront)

	sz1 = get_intensity_on_axis(self.__wavefront);
	self.__wavefront.custom_fields['/misc/spectrum1'] = sz1

        # Switch back to time representation.
        srwl.SetRepresElecField(self.__wavefront._srwl_wf, 't')

	#Resizing: decreasing Range of Horizontal and Vertical Position:
	srwl.ResizeElecField(self.__wavefront._srwl_wf, 'c', [0, 0.25, 1, 0.25,  1]);

	fwhm = calculate_fwhm(self.__wavefront)
	print "x-ray spot size at sample plane:"
	print(fwhm)	


    
	self.__wavefront.custom_fields['/misc/xFWHM'] = fwhm['fwhm_x']
	self.__wavefront.custom_fields['/misc/yFWHM'] = fwhm['fwhm_y']
	self.__wavefront.custom_fields['/params/beamline/printout'] = str(self.__beamline)

	self.__wavefront.custom_fields['/info/contact'] = [
        	'Name: Liubov Samoylova', 'Email: liubov.samoylova@xfel.eu',
        	'Name: Alexey Buzmakov', 'Email: buzmakov@gmail.com']
	self.__wavefront.custom_fields['/info/data_description'] = 'This dataset contains infromation about wavefront propagated through beamline (WPG and SRW frameworks).'
	self.__wavefront.custom_fields['/info/method_description'] = """WPG, WaveProperGator (http://github.com/samoylv/WPG)is an interactive simulation framework for coherent X-ray wavefront propagation.\nSRW, Synchrotron Radiation Workshop (http://github.com/ochubar/SRW),  is a physical optics computer code  for simulation of the radiation wavefront propagation through optical systems of beamlines as well as  detailed characteristics of Synchrotron Radiation (SR) generated by relativistic electrons in magnetic fields of arbitrary configuration."""
	self.__wavefront.custom_fields['/info/package_version'] = '2014.1'


        self.__wavefront.store_hdf5(self.output_path)
	self.add_history(self.output_path, self.input_path)


        return 0

    @property
    def data(self):
        """ Query for the field data. """
        return self.__data

    def _readH5(self):
        """ """
        """ Private method for reading the hdf5 input and extracting the parameters and data relevant to initialize the object. """
        # Check input.
        try:
            self.__h5 = h5py.File( self.input_path, 'r' )
        except:
            raise IOError( 'The input_path argument (%s) is not a path to a valid hdf5 file.' % (self.input_path) )

        # Construct wpg wavefront based on input data.
        self.__wavefront = Wavefront()
        self.__wavefront.load_hdf5(self.input_path)

    def saveH5(self):
        """ """
        """
        Private method to save the object to a file.

        @param output_path : The file where to save the object's data.
        <br/><b>type</b> : string
        <br/><b>default</b> : None
        """

        # This part is included in backengine, no action.




    def add_history(self, wf_file_name, history_file_name):
    	"""
    	Add history from pearent file to propagated file
    
    	:param wf_file_name: output file
    	:param history_file_name: peraent file
    	"""
	print wf_file_name, history_file_name
	
    	with h5py.File(wf_file_name) as wf_h5:
             with h5py.File(history_file_name) as history_h5:
       		if 'history' in wf_h5:
               		del wf_h5['history']
            
            	wf_h5.create_group('/history/parent/')
       	    	wf_h5.create_group('/history/parent/detail')
            
            	for k in history_h5:
                	if k=='history':
                    		try:
                        		history_h5.copy('/history/parent', wf_h5['history']['parent'])
                    		except KeyError:
                        		pass
                        
                	elif not k == 'data':
                    		history_h5.copy(k,wf_h5['history']['parent']['detail'])
                	else:
                    		wf_h5['history']['parent']['detail']['data'] = h5py.ExternalLink(history_file_name,'/data')
