pkgname = "idle-inhibit-proxy"
pkgver = "0.1.1"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
makedepends = [
    "dinit-dbus",
    "turnstile",
]
depends = [
    "dbus",
    "elogind",
]
pkgdesc = "DBus service for org.freedesktop.ScreenSaver interface"
license = "BSD-3-Clause"
url = "https://codeberg.org/natthias/idle-inhibit-dbus"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "b9caa349778a6252d2f3c1ceb7873c90b9d80005540baa55b2c399d1700ad1c3"


def post_install(self):
    (
        self.install_file(
            "resources/dinit/idle-inhibit-proxy", "usr/lib/dinit.d/user"
        ),
    )
    self.install_license("LICENSE")
