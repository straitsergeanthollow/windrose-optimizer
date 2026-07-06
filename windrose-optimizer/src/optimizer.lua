local Optimizer = {}
Optimizer.__index = Optimizer

function Optimizer.new(windrose)
    local self = setmetatable({}, Optimizer)
    self.windrose = windrose
    self.turbines = {}
    return self
end

function Optimizer:add_turbine(x, y)
    table.insert(self.turbines, {x = x, y = y})
end

function Optimizer:compute_score()
    local dir = self.windrose:get_weighted_direction()
    local speed = self.windrose:get_dominant_speed()
    local rad = math.rad(dir)
    local score = 0
    for _, t in ipairs(self.turbines) do
        local proj = t.x * math.cos(rad) + t.y * math.sin(rad)
        score = score + proj * speed
    end
    return score
end

return Optimizer