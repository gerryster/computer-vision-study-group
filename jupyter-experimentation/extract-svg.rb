#!/usr/bin/env ruby

# Prints the first SVG image to standard out.

require 'json'
jupyter = JSON.parse(File.read('matplotlib-determanism.ipynb'))
puts jupyter['cells'][1]['outputs'][1]['data']['image/svg+xml']
