pkgname = "libastal4"
pkgver = "0_git20253004"
_commit = "67ddc83e0bdbda6de7f6f15e4fbc5d6b9d2d1b18"
pkgrel = 0
build_wrksrc = "lib/astal/gtk4"
build_style = "meson"
configure_args = ["-Ddefault_library=shared"]
hostmakedepends = [
    "gobject-introspection",
    "meson",
    "pkgconf",
    "vala",
    "vala-valadoc",
]
makedepends = ["gtk4-devel", "gtk4-layer-shell-devel", "libastal-io-devel"]
depends = ["libastal-io"]
pkgdesc = "Building blocks for building desktop shells with GTK4"
license = "LGPL-2.1-or-later"
url = "https://github.com/Aylur/astal"
source = f"https://github.com/Aylur/astal/archive/{_commit}.tar.gz"
sha256 = "fe9ac3e126271de1d871ca0d5992be952835df2d89765181df1180e31cbf0391"


@subpackage("libastal4-devel")
def _(self):
    return self.default_devel()
