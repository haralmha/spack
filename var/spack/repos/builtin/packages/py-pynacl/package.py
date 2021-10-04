# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


class PyPynacl(PythonPackage):
    """Python binding to the Networking and Cryptography (NaCl) library."""

    homepage = "https://github.com/pyca/pynacl/"
    pypi = "PyNaCl/PyNaCl-1.4.0.tar.gz"

    version('1.4.0', sha256='54e9a2c849c742006516ad56a88f5c74bf2ce92c9f67435187c3c5953b346505')
    version('1.3.0', sha256='0c6100edd16fefd1557da078c7a31e7b7d7a52ce39fdca2bec29d4f7b6e7600c')

    depends_on('python@2.7:2.8,3.4:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-six', type=('build', 'run'))
    depends_on('py-cffi@1.4.1:', type=('build', 'run'))
    depends_on('py-wheel', type='build')
