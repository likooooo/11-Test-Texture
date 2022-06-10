set(thirdparty ../thirdparty)

include_directories(${thirdparty}/include)
add_executable(texture texture.cpp)
# target_link_libraries(texture ${thirdparty}/lib/opencv_world455)
