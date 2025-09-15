pkgname = "gtk-session-lock"
pkgver = "0.2.0"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "gobject-introspection",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "gtk+3-devel",
    "wayland-protocols",
]
pkgdesc = "Library to create screen lockers using the ext-session-lock protocol"
license = "GPL-3.0-or-later"
url = "https://github.com/Cu3PO42/gtk-session-lock"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a4245c6930580c15ed263b9a7bb7e39f47693baec78be1026b4e0e28b233cb4e"
hardening = ["vis", "!cfi"]
# tests are weird
options = ["!check"]


@subpackage("gtk-session-lock-devel")
def _(self):
    return self.default_devel()
