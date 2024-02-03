#!/bin/bash
set -e

dir=$(dirname $(dirname $(realpath "$0")))
cd "$dir"

cp bin/devmanage.in ./devmanage
sed -i -e "s|@DEVDOCS_INSTALL_DATADIR@|$dir|g" ./devmanage

all=$(./devmanage --all | tail -n+2 | sort -rV)

new=
declare -A had
for doc in $all; do
    mod=${doc//[~0-9.]*/}
    [[ -n "${had[$mod]}" ]] || had[$mod]=1 new+=" $doc"
done

cd html
del=$(echo $new $new $(ls -1) | tr ' ' '\n' | sort -V | uniq -u)
if [[ -n "$del" ]]; then
    echo ABOUT TO DELETE ...
    echo $del
    sleep 3
    rm -r $del
fi
echo $new | xargs mkdir -p
cd ..

./devmanage --update

cp debian/control.in debian/control
for doc in $new; do
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
