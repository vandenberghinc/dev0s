#!/usr/bin/env python3
from dev0s.shortcuts import dev0s, Array, String
import sys
dev0s.response.log_timestamps = False
dev0s.response.log(f"&GREY&Comment:&PURPLE& {String(Array(sys.argv[1:]).string(joiner=' ')).capitalized_word()}&END&")