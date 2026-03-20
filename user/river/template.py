pkgname = "river"
pkgver = "0.4.1"
pkgrel = 0
_zigver = "0.15.2"
hostmakedepends = ["pkgconf", "scdoc", "zvm"]
makedepends = [
    "libevdev-devel",
    "libxkbcommon-devel",
    "pixman-devel",
    "wayland-devel",
    "wayland-protocols",
    "wlroots0.19-devel",
]
depends = ["xwayland"]
pkgdesc = "Dynamic tiling wayland compositor"
license = "GPL-3.0-or-later"
url = "https://codeberg.org/river/river"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "e61fc010d07a8c1ed662a5b9ea5b06bb5c67efd2720dc991b5eee1ff7d883b8f"
env = {
    "DESTDIR": "zig-out",
    "ZVM_PATH": "/cbuild_cache/zig/zvm",
}


def prepare(self):
    self.do("zvm", "install", _zigver, allow_network=True)
    self.do(
        "zvm",
        "run",
        _zigver,
        "build",
        "--fetch",
        "--global-cache-dir",
        "/cbuild_cache/zig",
        allow_network=True,
    )


def build(self):
    self.do(
        "zvm",
        "run",
        _zigver,
        "build",
        "--global-cache-dir",
        "/cbuild_cache/zig",
        "-Doptimize=ReleaseSafe",
        "-Dpie",
        "-Dxwayland",
        "--prefix",
        "/usr",
    )


def check(self):
    self.do(
        "zvm",
        "run",
        _zigver,
        "build",
        "test",
        "--global-cache-dir",
        "/cbuild_cache/zig",
        "-Doptimize=ReleaseSafe",
        "-Dpie",
        "-Dxwayland",
        "--prefix",
        "/usr",
    )


def install(self):
    self.install_bin("zig-out/usr/bin/river")

    self.install_man("zig-out/usr/share/man/man1/river.1")

    self.install_file(
        "zig-out/usr/share/pkgconfig/river-protocols.pc", "usr/share/pkgconfig"
    )
    self.install_files(
        "zig-out/usr/share/river-protocols",
        "usr/share",
    )
