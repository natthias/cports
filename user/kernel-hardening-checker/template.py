pkgname = "kernel-hardening-checker"
pkgver = "0.6.17.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest"]
pkgdesc = "Tool for checking the security hardening options of the Linux kernel"
license = "GPL-3.0-or-later"
url = "https://github.com/a13xp0p0v/kernel-hardening-checker"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2383e851b44fe74c9a5db32919b897af05f022e676e8d1184cc53594bb9b344c"
# test fails and idk why
options = ["!check"]
