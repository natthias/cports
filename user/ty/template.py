pkgname = "ty"
pkgver = "0.0.35"
_ruff_commit = "ac6361d83e4d51ab123043b00d5285a842077b81"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
    "python-build",
    "python-installer",
    "python-maturin",
]
makedepends = [
    "rust-std",
    "zstd-devel",
]
checkdepends = ["python-pytest"]
pkgdesc = "Python type checker and language server"
license = "MIT"
url = "https://github.com/astral-sh/ty"
source = [
    f"{url}/archive/refs/tags/{pkgver}.tar.gz",
    f"https://github.com/astral-sh/ruff/archive/{_ruff_commit}.tar.gz",
]
source_paths = [".", "ruff"]
sha256 = [
    "4d66d83896afa9b7c34398a5fbf5f0d06c643fba3a46084859bf911610d7db5f",
    "0915709c52b8d7fee2c2c1a0e2a24dd25ba1181f127226441f1b290c4748600a",
]
# no thanks
options = ["!check"]


def post_prepare(self):
    # we need these in root of project
    self.do("ln", "-s", "ruff/vendor", "vendor")
    self.do("ln", "-s", "ruff/.cargo", ".cargo")


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self).vendor(wrksrc="ruff")


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_license("LICENSE")
