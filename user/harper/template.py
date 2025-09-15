pkgname = "harper"
pkgver = "2.1.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = ["zstd-devel"]
pkgdesc = "Grammar Checker for Developers"
license = "Apache-2.0"
url = "https://github.com/Automattic/harper"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2e04700a4755194e6aac904c1dc186be5c9d32946efa0e8eeb8f8bfdfaf434fd"


def install(self):
    self.install_bin("target/x86_64-chimera-linux-musl/release/harper-cli")
    self.install_bin("target/x86_64-chimera-linux-musl/release/harper-ls")
