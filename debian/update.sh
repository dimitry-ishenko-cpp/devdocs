#!/bin/bash

dir=$(dirname $(dirname $(realpath "$0")))
cd "$dir"

cp bin/devmanage.in ./devmanage
sed -i -e "s|@DEVDOCS_INSTALL_DATADIR@|$dir|g" ./devmanage

mkdir -p html
(cd html && ../devmanage --all | tail -n+2 | xargs mkdir -p)

./devmanage --update

cp debian/control.in debian/control
for doc in $(cd html && ls -1); do
    deb="devdocs-data-${doc//[_~]/-}"
    cat <<EOF >> debian/control

Package: $deb
Architecture: all
Depends: \${misc:Depends},
 devdocs (= \${binary:Version})
Description: View devdocs offline in a terminal
 This package contains offline data for $doc.
EOF

    echo "usr/share/devdocs/html/$doc" > debian/$deb.install
done

rm ./devmanage
