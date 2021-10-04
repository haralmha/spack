# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPandocfilters(PythonPackage):
    """A python module for writing pandoc filters"""

    homepage = "https://github.com/jgm/pandocfilters"
    pypi = "pandocfilters/pandocfilters-1.4.2.tar.gz"

    version('1.4.3', sha256='bc63fbb50534b4b1f8ebe1860889289e8af94a23bff7445259592df25a3906eb')
    version('1.4.2', sha256='b3dd70e169bb5449e6bc6ff96aea89c5eea8c5f6ab5e207fc2f521a2cf4a0da9')
