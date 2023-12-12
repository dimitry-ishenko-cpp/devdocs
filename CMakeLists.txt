cmake_minimum_required(VERSION 3.16) # focal
project(devdocs VERSION 0.0 LANGUAGES C)

include(GNUInstallDirs)
set(DEVDOCS_INSTALL_DIR ${CMAKE_INSTALL_FULL_DATAROOTDIR}/${CMAKE_PROJECT_NAME})

install(DIRECTORY html DESTINATION ${DEVDOCS_INSTALL_DIR})
install(FILES info.py README.md update.conf update.py DESTINATION ${DEVDOCS_INSTALL_DIR})

configure_file(devopen.in devopen)
install(PROGRAMS ${CMAKE_CURRENT_BINARY_DIR}/devopen DESTINATION ${CMAKE_INSTALL_BINDIR})

configure_file(devgrep.in devgrep)
install(PROGRAMS ${CMAKE_CURRENT_BINARY_DIR}/devgrep DESTINATION ${CMAKE_INSTALL_BINDIR})
