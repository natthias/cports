pkgname = "capsudo"
pkgver = "0.1.3"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["pkgconf"]
makedepends = ["dinit-chimera"]
pkgdesc = "Object capability-based privilege delegation daemon"
license = "ISC"
url = "https://codeberg.org/kaniini"
source = f"{url}/capsudo/archive/v{pkgver}.tar.gz"
sha256 = "129dc60bc203f37e51909091b8b206b5f1fafa398f0fc710ac95d33a70afdff3"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "capsudod")
