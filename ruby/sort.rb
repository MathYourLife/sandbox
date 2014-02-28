require "set"

all_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
puts all_numbers[0]
puts "AEOU"


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

@hostgroups = {"aa"=>3, "dd"=>2, "cc"=>1}

puts (["cc"] & @hostgroups.keys).sort.join(",")

hostgroups = {"all"=>{"name"=>"all", "alias"=>"All hosts"}}

hostgroups.sort.each do |hg, data|
    puts hg
    puts data["alias"]
end

services = {
    "all" => {
      "alias" => "All Hosts",
      "checks" => [{
        "id" => "ssh",
       "hostgroup_name" => "all",
        "command_line" => "$USER1$/check_ssh $HOSTADDRESS$"
      }]
    }
  }

puts "OEUEOUOEU"
services.each do |service_name, service_data|
    service_data["checks"].each do |s|
        puts s
    end
end

#service_data["checks"].each do |service|
