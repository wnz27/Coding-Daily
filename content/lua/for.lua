--[[
Author: 27
LastEditors: 27
Date: 2024-10-22 17:03:52
LastEditTime: 2024-10-22 17:03:55
FilePath: /Coding-Daily/content/lua/for.lua
description: type some description
--]]
for i = 1, 5, 1 do
    print('first: ', i)
end

print('loop variable scope is local:', i) -- will print nil

print()

for i = 1, 10, 1 do
    print('brk: ', i)
    if i == 5 then
        break
    end
end

print()

arr = { 'a', 'b', 'c', 'd' }
for i, v in ipairs(arr) do
    print('arr: i, v', i, v)
end

print()

for i = 1, 5 do
    if i % 2 == 0 then goto customer_continue end
    print('odd: ', i)
    ::customer_continue::
end

-- while
local i = 1
while i < 5 do
    print(i)
    i = i + 1
end

while true do
    print("This loop will run forever.")
    break
end
