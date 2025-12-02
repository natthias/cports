pkgname = "emmylua-analyzer-rust"
pkgver = "0.23.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["openssl3-devel"]
pkgdesc = "LSP, documentation generator, and static analysis for Lua"
license = "MIT"
url = "https://github.com/EmmyLuaLs/emmylua-analyzer-rust"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "9720bf016002a8d0df6bdcdc7c4ac148d0bc13b11115f50ff314c6c1a047498b"


def install(self):
    for bin in (
        "emmylua_check",
        "emmylua_doc_cli",
        "luafmt",
        "emmylua_ls",
    ):
        self.install_bin(f"target/x86_64-chimera-linux-musl/release/{bin}")

    self.install_license("LICENSE")
