pkgname = "doxygen"
pkgver = "1.18.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DCMAKE_BUILD_TYPE=Release", "-Duse_sys_sqlite3=ON"]
hostmakedepends = ["cmake", "ninja", "perl", "python", "flex", "bison"]
makedepends = ["sqlite-devel"]
checkdepends = ["libxml2-progs"]
pkgdesc = "Source code documentation generator tool"
license = "GPL-2.0-only"
url = "https://doxygen.nl"
source = f"{url}/files/doxygen-{pkgver}.src.tar.gz"
sha256 = "a1deed70a6785bbec95a2b2a9e419dc7f7b223a9d74a8644ae611c8e2dcdd354"
hardening = ["vis", "cfi"]


def post_extract(self):
    # needs texlive stuff
    self.rm("testing/012_cite.dox")
    # xmllint produces different outputs on semantically identical input
    self.rm("testing/009_bug.cpp")


def post_install(self):
    self.install_man("doc/doxygen.1")
