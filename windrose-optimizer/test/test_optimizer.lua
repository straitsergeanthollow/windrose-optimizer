local Windrose = require("src.windrose")
local Optimizer = require("src.optimizer")

local data = {
    directions = {0, 90, 180, 270},
    speeds = {10, 5, 10, 5}
}

local wr = Windrose.new(data)
local opt = Optimizer.new(wr)

opt:add_turbine(1, 0)
opt:add_turbine(0, 1)

local score = opt:compute_score()
local dir = wr:get_weighted_direction()
local speed = wr:get_dominant_speed()

assert(math.abs(dir - 0) < 0.01, "Expected direction near 0°, got " .. dir)
assert(math.abs(speed - 10) < 0.01, "Expected speed 10, got " .. speed)
assert(score > 0, "Score should be positive")

print("All tests passed.")