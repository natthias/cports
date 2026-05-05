pkgname = "keepassxc"
pkgver = "2.7.12.25050504"
_commit = "7c7ca4575e7fe6c3412d3fffcd1d5ad580211a17"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DKPXC_FEATURE_UPDATES=OFF",
    "-DWITH_TESTS=ON",
    "-DWITH_GUI_TESTS=ON",
    "-DWITH_APP_BUNDLE=OFF",
    "-DKEEPASSXC_BUILD_TYPE=Release",
]
make_check_wrapper = ["xvfb-run"]
hostmakedepends = [
    "asciidoctor",
    "cmake",
    "ninja",
    "pkgconf",
    "qt6-qtbase",
]
makedepends = [
    "botan-devel",
    "keyutils-devel",
    "libusb-devel",
    "minizip-devel",
    "pcsc-lite-devel",
    "qrencode-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
]
checkdepends = ["xserver-xorg-xvfb"]
pkgdesc = "Cross platform, community-driven port of Keepass Password Safe"
license = "GPL-2.0-only OR GPL-3.0-only"
url = "https://github.com/keepassxreboot/keepassxc"
# source = f"https://github.com/keepassxreboot/keepassxc/archive/refs/tags/{pkgver}.tar.gz"
source = f"https://github.com/keepassxreboot/keepassxc/archive/{_commit}.tar.gz"
sha256 = "5f6aac1db85c8437e608e8bcc7a6923386d4448d6d23819fa5667e0e99be9122"
# causes some tests to fail
hardening = ["!vis", "!cfi"]
# impossible
options = ["!check"]
