pkgname = "muon"
pkgver = "0.5.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "scdoc"]
makedepends = [
    "curl-devel",
    "libarchive-devel",
    "pkgconf-devel",
]
pkgdesc = "C99 implementation of the meson build system"
license = "GPL-3.0-only AND MIT AND Apache-2.0 AND Unlicense AND Python-2.0"
url = "https://github.com/muon-build/muon"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "565c1b6e1e58f7e90d8813fda0e2102df69fb493ddab4cf6a84ce3647466bee5"
hardening = ["vis", "cfi"]


def post_install(self):
    for license in (
        "Apache-2.0.txt",
        "MIT.txt",
        "Python-2.0.txt",
        "Unlicense.txt",
    ):
        self.install_license(f"LICENSES/{license}")
