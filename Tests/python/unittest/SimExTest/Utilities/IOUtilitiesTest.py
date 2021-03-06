##########################################################################
#                                                                        #
# Copyright (C) 2016 Carsten Fortmann-Grote                              #
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

""" Test module for the entity checks.
    @author CFG
    @institution XFEL
    @creation 20160623 (Day of the UK EU referendum)
"""
import exceptions
import os
import shutil
import numpy
import paths
import unittest

from TestUtilities.TestUtilities import generateTestFilePath
from SimEx.Utilities import IOUtilities

class IOUtilitiesTest(unittest.TestCase):
    """ Test class for the IOUtilities. """

    @classmethod
    def setUpClass(cls):
        """ Setting up the test class. """

    @classmethod
    def tearDownClass(cls):
        """ Tearing down the test class. """

    def setUp(self):
        """ Setting up a test. """
        self.__files_to_remove = []
        self.__paths_to_remove = []

    def tearDown(self):
        """ Tearing down a test. """
        # Clean up.
        for f in self.__files_to_remove:
            if os.path.isfile(f):
                os.remove(f)
        for p in self.__paths_to_remove:
            if os.path.isdir(p):
                shutil.rmtree(p)



    def testLoadPDB(self):
        """ Check that we can load a pdb and convert it to a dict. """

        # Setup path to pdb file.
        pdb_path = generateTestFilePath("2nip.pdb")

        self.__paths_to_remove.append('obsolete')

        # Attempt to load it.
        return_dict = IOUtilities.loadPDB(pdb_path)

        # Check items on dict.
        self.assertIsInstance( return_dict['Z'], numpy.ndarray )
        self.assertIsInstance( return_dict['r'], numpy.ndarray )
        self.assertIsInstance( return_dict['selZ'], dict )
        self.assertIsInstance( return_dict['N'], int )
        self.assertEqual( return_dict['Z'].shape, (4728,) )
        self.assertEqual( return_dict['r'].shape, (4728,3) )

        # Check that return type is a dict.
        self.assertIsInstance( return_dict, dict )

        # Check exception on corrupt file.
        # does not raise due to highly tolerant default acceptance levels in Bio.PDB.
        #self.assertRaises( IOError, IOUtilities.loadPDB, generateTestFilePath("2nip_corrupt.pdb" ) )

        # Check exception on wrong input type.
        self.assertRaises( IOError, IOUtilities.loadPDB, [1,2] )

        # Check exception on wrong file type.
        self.assertRaises( IOError, IOUtilities.loadPDB, generateTestFilePath("sample.h5") )

    def notestQueryPDB(self):
        """ Check that we can query a non-existing pdb from pdb.org and convert it to a dict. """

        # Setup path to pdb file.
        pdb_path = '2nip.pdb'
        self.__files_to_remove.append(pdb_path)
        self.__paths_to_remove.append('obsolete')

        # Attempt to load it.
        return_dict = IOUtilities.loadPDB(pdb_path)

        # Check items on dict.
        self.assertIsInstance( return_dict['Z'], numpy.ndarray )
        self.assertIsInstance( return_dict['r'], numpy.ndarray )
        self.assertIsInstance( return_dict['selZ'], dict )
        self.assertIsInstance( return_dict['N'], int )
        self.assertEqual( return_dict['Z'].shape, (4728,) )
        self.assertEqual( return_dict['r'].shape, (4728,3) )

        # Check that return type is a dict.
        self.assertIsInstance( return_dict, dict )

        # Check exception on wrong input type.
        self.assertRaises( IOError, IOUtilities.loadPDB, 'xyz.pdb' )

    def testQueryPDBDirectory(self):
        """ Check that if the pdb does not exist in the local database, it is queried from pdb.org, save in a dir, and convert it to a dict. """

        # Setup path to pdb file.
        pdb_path = 'pdb/2nip.pdb'
        self.__files_to_remove.append(pdb_path)

        self.__paths_to_remove.append('obsolete')
        self.__paths_to_remove.append('pdb')
        os.mkdir('pdb')

        # Attempt to load it.
        return_dict = IOUtilities.loadPDB(pdb_path)

        # Check items on dict.
        self.assertIsInstance( return_dict['Z'], numpy.ndarray )
        self.assertIsInstance( return_dict['r'], numpy.ndarray )
        self.assertIsInstance( return_dict['selZ'], dict )
        self.assertIsInstance( return_dict['N'], int )
        self.assertEqual( return_dict['Z'].shape, (4728,) )
        self.assertEqual( return_dict['r'].shape, (4728,3) )

        # Check that return type is a dict.
        self.assertIsInstance( return_dict, dict )


if __name__ == '__main__':
    unittest.main()
