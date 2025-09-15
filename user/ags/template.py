pkgname = "ags"
pkgver = "3.1.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "go",
    "meson",
    "nodejs",
    "pkgconf",
]
makedepends = [
    "gjs",
    "gtk4-layer-shell-devel",
]
depends = [
    "gjs",
    "libastal4",
    "nodejs",
    "sassc",
]
pkgdesc = "CLI for Astal & TypeScript"
license = "GPL-3.0-or-later"
url = "https://github.com/Aylur/ags"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7c9bf38cddfa9661ca3bc70268df0f3124174dad0d6ff85433445816471690f4"


def prepare(self):
    self.do("npm", "install", allow_network=True)


def post_prepare(self):
    from cbuild.util import golang

    self.do("touch", "go.mod")

    golang.Golang(self).mod_download(wrksrc="cli")


def init_build(self):
    from cbuild.util import golang

    self.make_env.update(golang.get_go_env(self))


@subpackage("ags-types")
def _(self):
    self.install_if = [self.parent]
    self.subdesc = "type genration dependencies"
    self.depends = [
        self.parent,
        "glib-devel",
        "gobject-introspection",
        "gtk4-devel",
        "libastal-battery-devel",
        "libastal-io-devel",
        "libastal-network-devel",
        "libastal-river-devel",
        "libastal-wireplumber-devel",
        "libastal4-devel",
    ]
    self.options = ["empty"]
    return []
