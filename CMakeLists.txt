cmake_minimum_required(VERSION 2.8)
project(genlisp)
find_package(catkin REQUIRED COMPONENTS genmsg)

catkin_stack()
catkin_package(${PROJECT_NAME}
  CFG_EXTRAS genlisp-extras.cmake)

file(WRITE ${CATKIN_BUILD_PREFIX}/${GENMSG_LANGS_DESTINATION}/genlisp "LISP")
install(FILES ${CATKIN_BUILD_PREFIX}/${GENMSG_LANGS_DESTINATION}/genlisp
  DESTINATION ${GENMSG_LANGS_DESTINATION})

catkin_python_setup()
