pkgname = "helix-plugin"
pkgver = "25.07.1"
_commit = "cba44fdf36d1c728468da73a5373348c7d831fb7"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "git"]
makedepends = ["rust-std"]
pkgdesc = "Fast modal terminal-based text editor"
license = "MPL-2.0"
url = "https://github.com/mattwparas/helix/tree/steel-event-system"
source = f"https://github.com/mattwparas/helix/archive/{_commit}.tar.gz"
sha256 = "dd043f5db3da2735eb6bd0bd4b56c52ffbfb7c18fec3e90e7a8c450067e52f8c"
env = {
    "HELIX_DEFAULT_RUNTIME": "/usr/lib/helix/runtime",
    "HELIX_DISABLE_AUTO_GRAMMAR_BUILD": "1",
}
# FIXME lintpixmaps
options = ["!lintpixmaps"]

if self.profile().wordsize == 32:
    broken = "needs atomic64"


def post_prepare(self):
    from cbuild.util import cargo

    cargo.clear_vendor_checksums(self, "cc")


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/hx")
    runtime_dir = "usr/lib/helix/runtime"
    self.install_dir(runtime_dir)

    self.install_files("runtime/queries", runtime_dir)
    self.install_files("runtime/themes", runtime_dir)
    self.install_file("runtime/tutor", runtime_dir)

    self.install_completion("contrib/completion/hx.bash", "bash", "hx")
    self.install_completion("contrib/completion/hx.fish", "fish", "hx")
    self.install_completion("contrib/completion/hx.zsh", "zsh", "hx")

    self.install_file("contrib/helix.png", "usr/share/pixmaps")
    self.install_file("contrib/Helix.desktop", "usr/share/applications")
