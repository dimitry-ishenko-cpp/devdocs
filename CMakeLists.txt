cmake_minimum_required(VERSION 3.16) # focal
project(devdocs VERSION 0.2 LANGUAGES C)

option(SYSTEM_INSTALL "" OFF)

if(SYSTEM_INSTALL)
    include(GNUInstallDirs)
    set(DEVDOCS_INSTALL_DATADIR ${CMAKE_INSTALL_FULL_DATAROOTDIR}/${CMAKE_PROJECT_NAME})
    set(DEVDOCS_INSTALL_BINDIR ${CMAKE_INSTALL_FULL_BINDIR})
else()
    if(DEFINED ENV{XDG_DATA_HOME})
        set(DEVDOCS_INSTALL_DATADIR $ENV{XDG_DATA_HOME}/${CMAKE_PROJECT_NAME})
    else()
        set(DEVDOCS_INSTALL_DATADIR $ENV{HOME}/.local/share/${CMAKE_PROJECT_NAME})
    endif()
    set(DEVDOCS_INSTALL_BINDIR $ENV{HOME}/.local/bin)
endif()

file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/html)
install(DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/html DESTINATION ${DEVDOCS_INSTALL_DATADIR})

configure_file(devgrep.in devgrep)
configure_file(devmanage.in devmanage)
configure_file(devopen.in devopen)
install(PROGRAMS ${CMAKE_CURRENT_BINARY_DIR}/devgrep ${CMAKE_CURRENT_BINARY_DIR}/devmanage ${CMAKE_CURRENT_BINARY_DIR}/devopen DESTINATION ${DEVDOCS_INSTALL_BINDIR})
