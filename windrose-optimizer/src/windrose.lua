local Windrose = {}
Windrose.__index = Windrose

function Windrose.new(data)
    local self = setmetatable({}, Windrose)
    self.directions = data.directions or {}
    self.speeds = data.speeds or {}
    return self
end

function Windrose:get_weighted_direction()
    local sum_x, sum_y = 0, 0
    for i, dir in ipairs(self.directions) do
        local rad = math.rad(dir)
        local speed = self.speeds[i] or 1
        sum_x = sum_x + speed * math.cos(rad)
        sum_y = sum_y + speed * math.sin(rad)
    end
    local avg_rad = math.atan2(sum_y, sum_x)
    return math.deg(avg_rad) % 360
end

function Windrose:get_dominant_speed()
    local max_speed = 0
    for _, speed in ipairs(self.speeds) do
        if speed > max_speed then max_speed = speed end
    end
    return max_speed
end

return Windrose