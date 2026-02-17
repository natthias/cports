pkgname = "steel"
pkgver = "0.8.2"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = ["libgit2-devel", "openssl3-devel"]
pkgdesc = "Embedded scheme interpreter in Rust"
license = "Apache-2.0 OR MIT"
url = "https://github.com/mattwparas/steel"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "06b11190a7c8bdfbe35bf9bd7d2e304569c3781278d3412e6436a2ff5b1e62e6"
# don't work, idc
options = ["!check"]


def prepare(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc=".").vendor()


def build(self):
    from cbuild.util import cargo

    self.make_env["LIBGIT2_NO_VENDOR"] = "0"  # libgit2 is outdated
    cargo.Cargo(self, wrksrc=".").build()
    cargo.Cargo(self, wrksrc="crates/forge").build()
    cargo.Cargo(self, wrksrc="crates/steel-language-server").build()


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/steel")
    self.install_bin(f"target/{self.profile().triplet}/release/forge")
    self.install_bin(
        f"target/{self.profile().triplet}/release/steel-language-server"
    )

    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-APACHE")
