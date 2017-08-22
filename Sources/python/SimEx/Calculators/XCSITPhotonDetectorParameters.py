##########################################################################
#                                                                        #
# Copyright (C) 2015-2017 Jan-Philipp Burchert, Carsten Fortmann-Grote   #
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
#                                                                        #
##########################################################################

import so

from SimEx.Parameters.AbstractCalculatorParameters import AbstractCalculatorParameters
from SimEx.Utilities.EntityChecks import checkAndSetInstance

class XCSITPhotonDetectorParameters(AbstractCalculatorParameters):
	"""
	Datastructure to store the necessary parameters for a XCSITPhotonDetector
	simulation
	"""

	# set the only allowed attributes of instances of this class
	__slots__ = "__detector_type",
				"__plasma_search_flag",
				"__plasma_simulation_flag",
				"__point_simulation_method"


	# Create the instance attributes
	def __init__(self,
				detector_type=None
				plasma_search_flag=None
				plasma_simulation_flag=None
				point_simulation_method=None):
		"""
		fields required to run the simulation

        :param detector_type: The detector type to simulate ("pnCCD" | "LPD" | "AGIPD | "AGIPDSPB").
        :type detector_type: str

        :param plasma_search_flag: Flag for the plasma search method ("BLANK").
        :type plasma_search_flag: str

        :param plasma_simulation_flag: Flag for the plasma simulation method ("BLANKPLASMA").
        :type plasma_simulation_flag: str

        :param point_simulation_method: Method for the charge point simulation ("FULL" | "FANO" | "LUT" | "BINNING").
        :type point_simulation_method: str
		"""
		
		# Use the setters: They check the type of the input and set the private
		# attributes or raise an exception if the the type does not match the
		# required type
		self.detector_type(detector_type)
		self.plasma_search_flag(plasma_search_flag)
		self.plasma_simulation_flag(plasma_simulation_flag)
		self.point_simulation_method(point_simulation_method)


	# Getter and Setter
	# getter raise an AttributeError if the attribute accessed by the called
	# getter is still of type None
	# setter check the input type with SimEx.Utilities.EntityChecks
	# checkAndSetInstance function -> raise an error if input type is not
	# matching
	@property
	def detector_type(self):
		"""
		:return string containing the detector name
		"""
		if self.__detector_type is None:
			raise AttributeError("Attribute detector_type has not been set yet.")
		else:
			return self.__detector_type
	@detector_type.setter
	def detector_type(self,value)
		"""
		:param value, a string with the detector name
		"""
		self.__detector_type = checkAndSetInstance(str,value,None)


	@property
	def plasma_search_flag(self):
		"""
		:return string, the plasma search method
		"""
		if self.__plasma_search_flag is None:
			raise AttributeError("Attribute plasma_search_flag has not been set yet.")
		else:
			return self.__plasma_search_flag
	@plasma_search_flag.setter
	def plasma_search_flag(self,value)
		"""
		:param value, a string, the plasma search method
		"""
		self.__plasma_search_flag = checkAndSetInstance(str,value,None)


	@property
	def plasma_simulation_flag(self):
		"""
		:return string, the plasma simulation method
		"""
		if self.__plasma_simulation_flag is None:
			raise AttributeError("Attribute plasma_simulation_flag has not been set yet.")
		else:
			return self.__plasma_simulation_flag
	@plasma_simulation_flag.setter
	def plasma_simulation_flag(self,value)
		"""
		:param value, a string, the plasma simulation method
		"""
		self.__plasma_simulation_flag = checkAndSetInstance(str,value,None)


	@property
	def point_simulation_method(self):
		"""
		:return string, the charge simulation method
		"""
		if self.__point_simulation_method is None:
			raise AttributeError("Attribute point_simulation_method has not been set yet.")
		else:
			return self.__point_simulation_method
	@point_simulation_method.setter
	def point_simulation_method(self,value)
		"""
		:param value, a string, the charge simulation method
		"""
		self.__point_simulation_method = checkAndSetInstance(str,value,None)
