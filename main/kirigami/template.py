pkgname = "kirigami"
pkgver = "6.13.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "qt6-qtbase-private-devel",  # qguiapplication_p.h
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE's QtQuick based UI component set"
license = "LGPL-2.0-only"
url = "https://develop.kde.org/frameworks/kirigami"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kirigami-{pkgver}.tar.xz"
sha256 = "dd5aa1b5b8fbc4eb731227851af7ca9caa1dcaac0dc99421dbd3d0d58d988329"
hardening = ["vis"]

_have_omp = self.profile().arch in [
    "aarch64",
    "loongarch64",
    "ppc64le",
    "ppc64",
    "riscv64",
    "x86_64",
]

if _have_omp:
    makedepends += ["libomp-devel"]


@subpackage("kirigami-devel")
def _(self):
    self.depends += ["qt6-qtdeclarative-devel"]
    if _have_omp:
        self.depends += ["libomp-devel"]
    return self.default_devel()
