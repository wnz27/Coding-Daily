--[[
Author: 27
LastEditors: 27
Date: 2024-10-22 16:59:03
LastEditTime: 2024-10-22 16:59:05
FilePath: /Coding-Daily/content/lua/values.lua
description: type some description
--]]
print("lua" .. 'lang')

print("1+1 =", 1 + 1)
print("7.0/3.0 =", 7.0 / 3.0)

print(true and false)
print(true or false)
print(not true)

print(true or (true and false))

if nil then
    print('nil is not true')
else
    print('nil is false')
end
