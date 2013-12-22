require "set"

set = SortedSet.new([2, 1, 5, 6, 4, 5, 3, 3, 3])
ary = []

set.each do |obj|
  ary << obj
end

puts ary

hosts = Set.new()

hosts << {"a" => "hosta", "b" => 5}
hosts << {"a" => "hosx.aou,.au", "b" => 4}
hosts << {"a" => "hostb", "b" => 9}

hosts.merge([
    {"a" => "ha", "b" => 6},
    {"a" => "ho", "b" => 1},
])

gs = hosts.sort_by { |v| v["a"] }

gs.each do |g|
    puts g
end


