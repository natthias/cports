pkgname = "qobine"
pkgver = "0.10.3"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--workspace",
    "--exclude",
    "qobuz-player-web",
]
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
    "protobuf-protoc",
]
makedepends = [
    "alsa-lib-devel",
    "gdk-pixbuf-devel",
    "glib-devel",
    "gtk4-devel",
    "libadwaita-devel",
    "openssl3-devel",
    "pango-devel",
    "sqlite-devel",
    "webkitgtk4-devel",
]
pkgdesc = "Audio player for Qobuz"
license = "GPL-3.0-only"
url = "https://github.com/SofusA/qobine"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "415971d6b8b68a500ebb310b6c15199b93a8caa4ea69f946a8c06dd0ab7f3ab1"


def install(self):
    for suffix in "", "-gtk", "-rfid":
        self.install_bin(
            f"target/{self.profile().triplet}/release/qobuz-player{suffix}"
        )

    self.install_file(
        "flatpak/io.github.sofusa.qobine.desktop", "usr/share/applications"
    )
    self.install_file(
        "flatpak/icon.svg",
        "usr/share/icons/hicolor/scalable/apps",
        name="io.github.sofusa.qobine.svg",
    )
