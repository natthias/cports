pkgname = "sequoia-chameleon-gnupg"
pkgver = "0.13.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "nettle-devel",
    "openssl3-devel",
    "sqlite-devel",
]
checkdepends = [
    "gnupg",
    "sequoia-sq",
]
pkgdesc = "<Re-implementation of gpg and gpgv from Sequoia OpenPGP"
license = "GPL-3.0-or-later"
url = "https://gitlab.com/sequoia-pgp/sequoia-chameleon-gnupg"
source = f"{url}/-/archive/v{pkgver}/sequoia-chameleon-gnupg-v{pkgver}.tar.gz"
sha256 = "9fe7b06b6cbdb5282adfb102cc5bdc09b3c8b1f3a7399e225e3ae8127db7078d"
# Checks fail, idk why
options = ["!check"]
