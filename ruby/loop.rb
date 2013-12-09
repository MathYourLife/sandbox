#!/usr/bin/env ruby

# A list of names
names = [ "Fred", "Bob", "Jim" ]

names.each do|n|
  puts "Hello #{n}"
end

contact_info = { 'name' => 'Bob', 'phone' => '111-111-1111' }

contact_info.each { |key, value| print key + ' = ' + value + "\n" }


some = [
  {"a"=>"b"}
]

some = []

some.each do|n|
    puts n["a"]
end
