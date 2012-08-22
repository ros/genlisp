cmake_minimum_required(VERSION 2.8)
project(genlisp)
find_package(catkin REQUIRED)

catkin_stack()
catkin_project(genlisp
  CFG_EXTRAS genlisp-extras.cmake
  )

file(WRITE ${catkin_BUILD_PREFIX}/etc/langs/genlisp "LISP")
install(FILES ${catkin_BUILD_PREFIX}/etc/langs/genlisp
  DESTINATION etc/langs
)

install(FILES stack.xml DESTINATION share/${PROJECT_NAME})

catkin_python_setup()
