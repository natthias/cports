pkgname = "mbedtls"
pkgver = "3.6.3"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DENABLE_TESTING=ON",
    "-DUSE_SHARED_MBEDTLS_LIBRARY=ON",
    "-DUSE_STATIC_MBEDTLS_LIBRARY=ON",
]
make_check_args = ["-j1"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "python",
]
makedepends = ["linux-headers"]
pkgdesc = "Light-weight cryptographic and SSL/TLS library"
license = "Apache-2.0 OR GPL-2.0-or-later"
url = "https://www.trustedfirmware.org/projects/mbed-tls"
source = f"https://github.com/Mbed-TLS/mbedtls/releases/download/mbedtls-{pkgver}/mbedtls-{pkgver}.tar.bz2"
sha256 = "64cd73842cdc05e101172f7b437c65e7312e476206e1dbfd644433d11bc56327"


def pre_configure(self):
    # set defines for allowing threads for non-embedded use
    self.do("python3", "scripts/config.py", "set", "MBEDTLS_THREADING_C")
    self.do("python3", "scripts/config.py", "set", "MBEDTLS_THREADING_PTHREAD")


@subpackage("mbedtls-devel")
def _(self):
    return self.default_devel()


@subpackage("mbedtls-progs")
def _(self):
    return self.default_progs()
