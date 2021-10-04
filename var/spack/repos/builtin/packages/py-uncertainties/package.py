# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyUncertainties(PythonPackage):
    """Transparent calculations with uncertainties on the quantities involved
    (aka error propagation); fast calculation of derivatives
    """

    homepage = "https://uncertainties-python-package.readthedocs.io/en/latest/"
    pypi = "uncertainties/uncertainties-3.1.4.tar.gz"

    version('3.1.4', sha256='63548a94899f2a51eeb89b640f6ac311f481a8016b37dce157186e44619bc968')
    version('3.1.2', sha256='ba07c17a8a78cb58a47cd373079c7ea459f8b26cd474e29163b6ba0d72856a1e')

    variant('optional', default=False, description='Enable extra features involving numpy')
    variant('docs',  default=False, description='Build with documentation')

    depends_on('python@2.7:',   type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-future',     type=('build', 'run'))
    depends_on('py-numpy',      type=('build', 'run'), when='+optional')
    depends_on('py-sphinx',     type='build', when='+docs')
