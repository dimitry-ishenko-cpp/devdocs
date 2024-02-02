# [devdocs](https://devdocs.io) + [fzf](https://github.com/junegunn/fzf) + [w3m](https://w3m.sourceforge.net/) = ☯

What happens when you combine _[devdocs](https://devdocs.io)_ API documentation, _[fzf](https://github.com/junegunn/fzf)_ fuzzy finder
and _[w3m](https://w3m.sourceforge.net/)_ text-based browser?

![](./image/showcase.gif)

## Installation

Stable version (requires [CMake](https://cmake.org/) >= 3.16):

```shell
$ p=devdocs v=0.3
$ wget -O ${p}-${v}.tar.gz https://github.com/dimitry-ishenko-cpp/${p}/archive/refs/tags/v${v}.tar.gz
$ tar xzf ${p}-${v}.tar.gz
$ mkdir ${p}-${v}/build
$ cd ${p}-${v}/build
$ cmake ..
$ make
$ make install
```

To install system-wide, change the above commands to:
```shell
$ cmake -DSYSTEM_INSTALL=ON ..
$ make
$ sudo make install
```

## Authors

* **Dimitry Ishenko** - dimitry (dot) ishenko (at) (gee) mail (dot) com

## License

This project is distributed under the GNU GPL license. See the
[LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

* [devdocs](https://devdocs.io)
* [fzf](https://github.com/junegunn/fzf)
* [w3m](https://w3m.sourceforge.net/)

Share and enjoy.
