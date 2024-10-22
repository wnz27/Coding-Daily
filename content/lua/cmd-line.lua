--[[
Author: 27
LastEditors: 27
Date: 2024-10-22 17:54:06
LastEditTime: 2024-10-22 17:54:08
FilePath: /Coding-Daily/content/lua/cmd-line.lua
description: type some description
--]]
local function dump(o)
    if type(o) == 'table' then
        local s = '{ '
        for k, v in pairs(o) do
            if type(k) ~= 'number' then k = '"' .. k .. '"' end
            s = s .. '[' .. k .. '] = ' .. dump(v) .. ','
        end
        return s .. '} '
    else
        return tostring(o)
    end
end

local args = { ... }

print(dump(args))
