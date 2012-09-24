install(
  FILES msg.lisp.template srv.lisp.template
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})

install(
  PROGRAMS gen_lisp.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
