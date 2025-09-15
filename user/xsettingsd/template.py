pkgname = "xsettingsd"
pkgver = "1.0.2"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
]
makedepends = [
    "libx11-devel",
    "turnstile",
]
pkgdesc = "Daemon that implements the XSETTINGS specification"
license = "BSD-3-Clause"
url = "https://codeberg.org/derat/xsettingsd"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "f751c7ff3f93ab088f3d31a4cb70ec415c22ec1bf832647d650b2b383cb1bf5d"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
    self.rm(self.destdir / "usr/lib/systemd", recursive=True)
    self.install_service(self.files_path / "xsettingsd.user")
