pkgname = "inputplumber"
pkgver = "0.77.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "clang-devel",
    "dinit-chimera",
    "libevdev-devel",
    "libiio-devel",
    "linux-headers",
    "udev-devel",
]
pkgdesc = "Input router and remapper daemon"
license = "GPL-3.0-only"
url = "https://github.com/ShadowBlip/InputPlumber"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "cd95c89b99e7e69f57ec8006bb441eab123aa316423abd763e932534c98f3391"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/inputplumber")
    self.install_file(
        "rootfs/usr/share/dbus-1/system.d/org.shadowblip.InputPlumber.conf",
        "usr/share/dbus-1/system.d",
    )
    self.install_file(
        "rootfs/usr/share/polkit-1/actions/org.shadowblip.InputPlumber.policy",
        "usr/share/polkit-1/actions",
    )
    self.install_files("rootfs/usr/share/inputplumber", "usr/share")
    self.install_files("rootfs/usr/lib/udev/hwdb.d", "usr/lib/udev")
    self.install_service(self.files_path / "inputplumber")
    self.install_file(
        self.files_path / "elogind-hook",
        "usr/lib/elogind/system-sleep",
        name="inputplumber",
        mode=0o700,
    )
