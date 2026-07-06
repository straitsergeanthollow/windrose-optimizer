local Windrose = require("src.windrose")
local Optimizer = require("src.optimizer")

local data = {
    directions = {0, 45, 90, 135, 180, 225, 270, 315},
    speeds = {5, 3, 7, 2, 4, 6, 8, 1}
}

local wr = Windrose.new(data)
local opt = Optimizer.new(wr)

opt:add_turbine(100, 50)
opt:add_turbine(200, 150)
opt:add_turbine(300, 250)

local score = opt:compute_score()
print("Optimization score: " .. score)
print("Dominant wind direction: " .. wr:get_weighted_direction() .. "°")
print("Dominant wind speed: " .. wr:get_dominant_speed() .. " m/s")