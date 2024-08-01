/*
 * @Author: 27
 * @LastEditors: 27
 * @Date: 2024-07-28 23:41:20
 * @LastEditTime: 2024-08-01 08:59:00
 * @FilePath: /Coding-Daily/content/C_language/cpp/lessons/l1.c++
 * @description: type some description
 */
#include <array>
#include <iostream>

int d1() {
  std::cout << "Hello World!" << std::endl;
  return 0;
}

int d2() {

  std::array<int, 5> my_array;

  for (size_t i = 0; i < my_array.size(); i++) {
    my_array[i] = i;
  }

  std::cout << my_array[2] << std::endl;
  return 0;
}

int main() { d2(); }
