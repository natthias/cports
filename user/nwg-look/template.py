pkgname = "nwg-look"
pkgver = "1.1.1"
pkgrel = 0
build_style = "go"
hostmakedepends = [
    "go",
    "pkgconf",
]
makedepends = [
    "gtk+3-devel",
]
pkgdesc = "GTK3 settings editor adapted to work in the wlroots environment"
license = "MIT"
url = "https://github.com/nwg-piotr/nwg-look"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "568c5efe443892d74ffce6cf8ac7db2aea6071be70d97d3ba7c5efd8b351e601"
# no
options = ["!check"]


def post_install(self):
    self.install_file("stuff/main.glade", "usr/share/nwg-look")
    self.install_file("stuff/nwg-look.desktop", "usr/share/applications")
    self.install_file(
        "stuff/nwg-look.svg", "usr/share/icons/hicolor/scalable/apps"
    )

    self.install_file("langs/*.json", "usr/share/nwg-look/langs", glob=True)

    self.install_license("LICENSE")
