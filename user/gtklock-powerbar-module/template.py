pkgname = "gtklock-powerbar-module"
pkgver = "4.0.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = ["gtk+3-devel"]
pkgdesc = "Module for gtklock adding power controls to the lockscreen"
license = "GPL-3.0-only"
url = "https://github.com/jovanlanik/gtklock-powerbar-module"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7fefa48ddb9a60e58b5c72df6da2005e1dd38fdc779c5d535aac80da9b508e9e"
