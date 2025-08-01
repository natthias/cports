pkgname = "gnome-terminal"
pkgver = "3.56.2"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
]
hostmakedepends = [
    "docbook-xsl-nons",
    "gettext",
    "glib-devel",
    "itstool",
    "libxslt-progs",
    "meson",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "gsettings-desktop-schemas-devel",
    "gtk+3-devel",
    "libhandy-devel",
    "nautilus-devel",
    "pcre2-devel",
    "util-linux-uuid-devel",
    "vte-gtk3-devel",
]
pkgdesc = "GNOME terminal emulator"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/Terminal"
source = f"$(GNOME_SITE)/gnome-terminal/{pkgver[: pkgver.rfind('.')]}/gnome-terminal-{pkgver}.tar.xz"
sha256 = "235bc09dfa34cc5f1e95122e9bf60203a84daf861cfacf7e4496c5f548239978"
# Upstream claims "LTO very much NOT supported"
# https://gitlab.gnome.org/GNOME/gnome-terminal/-/blob/09c8b31168460c325ac00820759d6eefdf3957ab/meson.build#L226
options = ["!cross", "!lto"]


def post_install(self):
    self.uninstall("usr/lib/systemd")


@subpackage("gnome-terminal-nautilus-extension")
def _(self):
    self.pkgdesc = "GNOME terminal extension for Nautilus"
    self.depends += [self.parent]
    self.install_if = [self.parent, "nautilus"]
    self.renames = ["nautilus-gnome-terminal-extension"]

    return [
        "usr/lib/nautilus",
        "usr/share/metainfo/org.gnome.Terminal.Nautilus.metainfo.xml",
    ]
