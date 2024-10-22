--[[
Author: 27
LastEditors: 27
Date: 2024-10-22 17:32:53
LastEditTime: 2024-10-22 17:33:00
FilePath: /Coding-Daily/content/lua/functions.lua
description: type some description
--]]
local function plus(a, b)
    return a + b
end

print("1+2 =" .. plus(1, 2))

local subtract = function(a, b)
    return a - b
end

print("2-1 =" .. subtract(2, 1))


local function values()
    return 3, 7
end

a, b = values()
print(a)
print(b)

_, c = values()
print(c)

print()

-- 多参数

local function sum(...)
    print("items: ", ...)
    total = 0
    for idx, num in ipairs({ ... }) do
        total = total + num
    end
    print("total: ", total)
end

sum(1, 2)
sum(1, 2, 3)

nums = { 1, 2, 3, 4 }
sum(table.unpack(nums))
