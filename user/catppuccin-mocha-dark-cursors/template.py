pkgname = "catppuccin-mocha-dark-cursors"
pkgver = "2.0.0"
pkgrel = 0
pkgdesc = "Soothing pastel cursors - dark"
license = "GPL-3.0-only"
url = "https://github.com/catppuccin/cursors"
source = f"{url}/releases/download/v{pkgver}/catppuccin-mocha-dark-cursors.zip"
sha256 = "a4d976491bdb1b1311b2de88327cad3f1c66c2d9da896e0c56362a660c802585"


def install(self):
    self.install_files(
        "cursors", "usr/share/icons/Catppuccin-Mocha-Dark-Cursors"
    )
    self.install_file(
        "index.theme", "usr/share/icons/Catppuccin-Mocha-Dark-Cursors"
    )
