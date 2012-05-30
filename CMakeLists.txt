cmake_minimum_required(VERSION 2.8)
project(genlisp)
find_package(catkin)
find_package(genmsg)

catkin_stack()
catkin_project(genlisp
  CFG_EXTRAS genlisp-extras.cmake
  )

file(WRITE ${CMAKE_CURRENT_BINARY_DIR}/genlisp "LISP")
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/genlisp
  DESTINATION etc/langs
)

install(FILES stack.xml DESTINATION share/${PROJECT_NAME})

catkin_python_setup()
