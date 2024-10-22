--[[
Author: 27
LastEditors: 27
Date: 2024-10-22 17:13:12
LastEditTime: 2024-10-22 17:13:14
FilePath: /Coding-Daily/content/lua/if-else.lua
description: type some description
--]]
if 7 % 2 == 0 then
    print("7 is even")
else
    print("7 is odd")
end

if 8 % 4 == 0 then
    print("8 is divisible by 4")
end

local num = 9
if num < 0 then
    print(num, "is negative")
elseif num < 10 then
    print(num, "has 1 digit")
else
    print(num, "has multiple digits")
end
